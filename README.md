# Resurrection AI

Autonomous Threat Intelligence, Risk Assessment, and Decision Engine.

## Project Structure

```text
resurrection-ai/
│
├── frontend/
│   └── src/
│       ├── components/
│       ├── pages/
│       └── services/
│
├── backend/
│   ├── main.py
│   ├── schemas/
│   ├── modules/
│   │   ├── nox/
│   │   ├── threat_intelligence/
│   │   ├── risk_assessment/
│   │   ├── decision_engine/
│   │   ├── simulation/
│   │   └── ai_reasoning/
│   └── services/
│
├── database/
│   └── migrations/
│
├── tests/
├── docs/
│   └── api-contracts/
│
├── requirements.txt
└── README.md
```

## Modules Overview

- **NOX**: Autonomous operations and orchestration core.
- **Threat Intelligence**: Real-time signal collection, threat actor profiling, and vulnerability indicators.
- **Risk Assessment**: Quantitative impact modeling and dynamic exposure scoring.
- **Decision Engine**: Automated heuristic and ML-driven mitigation policy execution.
- **Simulation**: Adversarial attack-surface simulations and synthetic scenario stress-testing.
- **AI Reasoning**: Multi-agent logical reasoning, explainability, and decision synthesis.

## Quickstart

### Backend Setup
```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt
uvicorn backend.main:app --reload
```

The API will be available at `http://localhost:8000` and Swagger documentation at `http://localhost:8000/docs`.

### Running Tests
```bash
pytest
```