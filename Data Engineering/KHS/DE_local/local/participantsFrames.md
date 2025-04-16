# participantFrames
각 프레임의 참가자 ID별 상태 (1~10번 참가자 존재)

예: participantFrames.1.championStats.abilityPower

---

## 챔피언 능력치 (championStats)

### < participantFrames.{id}.championStats.abilityHaste >

사용 정의  
스킬의 재사용 대기시간을 줄여주는 능력치입니다.

같이 사용되는 key: 
- championStats.cooldownReduction(과거 쿨타임 감소)

example: participantFrames.4.championStats.abilityHaste = 20

### < participantFrames.{id}.championStats.abilityPower >

사용 정의  
스킬 피해량에 영향을 주는 주문력입니다.

같이 사용되는 key: 
- championStats.magicPen

example: participantFrames.1.championStats.abilityPower = 45

### < participantFrames.{id}.championStats.armor >

사용 정의  
물리 피해를 감소시키는 방어력입니다.

같이 사용되는 key: 
- championStats.armorPen  

example: participantFrames.3.championStats.armor = 38

### < participantFrames.{id}.championStats.armorPen >

사용 정의  
적의 방어력을 관통할 수 있는 수치입니다.

같이 사용되는 key: 
- championStats.attackDamage  

example: participantFrames.5.championStats.armorPen = 12

### < participantFrames.{id}.championStats.armorPenPercent >

사용 정의  
적의 방어력을 몇 퍼센트 무시할지 결정하는 능력치입니다.

같이 사용되는 key: 
- championStats.bonusArmorPenPercent  

example: participantFrames.2.championStats.armorPenPercent = 0.25

### < participantFrames.{id}.championStats.attackDamage >

사용 정의  
기본 공격 피해량입니다.

같이 사용되는 key: 
- championStats.attackSpeed  

example: participantFrames.8.championStats.attackDamage = 90

### < participantFrames.{id}.championStats.attackSpeed >

사용 정의  
초당 기본 공격 횟수입니다.

같이 사용되는 key: 
- championStats.attackDamage  

example: participantFrames.6.championStats.attackSpeed = 100

### < participantFrames.{id}.championStats.bonusArmorPenPercent >

사용 정의  
추가로 얻은 방어력 관통률입니다.

같이 사용되는 key: 
- championStats.armorPenPercent  

example: participantFrames.9.championStats.bonusArmorPenPercent = 0.15

### < participantFrames.{id}.championStats.bonusMagicPenPercent >

사용 정의  
추가 마법 관통 비율입니다.

같이 사용되는 key: 
- championStats.magicPenPercent  

example: participantFrames.7.championStats.bonusMagicPenPercent = 0.18

### < participantFrames.{id}.championStats.ccReduction >

사용 정의  
군중 제어 효과의 지속시간 감소 비율입니다.

example: participantFrames.5.championStats.ccReduction = 0.25

### < participantFrames.{id}.championStats.cooldownReduction >

사용 정의  
모든 스킬 쿨타임을 줄여주는 수치입니다.

example: participantFrames.1.championStats.cooldownReduction = 10

### < participantFrames.{id}.championStats.health >

사용 정의  
현재 체력 수치입니다.

같이 사용되는 key: 
- championStats.healthMax  

example: participantFrames.10.championStats.health = 760

### < participantFrames.{id}.championStats.healthMax >

사용 정의  
최대 체력입니다.

같이 사용되는 key: 
- championStats.health  

example: participantFrames.2.championStats.healthMax = 1200

### < participantFrames.{id}.championStats.healthRegen >

사용 정의  
초당 체력 재생 수치입니다.

example: participantFrames.7.championStats.healthRegen = 8.2

### < participantFrames.{id}.championStats.lifesteal >

사용 정의  
기본 공격 시 회복되는 비율입니다.

example: participantFrames.9.championStats.lifesteal = 0.10

### < participantFrames.{id}.championStats.magicPen >

사용 정의  
고정 마법 관통 수치입니다.

example: participantFrames.4.championStats.magicPen = 18

### < participantFrames.{id}.championStats.magicPenPercent >

사용 정의  
마법 관통 비율입니다.

example: participantFrames.6.championStats.magicPenPercent = 0.2

### < participantFrames.{id}.championStats.magicResist >

사용 정의  
마법 피해 감소를 위한 저항 수치입니다.

example: participantFrames.3.championStats.magicResist = 30

### < participantFrames.{id}.championStats.movementSpeed >

사용 정의  
챔피언의 이동 속도입니다.

example: participantFrames.8.championStats.movementSpeed = 345

### < participantFrames.{id}.championStats.omnivamp >

사용 정의  
모든 피해량의 일부를 체력으로 회복하는 비율입니다.

example: participantFrames.6.championStats.omnivamp = 0.07

### < participantFrames.{id}.championStats.physicalVamp >

사용 정의  
물리 피해의 일부를 회복하는 비율입니다.

example: participantFrames.5.championStats.physicalVamp = 0.08

### < participantFrames.{id}.championStats.power >

사용 정의  
현재 마나 또는 에너지(기력) 수치입니다. 

같이 사용되는 key: 
- powerMax  

example: participantFrames.4.championStats.power = 420

### < participantFrames.{id}.championStats.powerMax >

사용 정의  
최대 마나 또는 에너지(기력) 수치입니다.

example: participantFrames.4.championStats.powerMax = 700

### < participantFrames.{id}.championStats.powerRegen >

사용 정의  
초당 마나 재생 수치입니다.

example: participantFrames.3.championStats.powerRegen = 9.4

### < participantFrames.{id}.championStats.spellVamp >

사용 정의  
스킬 피해량의 일부를 회복하는 비율입니다.

example: participantFrames.6.championStats.spellVamp = 0.10

---

## 피해 정보 (damageStats)

### < participantFrames.{id}.damageStats.totalDamageDoneToChampions >

사용 정의  
챔피언에게 입힌 누적 총 피해량입니다.

같이 사용되는 key: 
- physicalDamageDoneToChampions
- magicDamageDoneToChampions 

example: participantFrames.2.damageStats.totalDamageDoneToChampions = 3870

### < participantFrames.{id}.damageStats.totalDamageDone >

사용 정의  
모든 대상에게 입힌 피해 총합입니다.

같이 사용되는 key:
- trueDamageDone
- magicDamageDone
- physicalDamageDone

example: participantFrames.2.damageStats.totalDamageDone = 9041

### < participantFrames.{id}.damageStats.totalDamageTaken >

사용 정의  
받은 누적 피해량입니다.

같이 사용되는 key: 
- magicDamageTaken(받은 마법 피해량 누적)
- physicalDamageTaken(받은 물리 피해량 누적)
- trueDamageTaken(받은 고정 피해량 누적)

example: participantFrames.2.damageStats.totalDamageTaken = 6750

### < participantFrames.{id}.damageStats.trueDamageDoneToChampions >

사용 정의  
챔피언에게 입힌 고정 피해량입니다.

example: participantFrames.3.damageStats.trueDamageDoneToChampions = 325


---

## 자원 관련

### < participantFrames.{id}.currentGold >

사용 정의  
현재 보유 중인 골드입니다.

같이 사용되는 key: 
- totalGold
- goldPerSecond(초당 골드 획득량)

example: participantFrames.5.currentGold = 715

### < participantFrames.{id}.totalGold >

사용 정의  
이전까지 획득한 총 골드입니다.

example: participantFrames.5.totalGold = 6420

### < participantFrames.{id}.goldPerSecond >

사용 정의  
초당 골드 획득량입니다.

example: participantFrames.5.goldPerSecond = 1.3

---

## 기타

### < participantFrames.{id}.level >

사용 정의  
현재 챔피언 레벨입니다.

같이 사용되는 key:
- xp

example: participantFrames.1.level = 6

### < participantFrames.{id}.xp >

사용 정의  
누적 경험치입니다.

example: participantFrames.1.xp = 2445

### < participantFrames.{id}.minionsKilled >

사용 정의  
해당 시간까지의 미니언 처치 수입니다.

example: participantFrames.1.minionsKilled = 38

### < participantFrames.{id}.jungleMinionsKilled >

사용 정의  
정글 몬스터 처치 수입니다.

example: participantFrames.1.jungleMinionsKilled = 12

### < participantFrames.{id}.timeEnemySpentControlled >

사용 정의  
해당 플레이어가 경기 도중 적을 군중 제어 상태로 만든 총 시간(초 단위)입니다.  
이 수치는 스턴, 슬로우, 넉업, 침묵 등 다양한 CC 효과에 의해 적이 제어된 시간의 합입니다.

같이 사용되는 key: 
- damageStats.totalDamageDoneToChampions  
- championStats.ccReduction (CC 감쇠량)

example: participantFrames.2.timeEnemySpentControlled = 87

---

## 위치

x , y 좌표 범위 = 0 ~ 16k

### < participantFrames.{id}.position.x >

사용 정의  
지도상의 x좌표입니다.

같이 사용되는 key: position.y  
example: participantFrames.1.position.x = 7152

### < participantFrames.{id}.position.y >

사용 정의  
지도상의 y좌표입니다.

example: participantFrames.1.position.y = 10482
