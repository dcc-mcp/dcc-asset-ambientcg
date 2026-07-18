# DCC-MCP ambientCG Assets

<p align="center">
  <img src="docs/assets/dcc-asset-ambientcg.svg" alt="DCC-MCP · AMBIENTCG-ASSETS" width="600">
</p>

## Agent workflow

AI agents should use installed package skills through the shared gateway. IDE
users may continue to use the MCP endpoint.

```bash
dcc-mcp-cli dcc-types
dcc-mcp-cli list
dcc-mcp-cli search --query "<task>" --dcc-type <host>
dcc-mcp-cli describe <tool-slug>
dcc-mcp-cli call <tool-slug> --json '{"key":"value"}'
```

If the package skill is not active, call
`dcc-mcp-cli load-skill <skill-name> --dcc-type <host>`. After the task,
query `dcc-mcp-cli stats --range 24h --session-id <task-id>` and pass only
bounded evidence to the `review_skill_improvement` prompt from
`dcc-mcp-skills-creator`.


![Workflow showcase](docs/images/dcc-asset-ambientcg-showcase.webp)

Search and download ambientCG assets.

This skill uses the public ambientCG API and stores downloaded archives on disk.

## Install

```bash
dcc-mcp-cli marketplace add dcc-mcp/dcc-asset-ambientcg
dcc-mcp-cli marketplace install dcc-asset-ambientcg
```

## Tools

- `search_ambientcg_assets`
- `list_ambientcg_downloads`
- `download_ambientcg_asset`
