from __future__ import annotations

from typing import Any

from dcc_mcp_core.skill import skill_entry, skill_exception, skill_success

from _ambientcg import json_api


@skill_entry
def main(
    query: str | None = None,
    asset_type: str = "all",
    sort: str = "Popular",
    limit: int = 10,
    **_: Any,
) -> dict[str, Any]:
    try:
        data = json_api(
            "/full_json",
            {"q": query, "sort": sort, "limit": 250 if asset_type != "all" else limit},
        )
        found = data.get("foundAssets", [])
        if asset_type != "all":
            found = [a for a in found if a.get("dataType") == asset_type]
        assets = [
            {
                "id": a.get("assetId"),
                "display_name": a.get("displayName"),
                "type": a.get("dataType"),
                "category": a.get("category"),
                "preview_image": (a.get("previewImage") or {}).get("256-PNG"),
                "short_link": a.get("shortLink"),
            }
            for a in found[:limit]
        ]
        return skill_success("ambientCG assets found", assets=assets, count=len(assets))
    except Exception as exc:
        return skill_exception(exc, message="Failed to search ambientCG")


if __name__ == "__main__":
    from dcc_mcp_core.skill import run_main

    run_main(main)
