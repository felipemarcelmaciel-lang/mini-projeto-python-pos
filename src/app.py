from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

class SomaRequest(BaseModel):
    x: float
    y: float

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/stats")
def stats():
    with open("stats.json", "r", encoding="utf-8") as f:
        return json.load(f)

@app.post("/soma")
def soma(dados: SomaRequest):
    return {"resultado": dados.x + dados.y}