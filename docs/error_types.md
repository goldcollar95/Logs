# Error Type Definitions

본 문서는 로그 분석 파이프라인에서 사용되는
공식 에러 타입 정의를 관리한다.

---

## E001_DB_CONNECTION_TIMEOUT

- source: #1
- layer: database
- execution_type: batch
- severity: HIGH
- description: 배치 작업 중 DB 커넥션 풀 고갈로 인한 타임아웃

---

## E002_DB_TRIGGER_INVALID

- source: #2
- layer: database
- execution_type: realtime_api
- severity: MEDIUM
- description: DB 트리거 Invalid로 인해 UPDATE 실패 (배포/DDL 영향)

---

## E003_SECURITY_REQUEST_REJECTED

- source: #3
- layer: security
- execution_type: realtime_web
- severity: LOW
- description: Spring Security Firewall에 의해 차단된 비정상 URL 요청
