# 롤 데이터 칼럼

### 🔹 `event_assist`

| 영어 칼럼명      | 한글 설명                   |
| ---------------- | --------------------------- |
| game\_id         | 게임 고유 ID                |
| frame\_timestamp | 프레임 기준 타임스탬프      |
| event\_timestamp | 이벤트 발생 시간            |
| event\_type      | 이벤트 종류 (예: 어시스트)  |
| participant\_id  | 이벤트에 해당하는 참가자 ID |


### 🔹 `event_victim_damage_dealt`

| 영어 칼럼명      | 한글 설명                     |
| ---------------- | ----------------------------- |
| game\_id         | 게임 고유 ID                  |
| frame\_timestamp | 프레임 기준 타임스탬프        |
| event\_timestamp | 이벤트 발생 시간              |
| instance         | 피해 인스턴스 번호            |
| basic            | 기본 공격으로 준 피해량       |
| magic\_damage    | 마법 피해량                   |
| physical\_damage | 물리 피해량                   |
| true\_damage     | 고정 피해량                   |
| name             | 스킬 혹은 기본 공격 이름      |
| participant\_id  | 피해를 가한 참가자 ID         |
| spell\_name      | 사용한 스킬 이름              |
| spell\_slot      | 스킬 슬롯 (Q, W, E, R 등)     |
| type             | 피해 타입 (스킬, 기본공격 등) |


### 🔹 `event_victim_damage_received`

> 위와 동일한 구조, 단 **피해를 받은 사람** 기준 
   
| 영어 칼럼명      | 한글 설명                  |
| ---------------- | -------------------------- |
| game\_id         | 게임 고유 ID               |
| frame\_timestamp | 프레임 기준 타임스탬프     |
| event\_timestamp | 이벤트 발생 시간           |
| instance         | 피해 인스턴스 번호         |
| basic            | 기본 공격으로 받은 피해량  |
| magic\_damage    | 마법 피해량                |
| physical\_damage | 물리 피해량                |
| true\_damage     | 고정 피해량                |
| name             | 가해자 스킬 혹은 공격 이름 |
| participant\_id  | 피해를 받은 참가자 ID      |
| spell\_name      | 사용된 스킬 이름           |
| spell\_slot      | 스킬 슬롯 (Q, W, E, R 등)  |
| type             | 피해 타입                  |


### 🔹 `events_BUILDING_KILL`

| 영어 칼럼명      | 한글 설명                   |
| ---------------- | --------------------------- |
| bounty           | 건물 파괴로 얻은 현상금     |
| building\_type   | 건물 종류 (타워, 억제기 등) |
| frame\_timestamp | 프레임 기준 타임스탬프      |
| game\_id         | 게임 고유 ID                |
| killer\_id       | 건물을 파괴한 참가자 ID     |
| lane\_type       | 라인 종류 (탑, 미드, 봇 등) |
| position\_x      | x 좌표 위치                 |
| position\_y      | y 좌표 위치                 |
| team\_id         | 팀 ID                       |
| timestamp        | 실제 발생 시간              |
| tower\_type      | 타워의 세부 유형            |
| type             | 이벤트 타입                 |


### 🔹 `events__CHAMPION_KILL`

| 영어 칼럼명          | 한글 설명              |
| -------------------- | ---------------------- |
| bounty               | 처치 시 현상금         |
| frame\_timestamp     | 프레임 기준 타임스탬프 |
| game\_id             | 게임 고유 ID           |
| kill\_streak\_length | 연속 킬 수             |
| killer\_id           | 킬한 참가자 ID         |
| position\_x          | x 좌표 위치            |
| position\_y          | y 좌표 위치            |
| shutdown\_bounty     | 셧다운 보너스 현상금   |
| timestamp            | 실제 발생 시간         |
| type                 | 이벤트 타입            |
| victim\_id           | 죽은 참가자 ID         |


### 🔹 `events__CHAMPION_SPECIAL_KILL`

| 영어 칼럼명         | 한글 설명                              |
| ------------------- | -------------------------------------- |
| frame\_timestamp    | 프레임 기준 타임스탬프                 |
| game\_id            | 게임 고유 ID                           |
| kill\_type          | 특수 킬 유형 (예: 펜타킬, 트리플킬 등) |
| killer\_id          | 킬을 한 참가자 ID                      |
| multi\_kill\_length | 멀티킬 수 (2: 더블, 3: 트리플 등)      |
| position\_x         | x 좌표 위치                            |
| position\_y         | y 좌표 위치                            |
| timestamp           | 실제 발생 시간                         |
| type                | 이벤트 타입                            |


### 🔹 `events__CHAMPION_TRANSFORM`

| 영어 칼럼명      | 한글 설명               |
| ---------------- | ----------------------- |
| frame\_timestamp | 프레임 기준 타임스탬프  |
| game\_id         | 게임 고유 ID            |
| participant\_id  | 변신한 챔피언 참가자 ID |
| timestamp        | 실제 발생 시간          |
| type             | 이벤트 타입             |


### 🔹 `events_GAME_END`

> **중복된 events\_\_GAME\_END 도 존재하므로 구분 필요**  
> 이 버전은 챔피언 킬 정보 포함

| 영어 칼럼명          | 한글 설명                |
| -------------------- | ------------------------ |
| bounty               | 마지막 처치 보상         |
| frame\_timestamp     | 프레임 기준 타임스탬프   |
| game\_id             | 게임 고유 ID             |
| kill\_streak\_length | 킬 연속 기록             |
| killer\_id           | 마지막 킬을 한 참가자 ID |
| position\_x          | x 좌표 위치              |
| position\_y          | y 좌표 위치              |
| shutdown\_bounty     | 셧다운 보상              |
| timestamp            | 실제 발생 시간           |
| type                 | 이벤트 타입              |
| victim\_id           | 죽은 참가자 ID           |


### 🔹 `events__DRAGON_SOUL_GIVEN__OBJECTIVE_BOUNTY_FINISH`

| 영어 칼럼명      | 한글 설명                 |
| ---------------- | ------------------------- |
| frame\_timestamp | 프레임 기준 타임스탬프    |
| game\_id         | 게임 고유 ID              |
| team\_id         | 영혼/목표 보상 받은 팀 ID |
| timestamp        | 실제 발생 시간            |
| type             | 이벤트 타입               |


### 🔹 `events__ELITE_MONSTER_KILL`

| 영어 칼럼명        | 한글 설명                          |
| ------------------ | ---------------------------------- |
| bounty             | 몬스터 처치로 얻은 현상금          |
| frame\_timestamp   | 프레임 기준 타임스탬프             |
| game\_id           | 게임 고유 ID                       |
| killer\_id         | 몬스터 처치한 참가자 ID            |
| killer\_team\_id   | 처치한 팀 ID                       |
| monster\_sub\_type | 몬스터 세부 유형 (예: 대지 드래곤) |
| monster\_type      | 몬스터 종류 (드래곤, 바론 등)      |
| position\_x        | x 좌표 위치                        |
| position\_y        | y 좌표 위치                        |
| timestamp          | 실제 발생 시간                     |
| type               | 이벤트 타입                        |


### 🔹 `events__FEAT_UPDATE`

| 영어 칼럼명      | 한글 설명                    |
| ---------------- | ---------------------------- |
| feat\_type       | 달성한 도전 과제 유형        |
| feat\_value      | 도전 과제 수치 (예: 킬 수)   |
| frame\_timestamp | 프레임 기준 타임스탬프       |
| game\_id         | 게임 고유 ID                 |
| team\_id         | 해당 도전과제를 달성한 팀 ID |
| timestamp        | 실제 발생 시간               |
| type             | 이벤트 타입                  |


### 🔹 `events__GAME_END`

> **진짜 게임 종료 이벤트 (다른 `GAME_END`와는 다름)**  

| 영어 칼럼명      | 한글 설명                     |
| ---------------- | ----------------------------- |
| frame\_timestamp | 프레임 기준 타임스탬프        |
| game\_id         | 게임 고유 ID                  |
| real\_timestamp  | 실제 현실 시간 (Unix Time 등) |
| timestamp        | 게임 내 시간                  |
| type             | 이벤트 타입                   |
| winning\_team    | 승리한 팀의 ID                |


### 🔹 `events__ITEM_DESTROYED__ITEM_PURCHASED__ITEM_SOLD`

| 영어 칼럼명      | 한글 설명                       |
| ---------------- | ------------------------------- |
| frame\_timestamp | 프레임 기준 타임스탬프          |
| game\_id         | 게임 고유 ID                    |
| item\_id         | 아이템 고유 ID                  |
| participant\_id  | 아이템 관련 행동을 한 참가자 ID |
| timestamp        | 실제 발생 시간                  |
| type             | 이벤트 타입 (구매/판매/파괴 등) |


### 🔹 `events__ITEM_UNDO`

| 영어 칼럼명      | 한글 설명                        |
| ---------------- | -------------------------------- |
| after\_id        | 되돌린 후의 아이템 ID            |
| before\_id       | 되돌리기 전의 아이템 ID          |
| frame\_timestamp | 프레임 기준 타임스탬프           |
| game\_id         | 게임 고유 ID                     |
| gold\_gain       | 되돌리기로 회수한 골드           |
| participant\_id  | 행동한 참가자 ID                 |
| timestamp        | 실제 발생 시간                   |
| type             | 이벤트 타입 (아이템 되돌리기 등) |


### 🔹 `events__LEVEL_UP`

| 영어 칼럼명      | 한글 설명               |
| ---------------- | ----------------------- |
| frame\_timestamp | 프레임 기준 타임스탬프  |
| game\_id         | 게임 고유 ID            |
| level            | 레벨 업 후의 레벨       |
| participant\_id  | 레벨업한 참가자 ID      |
| timestamp        | 실제 발생 시간          |
| type             | 이벤트 타입 (레벨업 등) |


### 🔹 `events__OBJECTIVE_BOUNTY_PRESTART`

| 영어 칼럼명         | 한글 설명              |
| ------------------- | ---------------------- |
| actual\_start\_time | 실제 시작 시간         |
| frame\_timestamp    | 프레임 기준 타임스탬프 |
| game\_id            | 게임 고유 ID           |
| team\_id            | 보상을 받을 팀 ID      |
| timestamp           | 게임 내 시간           |
| type                | 이벤트 타입            |


### 🔹 `events__PAUSE_END`

| 영어 칼럼명      | 한글 설명                      |
| ---------------- | ------------------------------ |
| frame\_timestamp | 프레임 기준 타임스탬프         |
| game\_id         | 게임 고유 ID                   |
| real\_timestamp  | 실제 현실 시간                 |
| timestamp        | 게임 내 시간                   |
| type             | 이벤트 타입 (일시정지 종료 등) |


### 🔹 `events__SKILL_LEVEL_UP`

| 영어 칼럼명      | 한글 설명                          |
| ---------------- | ---------------------------------- |
| frame\_timestamp | 프레임 기준 타임스탬프             |
| game\_id         | 게임 고유 ID                       |
| level\_up\_type  | 스킬 레벨업 유형 (일반/궁극기 등)  |
| participant\_id  | 스킬을 올린 참가자 ID              |
| skill\_slot      | 스킬 슬롯 (예: 0:Q, 1:W, 2:E, 3:R) |
| timestamp        | 실제 발생 시간                     |
| type             | 이벤트 타입                        |


### 🔹 `events__TURRET_PLATE_DESTROYED`

| 영어 칼럼명      | 한글 설명                        |
| ---------------- | -------------------------------- |
| frame\_timestamp | 프레임 기준 타임스탬프           |
| game\_id         | 게임 고유 ID                     |
| killer\_id       | 포탑 플레이트를 파괴한 참가자 ID |
| lane\_type       | 라인 종류 (탑, 미드, 바텀 등)    |
| position\_x      | x 좌표 위치                      |
| position\_y      | y 좌표 위치                      |
| team\_id         | 파괴한 팀 ID                     |
| timestamp        | 실제 발생 시간                   |
| type             | 이벤트 타입                      |


### 🔹 `events__WARD_KILL`

| 영어 칼럼명      | 한글 설명                           |
| ---------------- | ----------------------------------- |
| frame\_timestamp | 프레임 기준 타임스탬프              |
| game\_id         | 게임 고유 ID                        |
| killer\_id       | 와드를 파괴한 참가자 ID             |
| timestamp        | 실제 발생 시간                      |
| type             | 이벤트 타입                         |
| ward\_type       | 와드 종류 (제어 와드, 시야 와드 등) |


### 🔹 `events__WARD_PLACED`

| 영어 칼럼명      | 한글 설명               |
| ---------------- | ----------------------- |
| creator\_id      | 와드를 설치한 참가자 ID |
| frame\_timestamp | 프레임 기준 타임스탬프  |
| game\_id         | 게임 고유 ID            |
| timestamp        | 실제 발생 시간          |
| type             | 이벤트 타입             |
| ward\_type       | 와드 종류               |


### 🔹 `frames`

| 영어 칼럼명 | 한글 설명                                |
| ----------- | ---------------------------------------- |
| game\_id    | 게임 고유 ID                             |
| timestamp   | 해당 프레임의 게임 내 시간 (밀리초 기준) |

> 📝 프레임은 일정 간격마다 저장된 게임의 전체 상태를 의미해.


### 🔹 `matches`

| 영어 칼럼명           | 한글 설명                             |
| --------------------- | ------------------------------------- |
| match\_id             | 매치 고유 ID                          |
| game\_id              | 게임 고유 ID                          |
| data\_version         | 데이터 버전 (패치 버전 등)            |
| end\_of\_game\_result | 게임 종료 결과 (승/패 여부 또는 비고) |
| frame\_interval       | 프레임 간격 (예: 1000ms 단위 등)      |

> 📝 하나의 매치에 대한 메타 정보로, 분석 전 전체 구조 파악에 유용해.


### 🔹 `participants_frames`

| 영어 칼럼명                    | 한글 설명                 |
| ------------------------------ | ------------------------- |
| game\_id                       | 게임 고유 ID              |
| participant\_id                | 참가자 ID                 |
| frame\_timestamp               | 해당 프레임의 시간        |
| current\_gold                  | 현재 소지 골드            |
| gold\_per\_second              | 초당 골드 획득량          |
| jungle\_minions\_killed        | 정글 몬스터 처치 수       |
| level                          | 레벨                      |
| minions\_killed                | 미니언 처치 수            |
| time\_enemy\_spent\_controlled | 상대를 군중제어한 시간    |
| total\_gold                    | 총 골드 획득량            |
| xp                             | 경험치                    |
| position\_x                    | 지도상의 x좌표            |
| position\_y                    | 지도상의 y좌표            |
| abilityhaste                   | 스킬 가속                 |
| abilitypower                   | 주문력                    |
| armor                          | 방어력                    |
| armorpen                       | 방어구 관통력             |
| armorpenpercent                | 방어구 관통(%)            |
| attackdamage                   | 공격력                    |
| attackspeed                    | 공격 속도                 |
| bonusarmorpenpercent           | 추가 방관(%)              |
| bonusmagicpenpercent           | 추가 마법 관통(%)         |
| ccreduction                    | 군중제어 감소             |
| cooldownreduction              | 쿨타임 감소               |
| health                         | 현재 체력                 |
| healthmax                      | 최대 체력                 |
| healthregen                    | 체력 재생                 |
| lifesteal                      | 흡혈 수치                 |
| magicpen                       | 마법 관통 수치            |
| magicpenpercent                | 마법 관통(%)              |
| magicresist                    | 마법 저항력               |
| movementspeed                  | 이동 속도                 |
| omnivamp                       | 만능 흡혈                 |
| physicalvamp                   | 물리 흡혈                 |
| power                          | 현재 자원량 (마나 등)     |
| powermax                       | 최대 자원량               |
| powerregen                     | 자원 재생 속도            |
| spellvamp                      | 주문 흡혈                 |
| magicDamageDone                | 누적 마법 피해            |
| magicDamageDoneToChampions     | 챔피언에게 가한 마법 피해 |
| magicDamageTaken               | 받은 마법 피해            |
| physicalDamageDone             | 누적 물리 피해            |
| physicalDamageDoneToChampions  | 챔피언에게 가한 물리 피해 |
| physicalDamageTaken            | 받은 물리 피해            |
| totalDamageDone                | 총 피해                   |
| totalDamageDoneToChampions     | 챔피언에게 가한 총 피해   |
| totalDamageTaken               | 받은 총 피해              |
| trueDamageDone                 | 고정 피해                 |
| trueDamageDoneToChampions      | 챔피언에게 가한 고정 피해 |
| trueDamageTaken                | 받은 고정 피해            |

> 📝 이 테이블은 **시간에 따라 변화하는 유저의 상태**를 추적하는 데 핵심이야.  
> 추세 분석, 유사도 파생 변수, 전투력 곡선 등의 기반이 될 수 있어.


### 🔹 `participants`

| 영어 칼럼명     | 한글 설명                      |
| --------------- | ------------------------------ |
| game\_id        | 게임 고유 ID                   |
| participant\_id | 참가자 ID                      |
| puuid           | 플레이어 고유 ID (전역 식별자) |

> 📝 `puuid`는 **op.gg 검색**, 유사도 비교 등에서 핵심 ID로 사용돼.

