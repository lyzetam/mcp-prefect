#!/usr/bin/env python3
"""
Prefect MCP Server wrapper
Provides workflow monitoring, debugging, and documentation access.
"""

from prefect_mcp_server.server import mcp

if __name__ == "__main__":
    mcp.run()
