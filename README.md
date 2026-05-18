# scrapy-itemlimit

Reusable Scrapy middleware for per-target item limiting during pagination crawls.

## Installation

```bash
pip install scrapy-itemlimit
```

## Included Middleware

### `PerTargetItemLimitSpiderMiddleware`

Stops further item output for a target key after the configured limit is reached.

Supported settings:

- `PER_TARGET_ITEM_LIMIT` (int)
- `TARGET_META_KEY` (str, default: `brand_token`)

## Scrapy Settings Example

```python
SPIDER_MIDDLEWARES = {
	"scrapy_itemlimit.middlewares.PerTargetItemLimitSpiderMiddleware": 543,
}

PER_TARGET_ITEM_LIMIT = 100
TARGET_META_KEY = "brand_token"
```

## Development Install

```bash
pip install -e .
```

## Build and Publish to PyPI

1. Bump version in both:
   - `setup.py`
   - `scrapy_itemlimit/__init__.py`
2. Build package:

```bash
python -m pip install --upgrade build twine
python -m build
```

3. Validate artifacts:

```bash
python -m twine check dist/*
```

4. Upload:

```bash
python -m twine upload dist/*
```

Optional (recommended first): TestPyPI

```bash
python -m twine upload --repository testpypi dist/*
```

## Version

Current package version: `0.2.0`
