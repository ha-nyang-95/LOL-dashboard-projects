import requests
import time
import json

# Riot API 인증 키
api_key = "RGAPI-17f8bed5-3cde-4b80-a75b-47dc7ade2fa1"
headers = {"X-Riot-Token": api_key}

# 최근 호출 시간 기록 (API 제한 대응용)
call_timestamps = []

# Rate Limit + 예외처리 + 자동 재시도
def rate_limited_get(url, headers, max_retries=3, timeout=10):
    global call_timestamps
    now = time.time()
    call_timestamps = [t for t in call_timestamps if now - t < 120]
    
    if len(call_timestamps) >= 99:
        wait_time = 120 - (now - call_timestamps[0]) + 0.1
        print(f"Rate limit reached. Sleeping for {wait_time:.2f} seconds...")
        time.sleep(wait_time)
        now = time.time()
        call_timestamps = [t for t in call_timestamps if now - t < 120]
    
    call_timestamps.append(now)

    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=headers, timeout=timeout)
            response.raise_for_status()
            return response
        except requests.exceptions.ChunkedEncodingError:
            print(f"[{attempt+1}/{max_retries}] ChunkedEncodingError - 재시도 중...")
            time.sleep(2)
        except requests.exceptions.RequestException as e:
            print(f"[{attempt+1}/{max_retries}] 요청 예외 발생: {e} - 재시도 중...")
            time.sleep(2)

    print(f"[FAIL] 요청 실패 (URL): {url}")
    return None

# 티어별 소환사 목록 가져오기
def lol_tier(tier):
    queue = "RANKED_SOLO_5x5"
    if tier.lower() == "challenger":
        url = f"https://kr.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/{queue}"
    else:
        url = f"https://kr.api.riotgames.com/lol/league/v4/grandmasterleagues/by-queue/{queue}"
    return rate_limited_get(url, headers)

# 소환사별 매치 ID 가져오기
def match_list(puuid, start=0, count=20):
    startTime = 1743811200  # 2025-04-05 00:00:00 UTC
    endTime = 1743897600    # 2025-04-06 00:00:00 UTC
    url = (
        f"https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids"
        f"?startTime={startTime}&endTime={endTime}&type=ranked&start={start}&count={count}"
    )
    return rate_limited_get(url, headers)

# 매치 타임라인 상세 정보 가져오기
def match_detail(matchId):
    url = f"https://asia.api.riotgames.com/lol/match/v5/matches/{matchId}/timeline"
    return rate_limited_get(url, headers)

# 1. 티어별 소환사 PUUID 수집
puuids = []
tiers = ["challenger", "grandmaster"]
for tier in tiers:
    req = lol_tier(tier)
    if req and req.status_code == 200:
        data = req.json()["entries"]
        for item in data:
            puuid = item.get("puuid")
            if puuid:
                puuids.append(puuid)
    else:
        print(f"{tier} 티어 데이터 조회 실패:", req.status_code if req else "No Response")

# 2. 모든 소환사의 매치 ID 수집 및 중복 제거
unique_match_ids = set()
for puuid in puuids:
    req = match_list(puuid)
    if req and req.status_code == 200:
        match_ids = req.json()
        unique_match_ids.update(match_ids)
    else:
        print("매치 목록 조회 실패 (PUUID):", puuid, req.status_code if req else "No Response")

# 3. 매치 ID 기준으로 상세 데이터 조회 및 저장
match_details_dict = {}
for match_id in unique_match_ids:
    detail_req = match_detail(match_id)
    if detail_req and detail_req.status_code == 200:
        match_details_dict[match_id] = detail_req.json()
    else:
        print(
            "매치 상세 조회 실패 (matchId):",
            match_id,
            detail_req.status_code if detail_req else "No Response"
        )

# 4. 결과를 JSON 파일로 저장 (PUUID 없이 matchId 기준)
with open("matches_details_time.json", "w", encoding="utf-8") as f:
    json.dump(match_details_dict, f, ensure_ascii=False, indent=4)

print("모든 매치 상세 데이터를 matches_details_time.json 파일에 저장하였습니다.")