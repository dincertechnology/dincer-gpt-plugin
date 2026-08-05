import asyncio
import os

os.environ.setdefault("BUCKET_NAME", "test-bucket")
os.environ.setdefault("DEPOT_KEY", "depot.xlsx")
os.environ.setdefault("TRANSPORT_KEY", "transport.xlsx")
os.environ.setdefault("COGNITO_ISSUER", "https://example.invalid")
os.environ.setdefault("COGNITO_CLIENT_ID", "test-client")
os.environ.setdefault("COGNITO_LOGIN_DOMAIN", "https://example.invalid")
os.environ.setdefault("CHATGPT_OAUTH_CALLBACK", "https://chatgpt.com/connector/oauth/test")

from mcp.server.fastmcp import FastMCP

import app


def test_tools_have_descriptions_and_output_schemas():
    server = FastMCP("test")
    server.add_tool(app.sources_status)
    server.add_tool(app.query_data)

    tools = {tool.name: tool for tool in asyncio.run(server.list_tools())}

    assert "last-modified" in tools["sources_status"].description
    assert tools["sources_status"].outputSchema["type"] == "object"
    assert "sources" in tools["sources_status"].outputSchema["properties"]
    assert tools["query_data"].outputSchema["type"] == "object"
    assert "matches" in tools["query_data"].outputSchema["properties"]
