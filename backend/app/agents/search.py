from __future__ import annotations

import re

from app.catalog import load_catalog
from app.models import AgentTraceStep, Product, StructuredRequirements

MAX_CANDIDATES = 8

_CATEGORY_ALIASES: dict[str, str] = {
    "headphone": "headphones",
    "headphones": "headphones",
    "earphone": "headphones",
    "earbuds": "headphones",
    "tws": "headphones",
    "headset": "headphones",
    "laptop": "laptop",
    "laptops": "laptop",
    "notebook": "laptop",
    "smartwatch": "smartwatch",
    "watch": "smartwatch",
    "watches": "smartwatch",
    "fitness band": "smartwatch",
    "smartphone": "smartphone",
    "phone": "smartphone",
    "phones": "smartphone",
    "mobile": "smartphone",
    "tablet": "tablet",
    "tablets": "tablet",
    "television": "television",
    "tv": "television",
    "speaker": "speaker",
    "speakers": "speaker",
    "camera": "camera",
    "cameras": "camera",
    "appliance": "appliance",
    "appliances": "appliance",
}


def _normalize_category(category: str) -> str:
    key = category.strip().lower()
    return _CATEGORY_ALIASES.get(key, key)


def _tokenize(text: str) -> set[str]:
    tokens = re.findall(r"[a-z0-9]+", text.lower())
    return {t for t in tokens if len(t) > 2}


def _keyword_score(product: Product, keywords: list[str]) -> float:
    if not keywords:
        return 0.0
    haystack = " ".join(
        [product.title, product.description, product.category, *product.specs.values()]
    ).lower()
    hits = sum(1 for kw in keywords if kw.lower() in haystack)
    return hits / len(keywords)


def search_products(requirements: StructuredRequirements) -> tuple[list[Product], AgentTraceStep]:
    category = _normalize_category(requirements.category)
    keywords = [k.strip().lower() for k in requirements.keywords if k.strip()]
    priorities = [p.strip().lower() for p in requirements.priorities if p.strip()]

    scored: list[tuple[float, Product]] = []
    for product in load_catalog():
        if _normalize_category(product.category) != category:
            continue
        if (
            requirements.budget_specified
            and requirements.max_price_inr is not None
            and product.price_inr > requirements.max_price_inr
        ):
            continue

        score = product.rating * 2.0
        if "rating" in priorities or any(p in ("rating", "best", "quality") for p in priorities):
            score += product.rating * 1.5
        score += _keyword_score(product, keywords) * 3.0
        score += _keyword_score(product, priorities) * 2.0

        if keywords or priorities:
            blob = " ".join(product.specs.values()).lower()
            for priority in priorities:
                if priority in blob or priority in product.description.lower():
                    score += 0.5

        scored.append((score, product))

    scored.sort(key=lambda x: (-x[0], -x[1].rating, x[1].price_inr))
    candidates = [p for _, p in scored[:MAX_CANDIDATES]]

    if requirements.budget_specified and requirements.max_price_inr is not None:
        budget_summary = f"under ₹{requirements.max_price_inr:.0f}"
    else:
        budget_summary = "all price ranges (no budget in query)"

    trace = AgentTraceStep(
        agent="SearchAgent",
        summary=f"Found {len(candidates)} products in '{category}' {budget_summary}.",
        detail={
            "category": category,
            "budget_specified": requirements.budget_specified,
            "max_price_inr": requirements.max_price_inr,
            "candidate_ids": [p.id for p in candidates],
            "total_matches_before_cap": len(scored),
        },
    )
    return candidates, trace
