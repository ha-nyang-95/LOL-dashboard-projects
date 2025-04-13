import json

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

timeline_json = load_json('single_match_timeline.json')

def parse_match_data(raw_json):
    match_key = list(raw_json.keys())[0]
    data = raw_json[match_key]

    parsed_data = {
        "matchId": data["metadata"]["matchId"],
        "participants": data["metadata"]["participants"],
        "frames": []
    }

    for frame in data["info"]["frames"]:
        frame_dict = {
            "timestamp": frame["timestamp"],
            "events": frame.get("events", []),
            "participantFrames": frame.get("participantFrames", {})
        }
        parsed_data["frames"].append(frame_dict)

    return parsed_data

parsed_data = parse_match_data(timeline_json)

def save_parsed_json(parsed_json, filename='parsed_match_data.json'):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(parsed_json, f, ensure_ascii=False, indent=4)

save_parsed_json(parsed_data)
