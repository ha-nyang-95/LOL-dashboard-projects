import requests, sys, json, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 🔐 새로 발급받은 Riot API 키를 여기에 입력
API_KEY = 'RGAPI-17f8bed5-3cde-4b80-a75b-47dc7ade2fa1'

# 🔧 유저 정보
summoner_name = 'Hide on bush'  # 예시 소환사 이름
region = 'KR'                   # 소환사 정보용 (kr, jp1 등)
continent = 'ASIA'

# 🛡️ 요청 헤더
headers = {
    "X-Riot-Token": API_KEY
}

# 1. 소환사 이름으로 PUUID 가져오기
def get_puuid(summoner_name):
    url = f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()['puuid']
    else:
        raise Exception(f"PUUID 요청 실패: {response.status_code}, {response.text}")

# 2. PUUID로 최근 솔로랭크 매치 ID 1개 가져오기
def get_recent_solo_match_id(puuid):
    url = f"https://{continent}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids"
    params = {
        "start": 0,
        "count": 1,
        "queue": 420  # 솔로랭크 큐 ID
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        match_ids = response.json()
        if match_ids:
            return match_ids[0]
        else:
            raise Exception("솔로랭크 매치 없음.")
    else:
        raise Exception(f"매치 ID 요청 실패: {response.status_code}, {response.text}")

# 3. 매치 ID로 상세 매치 정보 가져오기
def get_match_detail(match_id):
    url = f"https://{continent}.api.riotgames.com/lol/match/v5/matches/{match_id}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"매치 상세 요청 실패: {response.status_code}, {response.text}")

# 🧪 실행 메인 함수
def main():
    try:
        print("▶ 소환사 이름으로 PUUID 조회 중...")
        puuid = get_puuid(summoner_name)
        print(f"PUUID: {puuid}\n")

        print("▶ 최근 솔로랭크 매치 ID 조회 중...")
        match_id = get_recent_solo_match_id(puuid)
        print(f"Match ID: {match_id}\n")

        print("▶ 매치 상세 정보 가져오는 중...")
        match_detail = get_match_detail(match_id)

        # 예쁘게 출력 (optionally 전체 내용 보기)
        print(json.dumps(match_detail, indent=2))  

    except Exception as e:
        print(f"오류 발생: {e}")

if __name__ == "__main__":
    main()
