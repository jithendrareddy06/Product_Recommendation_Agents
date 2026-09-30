from __future__ import annotations

import json

from app.catalog import get_product_by_id
from app.llm import llm_available, structured_completion
from app.models import (
    AgentTraceStep,
    ComparisonMatrix,
    Product,
    Recommendation,
    StructuredRequirements,
)


class _RecommendationLLMOut(Recommendation):
    pass


def _heuristic_recommendation(
    candidates: list[Product],
    requirements: StructuredRequirements,
) -> Recommendation:
    if not candidates:
        return Recommendation(
            product_id="",
            title="No matching products",
            score=0.0,
            reasons=["Try increasing your budget or broadening the product category."],
        )

    def score_product(p: Product) -> float:
        s = p.rating * 2.0
        if requirements.priorities:
            blob = " ".join([p.description, *p.specs.values()]).lower()
            for priority in requirements.priorities:
                if priority.lower() in blob:
                    s += 1.5
        s += max(0.0, (requirements.max_price_inr - p.price_inr) / max(requirements.max_price_inr, 1))
        return s

    best = max(candidates, key=score_product)
    reasons = [
        f"Rated {best.rating}/5 within your ₹{requirements.max_price_inr:,.0f} budget.",
        f"Priced at ₹{best.price_inr:,.0f}, leaving room under your cap.",
    ]
    if requirements.priorities:
        reasons.append(f"Aligns with your priorities: {', '.join(requirements.priorities)}.")

    return Recommendation(
        product_id=best.id,
        title=best.title,
        score=round(score_product(best), 2),
        reasons=reasons[:3],
    )


def recommend_product(
    candidates: list[Product],
    requirements: StructuredRequirements,
    comparison: ComparisonMatrix,
) -> tuple[Recommendation, AgentTraceStep]:
    allowed_ids = {p.id for p in candidates}
    recommendation: Recommendation | None = None
    source = "heuristic"

    if llm_available() and candidates:
        catalog_blob = json.dumps([p.model_dump() for p in candidates], indent=2)
        comparison_blob = comparison.model_dump_json(indent=2)
        user = (
            f"User requirements:\n{requirements.model_dump_json()}\n\n"
            f"Candidate products (ONLY choose product_id from this list):\n{catalog_blob}\n\n"
            f"Comparison matrix:\n{comparison_blob}\n\n"
            "Pick the single best product_id and give 2-3 short reasons."
        )
        system = (
            "You are the Recommendation Agent. You must recommend exactly one product "
            "from the candidate list. product_id must match an id from the list. "
            "Reasons must cite real attributes (price, rating, specs)."
        )
        recommendation = structured_completion(system, user, _RecommendationLLMOut)

    if recommendation is None:
        recommendation = _heuristic_recommendation(candidates, requirements)
    else:
        source = "llm"

    if recommendation.product_id not in allowed_ids:
        product = get_product_by_id(recommendation.product_id)
        if product is None or product.id not in allowed_ids:
            recommendation = _heuristic_recommendation(candidates, requirements)
            source = "heuristic_corrected"

    if not recommendation.title and recommendation.product_id:
        p = get_product_by_id(recommendation.product_id)
        if p:
            recommendation = recommendation.model_copy(update={"title": p.title})

    trace = AgentTraceStep(
        agent="RecommendationAgent",
        summary=f"Recommended '{recommendation.title}' ({source}).",
        detail={
            "product_id": recommendation.product_id,
            "score": recommendation.score,
            "reasons": recommendation.reasons,
        },
    )
    return recommendation, trace
