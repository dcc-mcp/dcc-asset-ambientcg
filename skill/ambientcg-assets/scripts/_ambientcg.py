from __future__ import annotations

import csv
import json
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


BASE_URL = "https://ambientCG.com/api/v2"


def json_api(path: str, params: dict[str, Any]) -> dict[str, Any]:
    url = BASE_URL + path + "?" + urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
    with urllib.request.urlopen(url, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def download_rows(asset_id: str) -> list[dict[str, str]]:
    url = BASE_URL + "/downloads_csv?" + urllib.parse.urlencode({"id": asset_id})
    with urllib.request.urlopen(url, timeout=30) as resp:
        text = resp.read().decode("utf-8")
    return list(csv.DictReader(text.splitlines()))


def fetch(url: str, output_dir: str) -> str:
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    name = urllib.parse.urlparse(url).query.removeprefix("file=") or urllib.parse.urlparse(url).path.rsplit("/", 1)[-1]
    target = Path(output_dir) / urllib.parse.unquote(name)
    urllib.request.urlretrieve(url, target)
    return str(target)

