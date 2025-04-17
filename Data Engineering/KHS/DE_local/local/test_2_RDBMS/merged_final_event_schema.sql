
-- 1. matches 테이블
CREATE TABLE matches (
    game_id BIGINT PRIMARY KEY,
    match_id TEXT,
    data_version TEXT,
    end_of_game_result TEXT,
    frame_interval INT
);

-- 2. participants 테이블
CREATE TABLE participants (
    game_id BIGINT REFERENCES matches(game_id),
    participant_id INT,
    puuid TEXT,
    PRIMARY KEY(game_id, participant_id)
);

-- 3. frames 테이블
CREATE TABLE frames (
    game_id BIGINT REFERENCES matches(game_id),
    timestamp INT,
    PRIMARY KEY(game_id, timestamp)
);

-- 4. participant_frames 테이블
CREATE TABLE participant_frames (
    game_id BIGINT REFERENCES matches(game_id),
    participant_id INT,
    frame_timestamp INT,
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
    true_damage_taken INT,
    PRIMARY KEY(game_id, participant_id, frame_timestamp),
    FOREIGN KEY(game_id, frame_timestamp) REFERENCES frames(game_id, timestamp),
    FOREIGN KEY(game_id, participant_id) REFERENCES participants(game_id, participant_id)
);

-- 5. event_assists 테이블
CREATE TABLE event_assists (
    game_id BIGINT REFERENCES matches(game_id),
    frame_timestamp INT,
    event_timestamp INT,
    event_type TEXT,
    participant_id INT,
    PRIMARY KEY(game_id, event_timestamp, participant_id)
);

-- 6. event_victim_damage_dealt 테이블
CREATE TABLE event_victim_damage_dealt (
    game_id BIGINT REFERENCES matches(game_id),
    frame_timestamp INT,
    event_timestamp INT,
    instance SMALLINT,
    basic BOOLEAN,
    magic_damage INT,
    physical_damage INT,
    true_damage INT,
    name TEXT,
    participant_id INT,
    spell_name TEXT,
    spell_slot INT,
    type TEXT,
    PRIMARY KEY(game_id, event_timestamp, instance)
);

-- 7. event_victim_damage_received 테이블
CREATE TABLE event_victim_damage_received (
    game_id BIGINT REFERENCES matches(game_id),
    frame_timestamp INT,
    event_timestamp INT,
    instance SMALLINT,
    basic BOOLEAN,
    magic_damage INT,
    physical_damage INT,
    true_damage INT,
    name TEXT,
    participant_id INT,
    spell_name TEXT,
    spell_slot INT,
    type TEXT,
    PRIMARY KEY(game_id, event_timestamp, instance)
);





CREATE TABLE events_champion_kill (
	event_id SERIAL PRIMARY KEY,
	game_id BIGINT REFERENCES matches(game_id),
	frame_timestamp INT REFERENCES frames(timestamp),
	timestamp INT,
	real_timestamp BIGINT,
	type TEXT,
	killer_id INT,
	victim_id INT,
	kill_streak_length INT,
	multi_kill_length INT,
	kill_type TEXT,
	position_x INT,
	position_y INT
);
    


CREATE TABLE events_building_kill (
	event_id SERIAL PRIMARY KEY,
	game_id BIGINT REFERENCES matches(game_id),
	frame_timestamp INT REFERENCES frames(timestamp),
	timestamp INT,
	real_timestamp BIGINT,
	type TEXT,
	killer_id INT,
	team_id INT,
	building_type TEXT,
	tower_type TEXT,
	lane_type TEXT,
	position_x INT,
	position_y INT
);
    


CREATE TABLE events_ward_placed (
	event_id SERIAL PRIMARY KEY,
	game_id BIGINT REFERENCES matches(game_id),
	frame_timestamp INT REFERENCES frames(timestamp),
	timestamp INT,
	real_timestamp BIGINT,
	type TEXT,
	creator_id INT,
	ward_type TEXT,
	position_x INT,
	position_y INT
);
    


CREATE TABLE events_ward_kill (
	event_id SERIAL PRIMARY KEY,
	game_id BIGINT REFERENCES matches(game_id),
	frame_timestamp INT REFERENCES frames(timestamp),
	timestamp INT,
	real_timestamp BIGINT,
	type TEXT,
	killer_id INT,
	ward_type TEXT,
	position_x INT,
	position_y INT
);
    


CREATE TABLE events_elite_monster_kill (
	event_id SERIAL PRIMARY KEY,
	game_id BIGINT REFERENCES matches(game_id),
	frame_timestamp INT REFERENCES frames(timestamp),
	timestamp INT,
	real_timestamp BIGINT,
	type TEXT,
	killer_id INT,
	killer_team_id INT,
	monster_type TEXT,
	monster_sub_type TEXT,
	position_x INT,
	position_y INT
);



CREATE TABLE events_item_event (
	event_id SERIAL PRIMARY KEY,
	game_id BIGINT REFERENCES matches(game_id),
	frame_timestamp INT REFERENCES frames(timestamp),
	timestamp INT,
	real_timestamp BIGINT,
	type TEXT,
	participant_id INT,
	item_id INT,
	before_id INT,
	after_id INT
);



CREATE TABLE events_level_up (
	event_id SERIAL PRIMARY KEY,
	game_id BIGINT REFERENCES matches(game_id),
	frame_timestamp INT REFERENCES frames(timestamp),
	timestamp INT,
	real_timestamp BIGINT,
	type TEXT,
	participant_id INT,
	level INT,
	level_up_type TEXT
);



CREATE TABLE events_skill_level_up (
	event_id SERIAL PRIMARY KEY,
	game_id BIGINT REFERENCES matches(game_id),
	frame_timestamp INT REFERENCES frames(timestamp),
	timestamp INT,
	real_timestamp BIGINT,
	type TEXT,
	participant_id INT,
	skill_slot INT,
	level_up_type TEXT
);



CREATE TABLE events_bounty_kill (
	event_id SERIAL PRIMARY KEY,
	game_id BIGINT REFERENCES matches(game_id),
	frame_timestamp INT REFERENCES frames(timestamp),
	timestamp INT,
	real_timestamp BIGINT,
	type TEXT,
	killer_id INT,
	victim_id INT,
	shutdown_bounty INT,
	bounty INT,
	gold_gain INT
);



CREATE TABLE events_game_end (
	event_id SERIAL PRIMARY KEY,
	game_id BIGINT REFERENCES matches(game_id),
	frame_timestamp INT REFERENCES frames(timestamp),
	timestamp INT,
	real_timestamp BIGINT,
	type TEXT,
	winning_team INT
);
