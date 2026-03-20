from schemata import get, keys


def test_get_kind1():
    schema = get("kind1Schema")
    assert schema is not None
    assert "$schema" in schema or "allOf" in schema


def test_get_note():
    schema = get("noteSchema")
    assert schema is not None


def test_get_nonexistent():
    assert get("nonexistent") is None


def test_keys_count():
    assert len(keys()) > 100
