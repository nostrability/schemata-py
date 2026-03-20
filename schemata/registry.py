"""Schema registry — loads vendored JSON schemas by key."""

import json
from pathlib import Path
from typing import Any, Optional

from schemata._registry_map import REGISTRY

_SCHEMAS_DIR = Path(__file__).parent
_cache: dict[str, Any] = {}


def get(key: str) -> Optional[dict]:
    """Return parsed JSON schema for the given key, or None."""
    if key in _cache:
        return _cache[key]
    path = REGISTRY.get(key)
    if path is None:
        return None
    full_path = _SCHEMAS_DIR / path
    if not full_path.exists():
        return None
    with open(full_path) as f:
        schema = json.load(f)
    _cache[key] = schema
    return schema


def keys() -> list[str]:
    """Return all available schema registry keys."""
    return sorted(REGISTRY.keys())
