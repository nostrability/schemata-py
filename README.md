# schemata-py

Python data package for [Nostr](https://nostr.com/) protocol JSON schemas. Vendored from [nostrability/schemata](https://github.com/nostrability/schemata).

## Usage

```python
from schemata import get, keys

schema = get("kind1Schema")  # returns dict or None
all_keys = keys()            # sorted list of available keys
```

## License

GPL-3.0-or-later
