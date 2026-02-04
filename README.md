# mcp-prefect

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

MCP server wrapper for Prefect workflow orchestration. Thin wrapper around [`prefect-mcp-server`](https://pypi.org/project/prefect-mcp-server/) providing a consistent entry point.

## Features

16 tools for Prefect workflow management (provided by `prefect-mcp-server`):

| Category | Tools |
|----------|-------|
| Flows | `get_flow_by_id`, `get_flow_by_name`, `list_flows`, `search_flows`, `filter_flows` |
| Flow Runs | `get_flow_run_by_id`, `list_flow_runs`, `search_flow_runs_by_state`, `cancel_flow_run`, `create_flow_run`, `filter_flow_runs` |
| Deployments | `get_deployment_by_id`, `get_deployment_by_name`, `list_deployments`, `search_deployments_by_status`, `filter_deployments` |
| Execution | `create_flow_run_from_deployment` |

## Architecture

This package is a **thin wrapper** around `prefect-mcp-server`. It re-exports the MCP server instance and provides a CLI entry point:

```python
from prefect_mcp_server.server import mcp

def main():
    mcp.run()
```

All tool implementations are provided by `prefect-mcp-server`, which uses the official Prefect client library.

## Installation

```bash
pip install .
```

## Configuration

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `PREFECT_API_URL` | No | `http://localhost:4200/api` | Prefect API server URL |
| `PREFECT_API_KEY` | No | _(empty)_ | Prefect Cloud API key (required for Prefect Cloud) |

### `.env` Example

```bash
PREFECT_API_URL=https://api.prefect.cloud/api/accounts/YOUR_ACCOUNT/workspaces/YOUR_WORKSPACE
PREFECT_API_KEY=pnu_your_api_key_here
```

## Quick Start

### As MCP Server

```bash
# Run via stdio (for Claude Desktop/Code)
mcp-prefect
```

Add to Claude Code (`~/.claude.json`):

```json
{
  "mcpServers": {
    "prefect": {
      "type": "stdio",
      "command": "uv",
      "args": ["--directory", "/path/to/mcp-prefect", "run", "mcp-prefect"],
      "env": {
        "PREFECT_API_URL": "http://localhost:4200/api"
      }
    }
  }
}
```

### Docker

```bash
docker build -t mcp-prefect .
docker run -e PREFECT_API_URL=http://host.docker.internal:4200/api mcp-prefect
```

## License

MIT
