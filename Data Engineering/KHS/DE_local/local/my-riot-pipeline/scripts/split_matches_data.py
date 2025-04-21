import json
import pandas as pd
from pathlib import Path
from tqdm import tqdm

# JSON 로드
with open("matches_details_time.json", "r", encoding="utf-8") as f:
    all_data = json.load(f)

# 저장 경로
output_dir = Path("./specific_data")

output_dir.mkdir(exist_ok=True)

# 누적 리스트 초기화
matches_rows = []
participants_rows = []
frames_rows = []
participant_frame_rows = []
events_rows = []
event_assists_rows = []
event_victim_damage_dealt_rows = []
event_victim_damage_received_rows = []

for match_id, match_data in tqdm(all_data.items(), desc="Processing matches"):
    info = match_data["info"]
    metadata = match_data["metadata"]
    frames_list = info.get("frames", [])
    game_id = info.get("gameId")

    # 1. matches
    matches_rows.append({
        "match_id": match_id,
        "game_id": game_id,
        "data_version": metadata.get("dataVersion"),
        "end_of_game_result": info.get("endOfGameResult"),
        "frame_interval": info.get("frameInterval")
    })

    # 2. participants
    for p in info.get("participants", []):
        participants_rows.append({
            "game_id": game_id,
            "participant_id": p["participantId"],
            "puuid": p["puuid"]
        })

    # 3. frames / 4. participant_frames
    for frame in frames_list:
        frame_ts = frame["timestamp"]
        frames_rows.append({
            "game_id": game_id,
            "timestamp": frame_ts
        })

        for pid_str, pf in frame.get("participantFrames", {}).items():
            part_id = int(pid_str)
            row = {
                "game_id": game_id,
                "participant_id": part_id,
                "frame_timestamp": frame_ts,
                "current_gold": pf.get("currentGold"),
                "gold_per_second": pf.get("goldPerSecond"),
                "jungle_minions_killed": pf.get("jungleMinionsKilled"),
                "level": pf.get("level"),
                "minions_killed": pf.get("minionsKilled"),
                "time_enemy_spent_controlled": pf.get("timeEnemySpentControlled"),
                "total_gold": pf.get("totalGold"),
                "xp": pf.get("xp"),
                "position_x": pf.get("position", {}).get("x"),
                "position_y": pf.get("position", {}).get("y"),
            }
            for k, v in pf.get("championStats", {}).items():
                row[f"{k.lower()}"] = v
            for k, v in pf.get("damageStats", {}).items():
                row[f"{k[0].lower() + k[1:]}"] = v
            participant_frame_rows.append(row)

    # 5. events & sub tables
    for frame in frames_list:
        frame_ts = frame["timestamp"]
        for event in frame.get("events", []):
            events_rows.append({
                "game_id": game_id,
                "frame_timestamp": frame_ts,
                "timestamp": event.get("timestamp"),
                "real_timestamp": event.get("realTimestamp"),
                "type": event.get("type"),
                "participant_id": event.get("participantId"),
                "killer_id": event.get("killerId"),
                "victim_id": event.get("victimId"),
                "creator_id": event.get("creatorId"),
                "killer_team_id": event.get("killerTeamId"),
                "team_id": event.get("teamId"),
                "item_id": event.get("itemId"),
                "before_id": event.get("beforeId"),
                "after_id": event.get("afterId"),
                "skill_slot": event.get("skillSlot"),
                "level_up_type": event.get("levelUpType"),
                "level": event.get("level"),
                "ward_type": event.get("wardType"),
                "building_type": event.get("buildingType"),
                "tower_type": event.get("towerType"),
                "lane_type": event.get("laneType"),
                "monster_type": event.get("monsterType"),
                "monster_sub_type": event.get("monsterSubType"),
                "kill_streak_length": event.get("killStreakLength"),
                "multi_kill_length": event.get("multiKillLength"),
                "kill_type": event.get("killType"),
                "bounty": event.get("bounty"),
                "shutdown_bounty": event.get("shutdownBounty"),
                "gold_gain": event.get("goldGain"),
                "feat_type": event.get("featType"),
                "feat_value": event.get("featValue"),
                "winning_team": event.get("winningTeam"),
                "actual_start_time": event.get("actualStartTime"),
                "position_x": event.get("position", {}).get("x"),
                "position_y": event.get("position", {}).get("y")
            })

            if event.get("assistingParticipantIds"):
                for pid in event["assistingParticipantIds"]:
                    event_assists_rows.append({
                        "game_id": game_id,
                        "frame_timestamp": frame_ts,
                        "event_timestamp": event.get("timestamp"),
                        "event_type": event.get("type"),
                        "participant_id": pid
                    })

            if event.get("victimDamageDealt"):
                for idx, dmg in enumerate(event["victimDamageDealt"], start=1):
                    event_victim_damage_dealt_rows.append({
                        "game_id": game_id,
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

            if event.get("victimDamageReceived"):
                for idx, dmg in enumerate(event["victimDamageReceived"], start=1):
                    event_victim_damage_received_rows.append({
                        "game_id": game_id,
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

# 기본 테이블 저장
pd.DataFrame(matches_rows).to_csv(output_dir / "matches.csv", index=False)
pd.DataFrame(participants_rows).to_csv(output_dir / "participants.csv", index=False)
pd.DataFrame(frames_rows).to_csv(output_dir / "frames.csv", index=False)
pd.DataFrame(participant_frame_rows).to_csv(output_dir / "participant_frames.csv", index=False)
pd.DataFrame(event_assists_rows).to_csv(output_dir / "event_assists.csv", index=False)
pd.DataFrame(event_victim_damage_dealt_rows).to_csv(output_dir / "event_victim_damage_dealt.csv", index=False)
pd.DataFrame(event_victim_damage_received_rows).to_csv(output_dir / "event_victim_damage_received.csv", index=False)

# ✅ events.csv 저장 후 type별 분할
events_df = pd.DataFrame(events_rows)
events_df.to_csv(output_dir / "events.csv", index=False)

# type_groups = {}
# for event_type, group_df in events_df.groupby("type"):
#     used_cols = tuple(sorted([col for col in group_df.columns if group_df[col].notna().any()]))
#     if used_cols not in type_groups:
#         type_groups[used_cols] = []
#     type_groups[used_cols].append(event_type)

# split_dir = output_dir / "events_split_by_type"
# split_dir.mkdir(exist_ok=True)

# for used_cols, types in type_groups.items():
#     filename = f"events__{'__'.join(types)}.csv"
#     filtered_df = events_df[events_df["type"].isin(types)][list(used_cols)]
#     filtered_df.to_csv(split_dir / filename, index=False)

print(f"\n✅ CSV 파일이 성공적으로 저장되었습니다. 메인 경로: {output_dir.resolve()}")
print(f"🪓 events 테이블은 type별로 {len(type_groups)}개로 분할됨. 폴더: {split_dir.resolve()}")
