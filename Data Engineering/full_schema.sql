/*───────────────────────────────
   0. 정리
───────────────────────────────*/
DROP TABLE IF EXISTS events CASCADE;
DROP TABLE IF EXISTS event_victim_damage_received   CASCADE;
DROP TABLE IF EXISTS event_victim_damage_dealt      CASCADE;
DROP TABLE IF EXISTS event_assists                  CASCADE;
DROP TABLE IF EXISTS events__ITEM_DESTROYED_PURCHASED_SOLD CASCADE;
DROP TABLE IF EXISTS events_champion_kill           CASCADE;
DROP TABLE IF EXISTS events_elite_monster_kill      CASCADE;
DROP TABLE IF EXISTS events_building_kill           CASCADE;
DROP TABLE IF EXISTS events_turret_plate_destroyed  CASCADE;
DROP TABLE IF EXISTS events_ward_placed             CASCADE;
DROP TABLE IF EXISTS events_ward_kill               CASCADE;
DROP TABLE IF EXISTS events_item_destroyed          CASCADE;
DROP TABLE IF EXISTS events_item_undo               CASCADE;
DROP TABLE IF EXISTS events_skill_level_up          CASCADE;
DROP TABLE IF EXISTS events_level_up                CASCADE;

DROP TABLE IF EXISTS events_game_end                CASCADE;
DROP TABLE IF EXISTS events_champion_special_kill   CASCADE;

DROP TABLE IF EXISTS participant_frames CASCADE;
DROP TABLE IF EXISTS frames             CASCADE;
DROP TABLE IF EXISTS participants        CASCADE;
DROP TABLE IF EXISTS matches             CASCADE;

/*───────────────────────────────
   1. matches
───────────────────────────────*/
CREATE TABLE matches (
    game_id            BIGINT  PRIMARY KEY,
    match_id           TEXT    UNIQUE,
    data_version       INTEGER,
    end_of_game_result TEXT,
    frame_interval     INTEGER
);

/*───────────────────────────────
   2. participants
───────────────────────────────*/
CREATE TABLE participants (
    game_id        BIGINT,
    participant_id SMALLINT,
    puuid          TEXT,
    PRIMARY KEY (game_id, participant_id),
    FOREIGN KEY (game_id) REFERENCES matches (game_id) ON DELETE CASCADE
);

/*───────────────────────────────
   3. frames
───────────────────────────────*/
CREATE TABLE frames (
    game_id   BIGINT,
    timestamp BIGINT,
    PRIMARY KEY (game_id, timestamp),
    FOREIGN KEY (game_id) REFERENCES matches (game_id) ON DELETE CASCADE
);

/*───────────────────────────────
   4. participant_frames
───────────────────────────────*/
CREATE TABLE participant_frames (
    game_id      BIGINT,
    participant_id SMALLINT,
    frame_timestamp BIGINT,

    /* ↓ last_test.py 에서 생성한 컬럼들 :contentReference[oaicite:0]{index=0}&#8203;:contentReference[oaicite:1]{index=1} */
    current_gold               INTEGER,
    gold_per_second            INTEGER,
    jungle_minions_killed      INTEGER,
    level                      SMALLINT,
    minions_killed             INTEGER,
    time_enemy_spent_controlled INTEGER,
    total_gold                 INTEGER,
    xp                         INTEGER,
    position_x                 INTEGER,
    position_y                 INTEGER,

    abilityhaste               SMALLINT,
    abilitypower               SMALLINT,
    armor                      SMALLINT,
    armorpen                   SMALLINT,
    armorpenpercent            NUMERIC,
    attackdamage               SMALLINT,
    attackspeed                NUMERIC,
    bonusarmorpenpercent       NUMERIC,
    bonusmagicpenpercent       NUMERIC,
    ccreduction                NUMERIC,
    cooldownreduction          NUMERIC,
    health                     INTEGER,
    healthmax                  INTEGER,
    healthregen                NUMERIC,
    lifesteal                  NUMERIC,
    magicpen                   NUMERIC,
    magicpenpercent            NUMERIC,
    magicresist                SMALLINT,
    movementspeed              NUMERIC,
    omnivamp                   NUMERIC,
    physicalvamp               NUMERIC,
    power                      INTEGER,
    powermax                   INTEGER,
    powerregen                 NUMERIC,
    spellvamp                  NUMERIC,

    magicDamageDone                BIGINT,
    magicDamageDoneToChampions     BIGINT,
    magicDamageTaken               BIGINT,
    physicalDamageDone             BIGINT,
    physicalDamageDoneToChampions  BIGINT,
    physicalDamageTaken            BIGINT,
    totalDamageDone                BIGINT,
    totalDamageDoneToChampions     BIGINT,
    totalDamageTaken               BIGINT,
    trueDamageDone                 BIGINT,
    trueDamageDoneToChampions      BIGINT,
    trueDamageTaken                BIGINT,

    PRIMARY KEY (game_id, participant_id, frame_timestamp),
    FOREIGN KEY (game_id, frame_timestamp)
        REFERENCES frames (game_id, timestamp) ON DELETE CASCADE,
    FOREIGN KEY (game_id, participant_id)
        REFERENCES participants (game_id, participant_id) ON DELETE CASCADE
);

/*───────────────────────────────
   6. 이벤트‑종류별 테이블
   (각 PK = game_id + frame_ts + event_ts)
───────────────────────────────*/



CREATE TABLE events__CHAMPION_KILL (
    game_id         BIGINT,
    timestamp       BIGINT,
    frame_timestamp BIGINT,
    killer_id       SMALLINT,
    victim_id       SMALLINT,
    kill_type       VARCHAR(20),
    bounty          INTEGER,
    shutdown_bounty INTEGER,
    position_x      INTEGER,
    position_y      INTEGER,
    PRIMARY KEY (game_id, timestamp),
    FOREIGN KEY (game_id, frame_timestamp) REFERENCES frames (game_id, timestamp),
    FOREIGN KEY (game_id, killer_id) REFERENCES participants (game_id, participant_id) ON DELETE SET NULL,
    FOREIGN KEY (game_id, victim_id) REFERENCES participants (game_id, participant_id) ON DELETE SET NULL
);

CREATE TABLE events__WARD_PLACED (
    game_id         BIGINT,
    timestamp       BIGINT,
    frame_timestamp BIGINT,
    creator_id      SMALLINT,
    ward_type       TEXT,
    position_x      INTEGER,
    position_y      INTEGER,
    PRIMARY KEY (game_id, timestamp),
    FOREIGN KEY (game_id, frame_timestamp) REFERENCES frames (game_id, timestamp),
    FOREIGN KEY (game_id, creator_id) REFERENCES participants (game_id, participant_id)
);

CREATE TABLE events__WARD_KILL (
    game_id         BIGINT,
    timestamp       BIGINT,
    frame_timestamp BIGINT,
    killer_id       SMALLINT,
    ward_type       TEXT,
    position_x      INTEGER,
    position_y      INTEGER,
    PRIMARY KEY (game_id, timestamp),
    FOREIGN KEY (game_id, frame_timestamp) REFERENCES frames (game_id, timestamp),
    FOREIGN KEY (game_id, killer_id) REFERENCES participants (game_id, participant_id)
);

CREATE TABLE events__ITEM_DESTROYED_PURCHASED_SOLD (
    game_id         BIGINT,
    timestamp       BIGINT,
    frame_timestamp BIGINT,
    participant_id  SMALLINT,
    item_id         INTEGER,
    event_type      VARCHAR(20),
    PRIMARY KEY (game_id, timestamp),
    FOREIGN KEY (game_id, frame_timestamp) REFERENCES frames (game_id, timestamp),
    FOREIGN KEY (game_id, participant_id) REFERENCES participants (game_id, participant_id)
);

CREATE TABLE events__ITEM_UNDO (
    game_id         BIGINT,
    timestamp       BIGINT,
    frame_timestamp BIGINT,
    participant_id  SMALLINT,
    before_id       INTEGER,
    after_id        INTEGER,
    PRIMARY KEY (game_id, timestamp),
    FOREIGN KEY (game_id, frame_timestamp) REFERENCES frames (game_id, timestamp),
    FOREIGN KEY (game_id, participant_id) REFERENCES participants (game_id, participant_id)
);

CREATE TABLE events__SKILL_LEVEL_UP (
    game_id         BIGINT,
    timestamp       BIGINT,
    frame_timestamp BIGINT,
    participant_id  SMALLINT,
    skill_slot      SMALLINT,
    level_up_type   VARCHAR(50),
    PRIMARY KEY (game_id, timestamp),
    FOREIGN KEY (game_id, frame_timestamp) REFERENCES frames (game_id, timestamp),
    FOREIGN KEY (game_id, participant_id) REFERENCES participants (game_id, participant_id)
);

CREATE TABLE events__LEVEL_UP (
    game_id         BIGINT,
    timestamp       BIGINT,
    frame_timestamp BIGINT,
    participant_id  SMALLINT,
    level           SMALLINT,
    PRIMARY KEY (game_id, timestamp),
    FOREIGN KEY (game_id, frame_timestamp) REFERENCES frames (game_id, timestamp),
    FOREIGN KEY (game_id, participant_id) REFERENCES participants (game_id, participant_id)
);

CREATE TABLE events__TURRET_PLATE_DESTROYED (
    game_id         BIGINT,
    timestamp       BIGINT,
    frame_timestamp BIGINT,
    killer_id       SMALLINT,
    lane_type       VARCHAR(20),
    team_id         SMALLINT,
    position_x      INTEGER,
    position_y      INTEGER,
    PRIMARY KEY (game_id, timestamp),
    FOREIGN KEY (game_id, frame_timestamp) REFERENCES frames (game_id, timestamp),
    FOREIGN KEY (game_id, killer_id) REFERENCES participants (game_id, participant_id)
);

CREATE TABLE events__BUILDING_KILL (
    game_id         BIGINT,
    timestamp       BIGINT,
    frame_timestamp BIGINT,
    killer_id       SMALLINT,
    team_id         SMALLINT,
    building_type   VARCHAR(50),
    tower_type      VARCHAR(20),
    lane_type       VARCHAR(20),
    bounty          INTEGER,
    position_x      INTEGER,
    position_y      INTEGER,
    PRIMARY KEY (game_id, timestamp),
    FOREIGN KEY (game_id, frame_timestamp) REFERENCES frames (game_id, timestamp),
    FOREIGN KEY (game_id, killer_id) REFERENCES participants (game_id, participant_id)
);

CREATE TABLE events__CHAMPION_SPECIAL_KILL (
    game_id         BIGINT,
    timestamp       BIGINT,
    frame_timestamp BIGINT,
    kill_type       VARCHAR(20),
    multi_kill_length SMALLINT,
    position_x      INTEGER,
    position_y      INTEGER,
    PRIMARY KEY (game_id, timestamp),
    FOREIGN KEY (game_id, frame_timestamp) REFERENCES frames (game_id, timestamp)
);

CREATE TABLE events__CHAMPION_TRANSFORM (
    game_id         BIGINT,
    timestamp       BIGINT,
    frame_timestamp BIGINT,
    participant_id  SMALLINT,
    PRIMARY KEY (game_id, timestamp),
    FOREIGN KEY (game_id, frame_timestamp) REFERENCES frames (game_id, timestamp),
    FOREIGN KEY (game_id, participant_id) REFERENCES participants (game_id, participant_id)
);

CREATE TABLE events__DRAGON_SOUL_GIVEN (
    game_id         BIGINT,
    timestamp       BIGINT,
    frame_timestamp BIGINT,
    team_id         SMALLINT,
    type		VARCHAR(50),
    PRIMARY KEY (game_id, timestamp),
    FOREIGN KEY (game_id, frame_timestamp) REFERENCES frames (game_id, timestamp)
);


CREATE TABLE events__ELITE_MONSTER_KILL (
    game_id         BIGINT,
    timestamp       BIGINT,
    frame_timestamp BIGINT,
    killer_id       SMALLINT,
    killer_team_id  SMALLINT,
    monster_type    VARCHAR(20),
    monster_sub_type VARCHAR(30),
    position_x      INTEGER,
    position_y      INTEGER,
    PRIMARY KEY (game_id, timestamp),
    FOREIGN KEY (game_id, frame_timestamp) REFERENCES frames (game_id, timestamp),
    FOREIGN KEY (game_id, killer_id) REFERENCES participants (game_id, participant_id)
);

CREATE TABLE events__GAME_END (
    game_id         BIGINT,
    timestamp       BIGINT,
    frame_timestamp BIGINT,
    winning_team    SMALLINT,
    PRIMARY KEY (game_id, timestamp),
    FOREIGN KEY (game_id, frame_timestamp) REFERENCES frames (game_id, timestamp)
);

CREATE TABLE events__PAUSE_END (
    game_id         BIGINT,
    timestamp       BIGINT,
    frame_timestamp BIGINT,
    actual_start_time BIGINT,
    PRIMARY KEY (game_id, timestamp),
    FOREIGN KEY (game_id, frame_timestamp) REFERENCES frames (game_id, timestamp)
);

CREATE TABLE events__FEAT_UPDATE (
    game_id         BIGINT,
    timestamp       BIGINT,
    frame_timestamp BIGINT,
    feat_type       SMALLINT,
    feat_value      INTEGER,
    PRIMARY KEY (game_id, timestamp),
    FOREIGN KEY (game_id, frame_timestamp) REFERENCES frames (game_id, timestamp)
);


/*───────────────────────────────
   7. event_assists
   ‑ 챔피언 킬만 대상
───────────────────────────────*/
CREATE TABLE event_assists (
    game_id            BIGINT,
    frame_timestamp    BIGINT,
    event_timestamp    BIGINT,
    participant_id     SMALLINT,
    PRIMARY KEY (game_id, frame_timestamp, event_timestamp, participant_id),
    FOREIGN KEY (game_id, frame_timestamp, event_timestamp)
        REFERENCES events_champion_kill (game_id, frame_timestamp, timestamp)
        ON DELETE CASCADE
);

/*───────────────────────────────
   8. victim_damage_*  (챔피언 킬 전용)
───────────────────────────────*/
CREATE TABLE event_victim_damage_dealt (
    game_id            BIGINT,
    frame_timestamp    BIGINT,
    event_timestamp    BIGINT,
    instance           SMALLINT,

    basic              BOOLEAN,
    magic_damage       INTEGER,
    physical_damage    INTEGER,
    true_damage        INTEGER,
    name               TEXT,
    participant_id     SMALLINT,
    spell_name         TEXT,
    spell_slot         SMALLINT,
    type               VARCHAR(30),

    PRIMARY KEY (game_id, frame_timestamp, event_timestamp, instance),
    FOREIGN KEY (game_id, frame_timestamp, event_timestamp)
        REFERENCES events_champion_kill (game_id, frame_timestamp, timestamp)
        ON DELETE CASCADE
);

CREATE TABLE event_victim_damage_received (
    game_id            BIGINT,
    frame_timestamp    BIGINT,
    event_timestamp    BIGINT,
    instance           SMALLINT,

    basic              BOOLEAN,
    magic_damage       INTEGER,
    physical_damage    INTEGER,
    true_damage        INTEGER,
    name               TEXT,
    participant_id     SMALLINT,
    spell_name         TEXT,
    spell_slot         SMALLINT,
    type               VARCHAR(30),

    PRIMARY KEY (game_id, frame_timestamp, event_timestamp, instance),
    FOREIGN KEY (game_id, frame_timestamp, event_timestamp)
        REFERENCES events_champion_kill (game_id, frame_timestamp, timestamp)
        ON DELETE CASCADE
);
