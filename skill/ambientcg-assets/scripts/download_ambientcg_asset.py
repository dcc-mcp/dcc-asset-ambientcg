from __future__ import annotations

from typing import Any

from dcc_mcp_core.skill import skill_entry, skill_error, skill_exception, skill_success

from _ambientcg import download_rows, fetch


@skill_entry
def main(
    asset_id: str,
    output_dir: str,
    download_attribute: str = "2K-JPG",
    use_raw_link: bool = False,
    **_: Any,
) -> dict[str, Any]:
    try:
        rows = download_rows(asset_id)
        row = next((r for r in rows if r.get("downloadAttribute") == download_attribute), None)
        if row is None:
            return skill_error("ambientCG download not found", download_attribute, downloads=rows)
        url = row.get("rawLink" if use_raw_link else "downloadLink")
        if not url:
            return skill_error("ambientCG download URL missing", download_attribute, row=row)
        path = fetch(url, output_dir)
        return skill_success("ambientCG asset downloaded", file=path, asset_id=asset_id, download=row)
    except Exception as exc:
        return skill_exception(exc, message="Failed to download ambientCG asset")


if __name__ == "__main__":
    from dcc_mcp_core.skill import run_main

    run_main(main)
