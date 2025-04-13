import json
import csv

# JSON 파일 로드
def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

# JSON에서 데이터 전체 추출
def extract_json_data(json_data):
    match_id = list(json_data.keys())[0]
    match_data = json_data[match_id]

    # match 데이터
    match_record = {
        "match_id": match_id,
        "data_version": match_data['metadata']['dataVersion'],
        "end_of_game_result": match_data['info']['endOfGameResult'],
        "frame_interval": match_data['info']['frameInterval']
    }

    # participants 데이터
    participant_records = [
        {"match_id": match_id, "puuid": puuid}
        for puuid in match_data['metadata']['participants']
    ]

    # frames, events, participant_frames 데이터
    frame_records = []
    event_records = []
    participant_frame_records = []

    for frame in match_data['info']['frames']:
        frame_timestamp = frame['timestamp']
        frame_record = {
            "match_id": match_id,
            "timestamp": frame_timestamp
        }
        frame_records.append(frame_record)

        # events 데이터 전부 추출
        for event in frame.get('events', []):
            event_record = {
                "match_id": match_id,
                "frame_timestamp": frame_timestamp,
                "event_type": event.get('type'),
                "participant_id": event.get('participantId'),
                "item_id": event.get('itemId'),
                "skill_slot": event.get('skillSlot'),
                "timestamp": event.get('timestamp')//60000,
                "additional_data": json.dumps(event)
            }
            event_records.append(event_record)

        # participant_frames 데이터 전부 추출
        for participant_id, p_frame in frame.get('participantFrames', {}).items():
            participant_frame_record = {
                "match_id": match_id,
                "frame_timestamp": frame_timestamp,
                "participant_id": int(participant_id),
                "current_gold": p_frame.get('currentGold'),
                "total_gold": p_frame.get('totalGold'),
                "level": p_frame.get('level'),
                "xp": p_frame.get('xp'),
                "champion_stats": json.dumps(p_frame.get('championStats'))
            }
            participant_frame_records.append(participant_frame_record)

    return {
        "match": match_record,
        "participants": participant_records,
        "frames": frame_records,
        "events": event_records,
        "participant_frames": participant_frame_records
    }

# CSV 저장 함수
def save_to_csv(data, filename, columns):
    with open(filename, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(data)

# 메인 실행부
if __name__ == "__main__":
    json_filepath = "../single_match_timeline.json"
    json_data = load_json(json_filepath)
    parsed_data = extract_json_data(json_data)

    # matches CSV
    save_to_csv([parsed_data['match']], 'matches.csv', [
        "match_id", "data_version", "end_of_game_result", "frame_interval"
    ])

    # participants CSV
    save_to_csv(parsed_data['participants'], 'participants.csv', [
        "match_id", "puuid"
    ])

    # frames CSV
    save_to_csv(parsed_data['frames'], 'frames.csv', [
        "match_id", "timestamp"
    ])

    # events CSV (전체 데이터 포함)
    save_to_csv(parsed_data['events'], 'events.csv', [
        "match_id", "frame_timestamp", "event_type", "participant_id",
        "item_id", "skill_slot", "timestamp", "additional_data"
    ])

    # participant_frames CSV (전체 데이터 포함)
    save_to_csv(parsed_data['participant_frames'], 'participant_frames.csv', [
        "match_id", "frame_timestamp", "participant_id",
        "current_gold", "total_gold", "level", "xp", "champion_stats"
    ])

    print("모든 데이터가 CSV 파일로 저장되었습니다.")
