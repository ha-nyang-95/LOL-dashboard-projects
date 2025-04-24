import requests
import time
import json

# Riot API Key
api_key = "RGAPI-cbd31053-71be-4f2e-81cd-123550e39f60"
headers = {"X-Riot-Token": api_key}
call_timestamps = []

# Rate Limiting 대응
def rate_limited_get(url, headers, max_retries=3, timeout=10):
    global call_timestamps
    now = time.time()
    call_timestamps = [t for t in call_timestamps if now - t < 120]

    if len(call_timestamps) >= 99:
        wait_time = 120 - (now - call_timestamps[0]) + 0.1
        print(f"[RATE LIMIT] 대기 중... {wait_time:.2f}초")
        time.sleep(wait_time)
        now = time.time()
        call_timestamps = [t for t in call_timestamps if now - t < 120]

    call_timestamps.append(now)

    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=headers, timeout=timeout)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"[{attempt+1}/{max_retries}] 요청 실패: {e} → 재시도 중...")
            time.sleep(2)
    print(f"[FAIL] 요청 실패 (URL): {url}")
    return None

# Riot ID → Account Info → PUUID
def get_account_info(name, tag):
    url = f"https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{name}/{tag}"
    return rate_limited_get(url, headers)

# PUUID → matchId 목록
def get_match_ids(puuid, count=100):  # 넉넉하게 50개 가져오자
    url = f"https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count={count}"
    return rate_limited_get(url, headers)

# matchId → match 정보
def get_match_info(match_id):
    url = f"https://asia.api.riotgames.com/lol/match/v5/matches/{match_id}"
    return rate_limited_get(url, headers)

# matchId → timeline 정보
def get_timeline(match_id):
    url = f"https://asia.api.riotgames.com/lol/match/v5/matches/{match_id}/timeline"
    return rate_limited_get(url, headers)

# 실행
summoner_name = "제철대방어"
summoner_tag = "KR1"
timeline_results = {}

# 1. 소환사 정보 조회
account_res = get_account_info(summoner_name, summoner_tag)
if not account_res:
    print("소환사 정보 조회 실패")
    exit()
puuid = account_res.json().get("puuid")

# 2. 매치 ID 목록 조회
matches_res = get_match_ids(puuid)
if not matches_res:
    print("매치 ID 조회 실패")
    exit()
match_ids = matches_res.json()

# 3. match info 확인하고, classic 게임만 timeline 저장
for match_id in match_ids:
    if len(timeline_results) >= 10:
        break

    info_res = get_match_info(match_id)
    if not info_res or info_res.status_code != 200:
        print(f"[{match_id}] match info 조회 실패")
        continue

    game_mode = info_res.json().get("info", {}).get("gameMode")
    if game_mode != "CLASSIC":
        print(f"[{match_id}] gameMode = {game_mode} → 제외")
        continue

    timeline_res = get_timeline(match_id)
    if timeline_res and timeline_res.status_code == 200:
        timeline_results[match_id] = timeline_res.json()
        print(f"[{match_id}] ✅ 저장 완료 ({len(timeline_results)}/10)")
    else:
        print(f"[{match_id}] ❌ timeline 조회 실패")

# 4. 저장
with open("제철대방어_CLASSIC_10경기_timeline.json", "w", encoding="utf-8") as f:
    json.dump(timeline_results, f, ensure_ascii=False, indent=4)

print("🎉 완료: 제철대방어의 CLASSIC 모드 타임라인 10경기 저장 완료!")
