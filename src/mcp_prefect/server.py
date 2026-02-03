"""Prefect MCP Server wrapper.

Provides workflow monitoring, debugging, and documentation access.
Thin wrapper around the prefect-mcp-server package.
"""

from prefect_mcp_server.server import mcp


def main():
    """Entry point for MCP stdio server."""
    mcp.run()


if __name__ == "__main__":
    main()
