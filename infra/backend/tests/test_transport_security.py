from mcp.server.transport_security import (
    TransportSecurityMiddleware,
    TransportSecuritySettings,
)
from starlette.testclient import TestClient

from app import CHATGPT_ORIGINS, _create_app


def test_rejects_unapproved_origin():
    middleware = TransportSecurityMiddleware(
        TransportSecuritySettings(
            allowed_hosts=["mcp.dincerlogistics.com"],
            allowed_origins=list(CHATGPT_ORIGINS),
        )
    )

    assert middleware._validate_origin("https://chatgpt.com")
    assert not middleware._validate_origin("https://evil.example")

    client = TestClient(_create_app("testserver"))
    metadata = "/.well-known/oauth-authorization-server"
    assert client.get(metadata, headers={"Origin": "https://chatgpt.com"}).status_code == 200
    assert client.get(metadata, headers={"Origin": "https://evil.example"}).status_code == 403
