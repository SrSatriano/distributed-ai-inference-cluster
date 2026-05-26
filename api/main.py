"""Gateway de inferência distribuída."""

import os
import random
from typing import Any

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Inference Cluster Gateway", version="0.1.0")

WORKERS = os.getenv("WORKERS", "http://worker-1:8001,http://worker-2:8001").split(",")


class InferRequest(BaseModel):
    model: str
    prompt: str
    max_tokens: int = 256


class InferResponse(BaseModel):
    text: str
    worker: str


@app.get("/health")
def health() -> dict:
    return {"workers": len(WORKERS), "status": "ok"}


@app.post("/v1/infer", response_model=InferResponse)
def infer(req: InferRequest) -> InferResponse:
    if not WORKERS or WORKERS == [""]:
        raise HTTPException(503, "No workers configured")
    worker = random.choice(WORKERS)  # TODO: least-queue + health check
    # TODO: proxy to worker
    return InferResponse(
        text=f"[stub] resposta para: {req.prompt[:80]}...",
        worker=worker,
    )


@app.get("/metrics")
def metrics() -> dict[str, Any]:
    return {"queue_depth": 0, "active_requests": 0}
