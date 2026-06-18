---
name: ambientcg-assets
description: Search, inspect, and download free ambientCG materials, HDRIs, and models.
metadata:
  dcc-mcp:
    version: v0.1.0
    dcc: python
    display_name: ambientCG Assets
    group: asset.download.free
    default_icon: package
    affinity: any
    marketplace: dcc-asset-ambientcg
    tools: tools.yaml
    execution: sync
    permissions:
      - network
      - filesystem
    examples:
      - "Search ambientCG for rock models"
      - "List download archives for an ambientCG asset"
      - "Download a 2K JPG archive"
    contact:
      name: dcc-mcp team
      url: https://github.com/dcc-mcp/dcc-asset-ambientcg
    install:
      add_source: "dcc-mcp-cli marketplace add dcc-mcp/dcc-asset-ambientcg"
      then_install: "dcc-mcp-cli marketplace install dcc-asset-ambientcg"
---

# ambientCG Assets

Use this skill for ambientCG asset discovery and archive downloads. It uses the
stable v2 `full_json` and `downloads_csv` endpoints because they expose direct
download rows.
