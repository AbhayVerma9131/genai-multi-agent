from fastapi import FastAPI
from agents import orchestrator

app = FastAPI(title="Multi-Agent AI")

@app.get("/")
def home():
    return {"message": "AI Running 🚀"}

@app.post("/chat")
def chat(query: str):
    return orchestrator(query)
