from __future__ import annotations

import json
import os
from typing import TypeVar

from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


def _client():
    from openai import OpenAI

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return None
    base_url = os.getenv("OPENAI_BASE_URL")
    if base_url:
        return OpenAI(api_key=api_key, base_url=base_url)
    return OpenAI(api_key=api_key)


def llm_available() -> bool:
    return _client() is not None


def structured_completion(
    system: str,
    user: str,
    schema: type[T],
    *,
    model: str | None = None,
) -> T | None:
    client = _client()
    if client is None:
        return None

    chosen_model = model or os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    response = client.chat.completions.create(
        model=chosen_model,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": schema.__name__,
                "schema": schema.model_json_schema(),
                "strict": True,
            },
        },
    )
    content = response.choices[0].message.content
    if not content:
        return None
    return schema.model_validate(json.loads(content))
