"""
Resurrection AI - Core Application Entry Point
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Resurrection AI",
    description="Autonomous Threat Intelligence, Risk Assessment, and Decision Engine",
    version="0.1.0",
)

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {
        "status": "online",
        "system": "Resurrection AI",
        "version": "0.1.0",
        "modules": [
            "nox",
            "threat_intelligence",
            "risk_assessment",
            "decision_engine",
            "simulation",
            "ai_reasoning",
        ],
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
