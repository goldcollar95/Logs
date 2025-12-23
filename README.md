# Log Incident Analysis Pipeline

운영 환경에서 발생하는 서비스 로그를 수집하여  
장애 유형별로 분류하고, 재발 패턴을 분석하기 위한 로그 분석 파이프라인 프로젝트입니다.

---

## 1. Problem

운영 중 장애가 발생할 때 로그는 존재했지만  
장애 유형, 발생 빈도, 재발 여부를 정량적으로 분석하기 어려웠습니다.

---

## 2. Approach

본 프로젝트는 로그를 단순 저장하지 않고  
먼저 **에러 타입을 정의**한 뒤, 해당 기준에 맞춰 로그를 구조화합니다.

---

## 3. Error Classification

에러 타입은 `docs/error_types.md`에서 관리되며  
Python 파서(`parsers/error_rules.py`)는 해당 기준을 코드로 구현합니다.

현재 정의된 에러 유형:

- E001_DB_CONNECTION_TIMEOUT (Batch / DB)
- E002_DB_TRIGGER_INVALID (Realtime API / DB)
- E003_SECURITY_REQUEST_REJECTED (Web / Security)

---

## 4. Output Example

```json
{
  "timestamp": "2025-12-22 14:50:36",
  "service": "api-service",
  "error_code": "E002_DB_TRIGGER_INVALID",
  "layer": "database",
  "execution_type": "realtime_api",
  "severity": "MEDIUM"
}
