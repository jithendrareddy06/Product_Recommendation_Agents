from __future__ import annotations

import re

from app.llm import llm_available, structured_completion
from app.models import AgentTraceStep, StructuredRequirements

_SYSTEM = (
    "You are the Requirement Agent for an e-commerce shopping assistant. "
    "Extract structured shopping requirements from the user query. "
    "Categories include: headphones, laptop, smartwatch, smartphone, tablet, "
    "television, speaker, camera, appliance. "
    "Set budget_specified to true ONLY if the user clearly states a budget, "
    "price limit, or 'under X'. If they do not mention money, set budget_specified "
    "to false and max_price_inr to null. "
    "For queries like 'best watches' or 'best phones', set priorities to include quality/rating."
)


class _RequirementLLMOut(StructuredRequirements):
    pass


def _extract_budget(text: str) -> tuple[bool, float | None]:
    inr_match = re.search(r"(?:₹|rs\.?|inr)\s*([\d,]+(?:\.\d+)?)", text, re.I)
    under_match = re.search(
        r"(?:under|below|less than|max|upto|up to)\s*(?:₹|rs\.?|inr)?\s*([\d,]+(?:\.\d+)?)",
        text,
        re.I,
    )
    for match in (under_match, inr_match):
        if match:
            return True, float(match.group(1).replace(",", ""))
    return False, None


def _detect_category(text: str) -> str:
    rules: list[tuple[tuple[str, ...], str]] = [
        (("laptop", "notebook", "macbook", "ultrabook"), "laptop"),
        (("smartwatch", "smart watch", "watch", "watches", "fitness band", "fitness tracker"), "smartwatch"),
        (("phone", "phones", "smartphone", "mobile", "iphone", "android phone"), "smartphone"),
        (("tablet", "ipad", "tab "), "tablet"),
        (("tv", "television", "smart tv", "led tv"), "television"),
        (("speaker", "soundbar", "bluetooth speaker"), "speaker"),
        (("camera", "dslr", "mirrorless", "action cam"), "camera"),
        (("fridge", "refrigerator", "washing machine", "air fryer", "mixer", "vacuum", "appliance"), "appliance"),
        (("headphone", "headphones", "earphone", "earbuds", "tws", "headset"), "headphones"),
    ]
    for keywords, category in rules:
        if any(k in text for k in keywords):
            return category
    return "headphones"


def _heuristic_requirements(query: str) -> StructuredRequirements:
    text = query.lower()
    category = _detect_category(text)
    budget_specified, max_price = _extract_budget(text)

    keywords: list[str] = []
    for term in (
        "wireless",
        "bluetooth",
        "anc",
        "noise cancellation",
        "gaming",
        "sport",
        "over-ear",
        "earbuds",
        "sound quality",
        "battery",
        "gps",
        "amoled",
        "5g",
        "4k",
    ):
        if term in text:
            keywords.append(term)

    priorities: list[str] = []
    if any(w in text for w in ("best", "top", "premium", "good quality")):
        priorities.append("rating")
    if "sound quality" in text or "good sound" in text:
        priorities.append("sound quality")
    if "noise" in text or "anc" in text:
        priorities.append("noise cancellation")
    if "battery" in text:
        priorities.append("battery life")
    if "lightweight" in text or "travel" in text:
        priorities.append("portability")
    if "camera" in text and category == "smartphone":
        priorities.append("camera")

    return StructuredRequirements(
        category=category,
        max_price_inr=max_price,
        budget_specified=budget_specified,
        keywords=keywords,
        priorities=priorities,
    )


def parse_requirements(query: str) -> tuple[StructuredRequirements, AgentTraceStep]:
    requirements: StructuredRequirements | None = None
    source = "heuristic"

    if llm_available():
        requirements = structured_completion(_SYSTEM, query, _RequirementLLMOut)

    if requirements is None:
        requirements = _heuristic_requirements(query)
    else:
        source = "llm"
        if not requirements.budget_specified:
            requirements = requirements.model_copy(update={"max_price_inr": None})

    budget_note = (
        f"budget ₹{requirements.max_price_inr:.0f}"
        if requirements.budget_specified and requirements.max_price_inr is not None
        else "no budget specified"
    )
    trace = AgentTraceStep(
        agent="RequirementAgent",
        summary=f"Parsed requirements ({source}): {requirements.category}, {budget_note}.",
        detail=requirements.model_dump(),
    )
    return requirements, trace
