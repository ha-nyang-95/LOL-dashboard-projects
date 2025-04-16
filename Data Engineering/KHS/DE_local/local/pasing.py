import ijson
import pandas as pd
from tqdm import tqdm
from pathlib import Path

def stream_matches_from_large_json(json_path):
    """
    메모리 효율적으로 경기 단위로 stream 파싱
    """
    with open(json_path, 'r', encoding='utf-8') as f:
        for match_id, match_data in ijson.kvitems(f, ''):
            yield match_id, match_data


def extract_events(match_id, match_data):
    """
    해당 경기의 모든 프레임에서 events 추출
    """
    frames = match_data.get("info", {}).get("frames", [])
    for frame in frames:
        timestamp = frame.get("timestamp")
        for event in frame.get("events", []):
            event["timestamp"] = timestamp//60000
            event["match_id"] = match_id
            yield event


def parse_large_json_to_csv(json_path, output_dir="output", save_every=100000):
    """
    전체 JSON에서 events를 파싱해 batch 단위로 CSV 저장
    """
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    temp_rows = []
    batch = 0
    total_events = 0

    for match_id, match_data in tqdm(stream_matches_from_large_json(json_path), desc="Processing Matches"):
        for event in extract_events(match_id, match_data):
            temp_rows.append(event)
            total_events += 1

        # 일정 개수마다 저장
        if len(temp_rows) >= save_every:
            df = pd.json_normalize(temp_rows)
            df.to_csv(f"{output_dir}/events_batch_{batch}.csv", index=False)
            print(f"✅ Saved events_batch_{batch}.csv ({len(temp_rows)} rows)")
            temp_rows.clear()
            batch += 1

    # 남은 데이터 저장
    if temp_rows:
        df = pd.json_normalize(temp_rows)
        df.to_csv(f"{output_dir}/events_batch_{batch}.csv", index=False)
        print(f"✅ Saved events_batch_{batch}.csv ({len(temp_rows)} rows)")

    print(f"\n🎉 전체 이벤트 파싱 완료: {total_events} rows across {batch + 1} files")



# 실행 (예시)
if __name__ == "__main__":
    parse_large_json_to_csv("matches_details_time.json")
