from __future__ import annotations

from app.models import AgentTraceStep, ComparisonMatrix, ComparisonRow, Product, StructuredRequirements

_CRITERION_LABELS: dict[str, str] = {
    "rating": "Rating",
    "price_inr": "Price",
    "battery_life": "Battery life",
    "sound_quality": "Sound quality",
    "noise_cancellation": "Noise cancellation",
    "connectivity": "Connectivity",
    "processor": "Processor",
    "ram": "RAM",
    "storage": "Storage",
    "display": "Display",
    "water_resistance": "Water resistance",
    "gps": "GPS",
}


def _format_value(key: str, product: Product) -> str:
    if key == "rating":
        return f"{product.rating:.1f} / 5"
    if key == "price_inr":
        return f"₹{product.price_inr:,.0f}"
    if key in product.specs:
        return product.specs[key]
    return "N/A"


def build_comparison(
    candidates: list[Product], requirements: StructuredRequirements
) -> tuple[ComparisonMatrix, AgentTraceStep]:
    if not candidates:
        empty = ComparisonMatrix(product_ids=[], product_titles={}, rows=[])
        trace = AgentTraceStep(
            agent="ComparisonAgent",
            summary="No products to compare.",
            detail={"row_count": 0},
        )
        return empty, trace

    product_ids = [p.id for p in candidates]
    titles = {p.id: p.title for p in candidates}

    spec_keys: set[str] = set()
    for product in candidates:
        spec_keys.update(product.specs.keys())

    row_keys = ["rating", "price_inr", *sorted(spec_keys)]
    rows: list[ComparisonRow] = []
    for key in row_keys:
        label = _CRITERION_LABELS.get(key, key.replace("_", " ").title())
        values = {p.id: _format_value(key, p) for p in candidates}
        rows.append(ComparisonRow(criterion=label, values=values))

    matrix = ComparisonMatrix(product_ids=product_ids, product_titles=titles, rows=rows)
    trace = AgentTraceStep(
        agent="ComparisonAgent",
        summary=f"Built comparison table with {len(rows)} criteria for {len(candidates)} products.",
        detail={
            "criteria": [r.criterion for r in rows],
            "priorities_considered": requirements.priorities,
        },
    )
    return matrix, trace
