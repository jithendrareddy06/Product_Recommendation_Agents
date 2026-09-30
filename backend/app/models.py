from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class StructuredRequirements(BaseModel):
    category: str = Field(description="Product category, e.g. headphones")
    max_price_inr: float | None = Field(
        default=None,
        description="Maximum budget in INR when the user stated one; otherwise null",
    )
    budget_specified: bool = Field(
        default=False,
        description="True only if the user explicitly gave a budget or price limit",
    )
    keywords: list[str] = Field(default_factory=list)
    priorities: list[str] = Field(default_factory=list)


class Product(BaseModel):
    id: str
    title: str
    category: str
    price_inr: float
    rating: float
    image_url: str
    description: str
    specs: dict[str, str] = Field(default_factory=dict)


class ComparisonRow(BaseModel):
    criterion: str
    values: dict[str, str] = Field(description="product_id -> display value")


class ComparisonMatrix(BaseModel):
    product_ids: list[str]
    product_titles: dict[str, str]
    rows: list[ComparisonRow]


class Recommendation(BaseModel):
    product_id: str
    title: str
    score: float | None = None
    reasons: list[str] = Field(default_factory=list)


class AgentTraceStep(BaseModel):
    agent: str
    summary: str
    detail: dict[str, Any] = Field(default_factory=dict)


class ShopState(BaseModel):
    query: str = ""
    requirements: StructuredRequirements | None = None
    candidates: list[Product] = Field(default_factory=list)
    comparison: ComparisonMatrix | None = None
    recommendation: Recommendation | None = None
    trace: list[AgentTraceStep] = Field(default_factory=list)


class ShopRequest(BaseModel):
    query: str


class ShopResponse(BaseModel):
    query: str
    requirements: StructuredRequirements
    products: list[Product]
    comparison: ComparisonMatrix
    recommendation: Recommendation
    trace: list[AgentTraceStep] = Field(default_factory=list)
