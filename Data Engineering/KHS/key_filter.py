import json

def extract_unique_keys(data, parent=''):
    """
    중첩 JSON 구조에서 모든 고유 key 경로를 추출
    (list index는 무시하고 구조만 기반으로)
    """
    keys = set()

    if isinstance(data, dict):
        for k, v in data.items():
            new_key = f"{parent}.{k}" if parent else k
            keys |= extract_unique_keys(v, new_key)

    elif isinstance(data, list):
        for item in data:
            # index 없이 리스트 내부 구조만 탐색
            keys |= extract_unique_keys(item, parent)
        if not data:
            keys.add(parent + "[]")  # 빈 리스트는 따로 표시

    else:
        keys.add(parent)

    return keys

# 예시 사용
if __name__ == "__main__":
    # 파일 경로 설정 (예: match_timeline.json)
    file_path = "./single_sample.json"

    with open(file_path, "r", encoding="utf-8") as f:
        json_data = json.load(f)

    # 전체 key 경로 추출
    key_set = extract_unique_keys(json_data)

    # 결과 확인
    print(f"전체 고유 컬럼 수: {len(key_set)}")
    for key in sorted(key_set):
        print(key)

with open("Keys_list.txt", "w", encoding="utf-8") as f:
    for key in sorted(key_set):  # 혹은 key_set
        f.write(key + "\n")
