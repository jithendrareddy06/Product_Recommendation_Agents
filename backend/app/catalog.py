from __future__ import annotations

import json
from pathlib import Path

from app.models import Product

_CATALOG_PATH = Path(__file__).resolve().parent.parent / "data" / "products.json"
_cache: list[Product] | None = None


def load_catalog() -> list[Product]:
    global _cache
    if _cache is None:
        raw = json.loads(_CATALOG_PATH.read_text(encoding="utf-8"))
        _cache = [Product.model_validate(item) for item in raw]
    return _cache


def get_product_by_id(product_id: str) -> Product | None:
    for product in load_catalog():
        if product.id == product_id:
            return product
    return None


def valid_product_ids(ids: list[str]) -> bool:
    catalog_ids = {p.id for p in load_catalog()}
    return all(i in catalog_ids for i in ids)
