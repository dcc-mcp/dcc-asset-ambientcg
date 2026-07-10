---
name: ambientcg-assets
description: Search, inspect, and download ambientCG CC0 assets as validated AssetDescriptors.
license: MIT
compatibility: "dcc-mcp-core 0.19+, Python 3.7+"
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
    produces: [asset_descriptor]
    tools: tools.yaml
---

# ambientCG Assets

Use this skill for ambientCG asset discovery and archive downloads. It uses the
stable v2 `full_json` and `downloads_csv` endpoints because they expose direct
download rows.

`download_ambientcg_asset` returns an `asset_descriptor` with the local archive, CC0 attribution,
and source download metadata. Pass that descriptor to a DCC adapter import skill.
