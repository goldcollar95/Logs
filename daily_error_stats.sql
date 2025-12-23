-- daily_error_stats.sql
-- 목적: 일별 에러 유형 집계를 위한 분석 테이블 정의
-- 이 SQL은 설계 산출물이며, 실제 실행은 환경에 따라 선택적으로 수행한다.


CREATE TABLE daily_error_stats (
    date DATE,
    error_code VARCHAR(50),
    execution_type VARCHAR(30),
    error_count INT
);