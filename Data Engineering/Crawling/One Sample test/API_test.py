import requests
import time
import json
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')



# Riot API 인증 키
api_key = "RGAPI-17f8bed5-3cde-4b80-a75b-47dc7ade2fa1"
headers = {"X-Riot-Token": api_key}

# Rate limit 대응
def rate_limited_get(url, headers, max_retries=3, timeout=10):
    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=headers, timeout=timeout)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"[{attempt+1}/{max_retries}] 요청 실패: {e}, 재시도 중...")
            time.sleep(2)
    return None

# 챌린저 티어 유저 리스트 → 첫 번째 유저 1명
def get_challenger_puuid():
    url = "https://kr.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5"
    response = rate_limited_get(url, headers)
    if response and response.status_code == 200:
        data = response.json()["entries"]
        summoner_id = data[0]["summonerId"]  # 첫 번째 유저
        # summonerId → puuid 얻기
        summoner_url = f"https://kr.api.riotgames.com/lol/summoner/v4/summoners/{summoner_id}"
        summoner_resp = rate_limited_get(summoner_url, headers)
        if summoner_resp and summoner_resp.status_code == 200:
            return summoner_resp.json()["puuid"]
    return None

# puuid → 단 하나의 매치 ID
def get_single_match_id(puuid):
    url = f"https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=1&type=ranked"
    response = rate_limited_get(url, headers)
    if response and response.status_code == 200:
        match_ids = response.json()
        if match_ids:
            return match_ids[0]
    return None

# matchId → 타임라인 데이터
def get_match_timeline(match_id):
    url = f"https://asia.api.riotgames.com/lol/match/v5/matches/{match_id}/timeline"
    response = rate_limited_get(url, headers)
    if response and response.status_code == 200:
        return response.json()
    return None

# 메인 실행
def main():
    print("▶ 챌린저 유저 중 1명의 PUUID 가져오는 중...")
    puuid = get_challenger_puuid()
    if not puuid:
        print("PUUID 조회 실패")
        return

    print("▶ 단 하나의 매치 ID 가져오는 중...")
    match_id = get_single_match_id(puuid)
    if not match_id:
        print("매치 ID 조회 실패")
        return
    print("Match ID:", match_id)

    print("▶ 매치 타임라인 가져오는 중...")
    timeline_data = get_match_timeline(match_id)
    if not timeline_data:
        print("타임라인 데이터 조회 실패")
        return

    # 저장
    with open("single_match_timeline.json", "w", encoding="utf-8") as f:
        json.dump({match_id: timeline_data}, f, ensure_ascii=False, indent=4)

    print("단일 매치 타임라인 데이터를 저장했습니다.")

if __name__ == "__main__":
    main()
