-- matches 테이블
CREATE TABLE matches (
    match_id VARCHAR PRIMARY KEY,
    game_id BIGINT,
    data_version VARCHAR,
    end_of_game_result VARCHAR,
    frame_interval BIGINT
);

-- participants 테이블
CREATE TABLE participants (
    id SERIAL PRIMARY KEY,
    game_id BIGINT,
    participant_id INT,
    puuid VARCHAR
);

-- frames 테이블
CREATE TABLE frames (
    id SERIAL PRIMARY KEY,
    game_id BIGINT,
    timestamp BIGINT
);

-- participant_frames 테이블
CREATE TABLE participant_frames (
    id SERIAL PRIMARY KEY,
    game_id BIGINT,
    participant_id INT,
    frame_timestamp BIGINT,
    current_gold INT,
    gold_per_second INT,
    jungle_minions_killed INT,
    level INT,
    minions_killed INT,
    time_enemy_spent_controlled INT,
    total_gold INT,
    xp INT,
    position_x INT,
    position_y INT,
    ability_haste INT,
    ability_power INT,
    armor INT,
    armor_pen INT,
    armor_pen_percent INT,
    attack_damage INT,
    attack_speed INT,
    bonus_armor_pen_percent INT,
    bonus_magic_pen_percent INT,
    cc_reduction INT,
    cooldown_reduction INT,
    health INT,
    health_max INT,
    health_regen INT,
    lifesteal INT,
    magic_pen INT,
    magic_pen_percent INT,
    magic_resist INT,
    movement_speed INT,
    omnivamp INT,
    physical_vamp INT,
    power INT,
    power_max INT,
    power_regen INT,
    spell_vamp INT,
    magic_damage_done INT,
    magic_damage_done_to_champions INT,
    magic_damage_taken INT,
    physical_damage_done INT,
    physical_damage_done_to_champions INT,
    physical_damage_taken INT,
    total_damage_done INT,
    total_damage_done_to_champions INT,
    total_damage_taken INT,
    true_damage_done INT,
    true_damage_done_to_champions INT,
    true_damage_taken INT
);

-- events 테이블
CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    game_id BIGINT,
    frame_timestamp BIGINT,
    timestamp BIGINT,
    real_timestamp BIGINT,
    type VARCHAR,
    participant_id INT,
    killer_id INT,
    victim_id INT,
    creator_id INT,
    killer_team_id INT,
    team_id INT,
    item_id INT,
    before_id INT,
    after_id INT,
    skill_slot INT,
    level_up_type VARCHAR,
    level INT,
    ward_type VARCHAR,
    building_type VARCHAR,
    tower_type VARCHAR,
    lane_type VARCHAR,
    monster_type VARCHAR,
    monster_sub_type VARCHAR,
    kill_streak_length INT,
    multi_kill_length INT,
    kill_type VARCHAR,
    bounty INT,
    shutdown_bounty INT,
    gold_gain INT,
    feat_type VARCHAR,
    feat_value INT,
    winning_team INT,
    actual_start_time BIGINT,
    position_x INT,
    position_y INT
);

-- event_assists 테이블
CREATE TABLE event_assists (
    id SERIAL PRIMARY KEY,
    game_id BIGINT,
    frame_timestamp BIGINT,
    event_timestamp BIGINT,
    event_type VARCHAR,
    participant_id INT
);

-- event_victim_damage_dealt 테이블
CREATE TABLE event_victim_damage_dealt (
    id SERIAL PRIMARY KEY,
    game_id BIGINT,
    frame_timestamp BIGINT,
    event_timestamp BIGINT,
    instance INT,
    basic BOOLEAN,
    magic_damage INT,
    physical_damage INT,
    true_damage INT,
    name VARCHAR,
    participant_id INT,
    spell_name VARCHAR,
    spell_slot INT,
    type VARCHAR
);

-- event_victim_damage_received 테이블
CREATE TABLE event_victim_damage_received (
    id SERIAL PRIMARY KEY,
    game_id BIGINT,
    frame_timestamp BIGINT,
    event_timestamp BIGINT,
    instance INT,
    basic BOOLEAN,
    magic_damage INT,
    physical_damage INT,
    true_damage INT,
    name VARCHAR,
    participant_id INT,
    spell_name VARCHAR,
    spell_slot INT,
    type VARCHAR
);