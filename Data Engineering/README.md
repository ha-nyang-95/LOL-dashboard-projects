# < 2025-04-09 > DE 1차 회의 및 작업 현황
## 1. API 파이프 라인 구축
- 시간이 오래 걸려도 `메타 데이터 명세화`.
- 모든 데이터를 적재해서 `데이터 웨어하우스` 구현

## 2. 기록
- 최적화
    - API를 불러올 때 중복되는 matchID가 존재하여 `set() 자료구조`와 `matchID`를 통해 중복되는 match 제외.
    - 결과적으로 JSON 데이터를 적재하는 데 걸리는 `시간 1.5 ~ 2배 단축`.
- 명세서 분업
    - 웅희: event의 key 값들에 대한 명세 작성
    - 형석: participants의 key 값들에 대한 명세 작성.
- 명세서를 왜 작성하는가?
    - DA와 DE의 커뮤니케이션을 위해서는 공통된 언어적 기준이 필요. 명세서는 이를 보조함.



# < 향후 계획 >
- 최종적으로 일 단위 업데이트되는 API 데이터를 'kafka &rightarrow; Flink or Spark &rightarrow; postgreSQL raw 적재 &rightarrow; postgreSQL RDBMS' 적재 파이프라인 구축.