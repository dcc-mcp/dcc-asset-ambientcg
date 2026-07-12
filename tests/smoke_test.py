from __future__ import annotations

import importlib.util
import io
import os
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skill" / "ambientcg-assets"
SCRIPTS = SKILL / "scripts"


def load(name: str):
    sys.path.insert(0, str(SCRIPTS))
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


def validate_skill() -> None:
    from dcc_mcp_core import validate_skill

    report = validate_skill(str(SKILL))
    assert not report.has_errors, report


def descriptor_smoke() -> None:
    downloader = load("download_ambientcg_asset")
    descriptor = downloader.asset_descriptor(
        "Wood095", "/tmp/Wood095.zip", {"downloadAttribute": "2K-JPG", "downloadLink": "https://example.com/Wood095.zip"}
    )
    assert descriptor["variants"][0]["local_path"] == "/tmp/Wood095.zip"
    assert descriptor["attribution"]["license_spdx"] == "CC0-1.0"
    assert descriptor["extra"]["download_attribute"] == "2K-JPG"


def download_headers_smoke() -> None:
    helper = load("_ambientcg")
    observed = {}

    class Response(io.BytesIO):
        def __enter__(self):
            return self

        def __exit__(self, *_args):
            self.close()

    def fake_urlopen(request, timeout):
        observed["headers"] = dict(request.header_items())
        observed["timeout"] = timeout
        return Response(b"zip-data")

    original = helper.urllib.request.urlopen
    helper.urllib.request.urlopen = fake_urlopen
    try:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(helper.fetch("https://ambientCG.com/get?file=Metal063_1K-JPG.zip", tmp))
            assert path.read_bytes() == b"zip-data"
            assert not path.with_suffix(".zip.part").exists()
    finally:
        helper.urllib.request.urlopen = original

    assert observed["headers"]["User-agent"].startswith("dcc-mcp/")
    assert observed["headers"]["Referer"] == "https://ambientcg.com/"
    assert observed["timeout"] == 180


def live_ambientcg_smoke() -> None:
    if os.environ.get("RUN_LIVE_API_SMOKE") != "true":
        print("skip live ambientCG API smoke")
        return
    search = load("search_ambientcg_assets").main(query="3D", asset_type="3DModel", limit=1)
    assert search["success"], search
    assert search["context"]["assets"], search
    downloads = load("list_ambientcg_downloads").main(asset_id="Wood095")
    assert downloads["success"], downloads
    assert downloads["context"]["downloads"], downloads


def main() -> None:
    validate_skill()
    descriptor_smoke()
    download_headers_smoke()
    live_ambientcg_smoke()


if __name__ == "__main__":
    main()
