from __future__ import annotations

from typing import TypedDict

from langgraph.graph import END, START, StateGraph

from app.agents.comparison import build_comparison
from app.agents.recommendation import recommend_product
from app.agents.requirement import parse_requirements
from app.agents.search import search_products
from app.models import (
    AgentTraceStep,
    ComparisonMatrix,
    Product,
    Recommendation,
    ShopResponse,
    StructuredRequirements,
)


class GraphState(TypedDict):
    query: str
    requirements: StructuredRequirements | None
    candidates: list[Product]
    comparison: ComparisonMatrix | None
    recommendation: Recommendation | None
    trace: list[AgentTraceStep]


def _node_requirement(state: GraphState) -> GraphState:
    requirements, step = parse_requirements(state["query"])
    trace = list(state.get("trace") or [])
    trace.append(step)
    return {
        **state,
        "requirements": requirements,
        "trace": trace,
    }


def _node_search(state: GraphState) -> GraphState:
    requirements = state["requirements"]
    if requirements is None:
        return state
    candidates, step = search_products(requirements)
    trace = list(state.get("trace") or [])
    trace.append(step)
    return {**state, "candidates": candidates, "trace": trace}


def _node_comparison(state: GraphState) -> GraphState:
    requirements = state["requirements"]
    candidates = state.get("candidates") or []
    if requirements is None:
        return state
    comparison, step = build_comparison(candidates, requirements)
    trace = list(state.get("trace") or [])
    trace.append(step)
    return {**state, "comparison": comparison, "trace": trace}


def _node_recommendation(state: GraphState) -> GraphState:
    requirements = state["requirements"]
    candidates = state.get("candidates") or []
    comparison = state.get("comparison")
    if requirements is None or comparison is None:
        return state
    recommendation, step = recommend_product(candidates, requirements, comparison)
    trace = list(state.get("trace") or [])
    trace.append(step)
    return {**state, "recommendation": recommendation, "trace": trace}


def _build_graph():
    graph = StateGraph(GraphState)
    graph.add_node("requirement", _node_requirement)
    graph.add_node("search", _node_search)
    graph.add_node("comparison", _node_comparison)
    graph.add_node("recommendation", _node_recommendation)

    graph.add_edge(START, "requirement")
    graph.add_edge("requirement", "search")
    graph.add_edge("search", "comparison")
    graph.add_edge("comparison", "recommendation")
    graph.add_edge("recommendation", END)

    return graph.compile()


_PIPELINE = _build_graph()


def run_shop_pipeline(query: str) -> ShopResponse:
    initial: GraphState = {
        "query": query,
        "requirements": None,
        "candidates": [],
        "comparison": None,
        "recommendation": None,
        "trace": [],
    }
    final = _PIPELINE.invoke(initial)

    requirements = final.get("requirements")
    comparison = final.get("comparison")
    recommendation = final.get("recommendation")

    if requirements is None or comparison is None or recommendation is None:
        raise RuntimeError("Pipeline did not produce a complete shop response.")

    return ShopResponse(
        query=query,
        requirements=requirements,
        products=final.get("candidates") or [],
        comparison=comparison,
        recommendation=recommendation,
        trace=final.get("trace") or [],
    )
