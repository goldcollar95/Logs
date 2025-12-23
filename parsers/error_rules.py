ERROR_RULES = {
    "E001_DB_CONNECTION_TIMEOUT": {
        "keywords": [
            "CannotGetJdbcConnectionException",
            "SQLTransientConnectionException",
            "Connection is not available"
        ],
        "layer": "database",
        "execution_type": "batch",
        "severity": "HIGH"
    },
    "E002_DB_TRIGGER_INVALID": {
        "keywords": [
            "ORA-04098",
            "BadSqlGrammarException",
            "trigger"
        ],
        "layer": "database",
        "execution_type": "realtime_api",
        "severity": "MEDIUM"
    },
    "E003_SECURITY_REQUEST_REJECTED": {
        "keywords": [
            "RequestRejectedException",
            "StrictHttpFirewall",
            "malicious String"
        ],
        "layer": "security",
        "execution_type": "realtime_web",
        "severity": "LOW"
    }
}


def detect_error_type(log_message: str):
    """
    로그 메시지를 기반으로 error_code를 판별한다.
    """
    for error_code, rule in ERROR_RULES.items():
        for keyword in rule["keywords"]:
            if keyword in log_message:
                return {
                    "error_code": error_code,
                    "layer": rule["layer"],
                    "execution_type": rule["execution_type"],
                    "severity": rule["severity"]
                }

    return {
        "error_code": "UNKNOWN",
        "layer": "unknown",
        "execution_type": "unknown",
        "severity": "LOW"
    }



def parse_log_record(log: dict) -> dict:
    """
    Raw 로그(dict)를 분석용 Parsed 로그로 변환
    """

    detection = detect_error_type(log.get("message", ""))

    return  {
        "timestamp"      : log.get("timestamp"),
        "service"        : log.get("service"),
        "error_code"     : detection["error_code"],
        "layer"          : detection["dection"],
        "execution_type" : detection["execution_type"],
        "severity"       : detection["serverity"]
    }