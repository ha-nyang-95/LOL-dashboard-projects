import json
import pandas as pd
from pathlib import Path

# JSON 로드
with open("single_match_timeline.json", "r", encoding="utf-8") as f:
    raw = json.load(f)

match_id = list(raw.keys())[0]
match_data = raw[match_id]

# --------------------------
# 1. matches 테이블
# --------------------------
matches_df = pd.DataFrame([{
    "match_id": match_id,
    "game_id": match_data["info"].get("gameId"),
    "data_version": match_data["metadata"].get("dataVersion"),
    "end_of_game_result": match_data["info"].get("endOfGameResult"),
    "frame_interval": match_data["info"].get("frameInterval")
}])

# --------------------------
# 2. participants 테이블
# --------------------------
participants_df = pd.DataFrame([
    {
        "match_id": match_id,
        "participant_id": p["participantId"],
        "puuid": p["puuid"]
    }
    for p in match_data["info"].get("participants", [])
])

# --------------------------
# 3. frames + participant_frames 테이블
# --------------------------
frames = match_data["info"]["frames"]
frames_df = []
participant_frames_df = []

for frame in frames:
    frame_ts = frame["timestamp"]
    frames_df.append({"match_id": match_id, "timestamp": frame_ts})

    for pid_str, p_data in frame["participantFrames"].items():
        pid = int(pid_str)
        row = {
            "match_id": match_id,
            "participant_id": pid,
            "frame_timestamp": frame_ts,
            "current_gold": p_data.get("currentGold"),
            "total_gold": p_data.get("totalGold"),
            "xp": p_data.get("xp"),
            "level": p_data.get("level"),
            "minions_killed": p_data.get("minionsKilled"),
            "jungle_minions_killed": p_data.get("jungleMinionsKilled"),
            "gold_per_second": p_data.get("goldPerSecond"),
            "time_enemy_spent_controlled": p_data.get("timeEnemySpentControlled"),
        }

        # position
        pos = p_data.get("position", {})
        row["position_x"] = pos.get("x")
        row["position_y"] = pos.get("y")

        # championStats
        for k, v in p_data.get("championStats", {}).items():
            row[f"champion_{k.lower()}"] = v

        # damageStats
        for k, v in p_data.get("damageStats", {}).items():
            row[f"damage_{k[0].lower() + k[1:]}"] = v

        participant_frames_df.append(row)

frames_df = pd.DataFrame(frames_df)
participant_frames_df = pd.DataFrame(participant_frames_df)

# --------------------------
# 4. events 테이블 (기본)
# --------------------------
events_rows = []
for frame in frames:
    for e in frame.get("events", []):
        row = {
            "match_id": match_id,
            "frame_timestamp": frame["timestamp"],
            "timestamp": e.get("timestamp"),
            "real_timestamp": e.get("realTimestamp"),
            "type": e.get("type"),
            "participant_id": e.get("participantId"),
            "killer_id": e.get("killerId"),
            "victim_id": e.get("victimId"),
            "creator_id": e.get("creatorId"),
            "item_id": e.get("itemId"),
            "skill_slot": e.get("skillSlot"),
            "position_x": e.get("position", {}).get("x") if e.get("position") else None,
            "position_y": e.get("position", {}).get("y") if e.get("position") else None,
            "level": e.get("level"),
            "level_up_type": e.get("levelUpType"),
            "ward_type": e.get("wardType"),
            "building_type": e.get("buildingType"),
            "tower_type": e.get("towerType"),
            "lane_type": e.get("laneType"),
            "monster_type": e.get("monsterType"),
            "monster_sub_type": e.get("monsterSubType"),
            "shutdown_bounty": e.get("shutdownBounty"),
            "bounty": e.get("bounty"),
            "gold_gain": e.get("goldGain"),
            "kill_streak_length": e.get("killStreakLength"),
            "multi_kill_length": e.get("multiKillLength"),
            "kill_type": e.get("killType"),
            "team_id": e.get("teamId"),
            "winning_team": e.get("winningTeam"),
        }
        events_rows.append(row)

events_df = pd.DataFrame(events_rows)



# 6. event_assists.csv
assist_rows = []
for frame in frames:
    frame_ts = frame["timestamp"]
    for event in frame.get("events", []):
        if event.get("assistingParticipantIds"):
            for pid in event["assistingParticipantIds"]:
                assist_rows.append({
                    "match_id": match_id,
                    "frame_timestamp": frame_ts,
                    "event_timestamp": event.get("timestamp"),
                    "event_type": event.get("type"),
                    "participant_id": pid
                })
assist_df = pd.DataFrame(assist_rows)

# 7. event_victim_damage_dealt.csv
dealt_rows = []
for frame in frames:
    frame_ts = frame["timestamp"]
    for event in frame.get("events", []):
        if event.get("victimDamageDealt"):
            for idx, dmg in enumerate(event["victimDamageDealt"], start=1):
                dealt_rows.append({
                    "match_id": match_id,
                    "frame_timestamp": frame_ts,
                    "event_timestamp": event.get("timestamp"),
                    "instance": idx,
                    "basic": dmg.get("basic"),
                    "magic_damage": dmg.get("magicDamage"),
                    "physical_damage": dmg.get("physicalDamage"),
                    "true_damage": dmg.get("trueDamage"),
                    "name": dmg.get("name"),
                    "participant_id": dmg.get("participantId"),
                    "spell_name": dmg.get("spellName"),
                    "spell_slot": dmg.get("spellSlot"),
                    "type": dmg.get("type")
                })
dealt_df = pd.DataFrame(dealt_rows)

# 8. event_victim_damage_received.csv
received_rows = []
for frame in frames:
    frame_ts = frame["timestamp"]
    for event in frame.get("events", []):
        if event.get("victimDamageReceived"):
            for idx, dmg in enumerate(event["victimDamageReceived"], start=1):
                received_rows.append({
                    "match_id": match_id,
                    "frame_timestamp": frame_ts,
                    "event_timestamp": event.get("timestamp"),
                    "instance": idx,
                    "basic": dmg.get("basic"),
                    "magic_damage": dmg.get("magicDamage"),
                    "physical_damage": dmg.get("physicalDamage"),
                    "true_damage": dmg.get("trueDamage"),
                    "name": dmg.get("name"),
                    "participant_id": dmg.get("participantId"),
                    "spell_name": dmg.get("spellName"),
                    "spell_slot": dmg.get("spellSlot"),
                    "type": dmg.get("type")
                })
received_df = pd.DataFrame(received_rows)
# CSV 저장 경로 (현재 작업 디렉토리에 저장됨)
output_dir = Path("./csv_outputs")
output_dir.mkdir(parents=True, exist_ok=True)  # 폴더 없으면 자동 생성
# 각 DataFrame을 CSV로 저장
assist_df.to_csv(output_dir / "event_assists.csv", index=False)
dealt_df.to_csv(output_dir / "event_victim_damage_dealt.csv", index=False)
received_df.to_csv(output_dir / "event_victim_damage_received.csv", index=False)
matches_df.to_csv(output_dir / "matches.csv", index=False, encoding="utf-8-sig")
participants_df.to_csv(output_dir / "participants.csv", index=False, encoding="utf-8-sig")
frames_df.to_csv(output_dir / "frames.csv", index=False, encoding="utf-8-sig")
participant_frames_df.to_csv(output_dir / "participant_frames.csv", index=False, encoding="utf-8-sig")
events_df.to_csv(output_dir / "events.csv", index=False, encoding="utf-8-sig")

print("✅ 모든 DataFrame을 CSV 파일로 저장 완료했습니다. 폴더 경로: ./csv_outputs")
