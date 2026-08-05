import base64
import json
import os

os.environ.setdefault("BUCKET_NAME", "test-bucket")
os.environ.setdefault("DEPOT_KEY", "depot.xlsx")
os.environ.setdefault("TRANSPORT_KEY", "transport.xlsx")
os.environ.setdefault("COGNITO_ISSUER", "https://example.invalid")
os.environ.setdefault("COGNITO_CLIENT_ID", "test-client")
os.environ.setdefault("COGNITO_LOGIN_DOMAIN", "https://example.invalid")
os.environ.setdefault("CHATGPT_OAUTH_CALLBACK", "https://chatgpt.com/connector/oauth/test")

import app


def _event(tool_name: str) -> dict:
    return {
        "body": json.dumps(
            {"method": "tools/call", "params": {"name": tool_name}}
        ),
        "requestContext": {
            "authorizer": {"jwt": {"claims": {"sub": "test-user"}}}
        },
    }


def test_query_data_call_is_counted():
    assert app._query_call_name(_event("query_data")) == "query_data"


def test_base64_request_is_decoded():
    event = _event("query_data")
    event["body"] = base64.b64encode(event["body"].encode()).decode()
    event["isBase64Encoded"] = True
    assert app._query_call_name(event) == "query_data"


def test_sources_status_is_not_counted():
    assert app._query_call_name(_event("sources_status")) == "sources_status"


def test_invalid_json_is_ignored():
    assert app._query_call_name({"body": "not-json"}) is None


def test_query_data_updates_daily_counter(monkeypatch):
    calls = []

    class FakeDdb:
        def update_item(self, **kwargs):
            calls.append(kwargs)

    monkeypatch.setattr(app, "_ddb", lambda: FakeDdb())
    assert app._enforce_daily_query_limit(_event("query_data")) is None
    assert calls[0]["ExpressionAttributeValues"][":limit"] == {"N": "20"}


def test_limit_exceeded_returns_429(monkeypatch):
    class LimitExceeded(Exception):
        response = {"Error": {"Code": "ConditionalCheckFailedException"}}

    class FakeDdb:
        def update_item(self, **kwargs):
            raise LimitExceeded

    monkeypatch.setattr(app, "_ddb", lambda: FakeDdb())
    response = app._enforce_daily_query_limit(_event("query_data"))
    assert response["statusCode"] == 429
    assert "daily_query_limit_exceeded" in response["body"]
