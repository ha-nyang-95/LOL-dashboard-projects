

import json
import psycopg2
from psycopg2.extras import execute_values
from pathlib import Path

with open("../single_match_timeline.json", encoding="utf-8") as f:
    match_data = json.load(f)

info = match_data["info"]
frames = info["frames"]
game_id = info["gameId"]

conn = psycopg2.connect(
    host="localhost",
    dbname="riot_match",
    user="ssafyuser",
    password="ssafy",
    port=5432
)
cur = conn.cursor()

match_row = (game_id, info["gameCreation"], info["gameDuration"], info["gameEndTimestamp"], info["gameStartTimestamp"], info["gameVersion"])
cur.execute("""
    INSERT INTO matches (game_id, creation, duration, end_timestamp, start_timestamp, version)
    VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;
""", match_row)

participant_rows = []
for p in info["participants"]:
    participant_rows.append((
        game_id,
        p["participantId"],
        p["puuid"]
    ))
execute_values(cur, """
    INSERT INTO participants (game_id, participant_id, puuid)
    VALUES %s ON CONFLICT DO NOTHING;
""", participant_rows)

frame_rows = []
participant_frame_rows = []
item_purchased_destoryed_sold_rows = []
skill_level_up_rows = []
level_up_rows = []
ward_placed_rows = []
ward_kill_rows = []
champion_kill_rows = []
champion_special_kill_rows = []
elite_monster_kill_rows = []
building_kill_rows = []
turret_plate_destroyed_rows = []
game_end_rows = []
pause_end_rows = []
feat_update_rows = []
champion_transform_rows = []
dragon_soul_given_rows = []

for frame in frames:
    ts = frame["timestamp"]
    frame_rows.append((game_id, ts))
    pf = frame.get("participantFrames", {})
    for pid, pf_data in pf.items():
        row = (game_id, int(pid), ts,
            pf_data.get("currentGold"), pf_data.get("goldPerSecond"), pf_data.get("jungleMinionsKilled"),
            pf_data.get("level"), pf_data.get("minionsKilled"), pf_data.get("timeEnemySpentControlled"),
            pf_data.get("totalGold"), pf_data.get("xp"),
            pf_data.get("position", {}).get("x"), pf_data.get("position", {}).get("y")
        )
        participant_frame_rows.append(row)

    for e in frame.get("events", []):
        t = e.get("type")
        ts = e.get("timestamp")
        pos = e.get("position", {})

        base = (game_id, frame["timestamp"], ts)

        if t == "ITEM_PURCHASED" or t=="ITEM_DESTROYED"or t == "ITEM_SOLD":
            item_purchased_destoryed_sold_rows.append(base + (e["participantId"], e["itemId"],e['type']))
        elif t == "ITEM_UNDO":
            cur.execute("""
                INSERT INTO events__ITEM_UNDO (game_id, frame_timestamp, timestamp, participant_id, before_id, after_id)
                VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;
            """, base + (e["participantId"], e["beforeId"], e["afterId"]))
        elif t == "SKILL_LEVEL_UP":
            skill_level_up_rows.append(base + (e["participantId"], e["skillSlot"], e["levelUpType"]))
        elif t == "LEVEL_UP":
            level_up_rows.append(base + (e["participantId"], e["level"]))
        elif t == "WARD_PLACED":
            ward_placed_rows.append(base + (e["creatorId"], e["wardType"], pos.get("x"), pos.get("y")))
        elif t == "WARD_KILL":
            ward_kill_rows.append(base + (e["killerId"], e["wardType"], pos.get("x"), pos.get("y")))
        elif t == "CHAMPION_KILL":
            champion_kill_rows.append(base + (e.get("killerId"), e.get("victimId"), e.get("killType"), e.get("bounty"), e.get("shutdownBounty"), pos.get("x"), pos.get("y")))
        elif t == "CHAMPION_SPECIAL_KILL":
            champion_special_kill_rows.append(base + (e.get("killType"), e.get("multiKillLength"), pos.get("x"), pos.get("y")))
        elif t == "ELITE_MONSTER_KILL":
            elite_monster_kill_rows.append(base + (e.get("killerId"), e.get("killerTeamId"), e.get("monsterType"), e.get("monsterSubType"), pos.get("x"), pos.get("y")))
        elif t == "BUILDING_KILL":
            building_kill_rows.append(base + (e.get("killerId"), e.get("teamId"), e.get("buildingType"), e.get("towerType"), e.get("laneType"), e.get("bounty"), pos.get("x"), pos.get("y")))
        elif t == "TURRET_PLATE_DESTROYED":
            turret_plate_destroyed_rows.append(base + (e.get("killerId"), e.get("laneType"), e.get("teamId"), pos.get("x"), pos.get("y")))
        elif t == "OBJECTIVE_BOUNTY_PRESTART"or t == "OBJECTIVE_BOUNTY_FINISH" or t == "DRAGON_SOUL_GIVEN":
            dragon_soul_given_rows.append(base + (e.get("teamId"),(e.get("type"))))
        elif t == "GAME_END":
            game_end_rows.append(base + (e.get("winningTeam"),))
        elif t == "PAUSE_END":
            pause_end_rows.append(base + (e.get("realTimestamp"),))
        elif t == "FEAT_UPDATE":
            feat_update_rows.append(base + (e.get("featType"), e.get("featValue")))
        elif t == "CHAMPION_TRANSFORM":
            champion_transform_rows.append(base + (e.get("participantId"),))


execute_values(cur, "INSERT INTO frames VALUES %s ON CONFLICT DO NOTHING", frame_rows)
execute_values(cur, "INSERT INTO participant_frames VALUES %s ON CONFLICT DO NOTHING", participant_frame_rows)
execute_values(cur, "INSERT INTO events__ITEM_DESTROYED_PURCHASED_SOLD VALUES %s ON CONFLICT DO NOTHING", item_purchased_destoryed_sold_rows)
execute_values(cur, "INSERT INTO events__SKILL_LEVEL_UP VALUES %s ON CONFLICT DO NOTHING", skill_level_up_rows)
execute_values(cur, "INSERT INTO events__LEVEL_UP VALUES %s ON CONFLICT DO NOTHING", level_up_rows)
execute_values(cur, "INSERT INTO events__WARD_PLACED VALUES %s ON CONFLICT DO NOTHING", ward_placed_rows)
execute_values(cur, "INSERT INTO events__WARD_KILL VALUES %s ON CONFLICT DO NOTHING", ward_kill_rows)
execute_values(cur, "INSERT INTO events__CHAMPION_KILL VALUES %s ON CONFLICT DO NOTHING", champion_kill_rows)
execute_values(cur, "INSERT INTO events__CHAMPION_SPECIAL_KILL VALUES %s ON CONFLICT DO NOTHING", champion_special_kill_rows)
execute_values(cur, "INSERT INTO events__ELITE_MONSTER_KILL VALUES %s ON CONFLICT DO NOTHING", elite_monster_kill_rows)
execute_values(cur, "INSERT INTO events__BUILDING_KILL VALUES %s ON CONFLICT DO NOTHING", building_kill_rows)
execute_values(cur, "INSERT INTO events__TURRET_PLATE_DESTROYED VALUES %s ON CONFLICT DO NOTHING", turret_plate_destroyed_rows)
execute_values(cur, "INSERT INTO events__GAME_END VALUES %s ON CONFLICT DO NOTHING", game_end_rows)
execute_values(cur, "INSERT INTO events__PAUSE_END VALUES %s ON CONFLICT DO NOTHING", pause_end_rows)
execute_values(cur, "INSERT INTO events__FEAT_UPDATE VALUES %s ON CONFLICT DO NOTHING", feat_update_rows)
execute_values(cur, "INSERT INTO events__CHAMPION_TRANSFORM VALUES %s ON CONFLICT DO NOTHING", champion_transform_rows)
execute_values(cur, "INSERT INTO events__DRAGON_SOUL_GIVEN VALUES %s ON CONFLICT DO NOTHING", dragon_soul_given_rows)

conn.commit()
cur.close()
conn.close()
print("✅ 모든 데이터가 성공적으로 적재되었습니다.")
