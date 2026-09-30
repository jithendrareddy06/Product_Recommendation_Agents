from __future__ import annotations

from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.models import ShopRequest, ShopResponse
from app.orchestrator import run_shop_pipeline

app = FastAPI(title="ShopEasy Multi-Agent API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/api/shop", response_model=ShopResponse)
def shop(request: ShopRequest) -> ShopResponse:
    query = request.query.strip()
    if not query:
        raise HTTPException(status_code=400, detail="Query must not be empty.")
    try:
        return run_shop_pipeline(query)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
