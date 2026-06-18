---
name: ambientcg-assets
description: Search, inspect, and download free ambientCG materials, HDRIs, and models.
license: MIT
compatibility: "dcc-mcp-core 0.18+"
metadata:
  dcc-mcp:
    version: v0.1.0
    dcc: python
    layer: domain
    tags:
      - asset
      - ambientcg
      - pbr
      - materials
      - hdris
      - models
      - download
    search-hint: "ambientcg, free pbr materials, texture archive, material download, hdri download, 3d model download"
    tools: tools.yaml
---

# ambientCG Assets

Use this skill for ambientCG asset discovery and archive downloads. It uses the
stable v2 `full_json` and `downloads_csv` endpoints because they expose direct
download rows.
