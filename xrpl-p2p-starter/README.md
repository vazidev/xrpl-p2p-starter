# XRPL P2P Cross-Border Starter (FastAPI)

A GitHub-ready starter for a P2P remittance backend using **FastAPI** and **xrpl-py**. 
Implements the blueprint endpoints: quotes, transfers, KYC, and webhooks — with stubbed logic and clean separation of concerns.

## Features
- FastAPI with modular routers (`/v1/quotes`, `/v1/transfers`, `/v1/kyc`, `/v1/webhooks`)
- XRPL service wrapper using `xrpl-py`
- SQLite via SQLAlchemy for demo (replace with Postgres in prod)
- Pydantic models and idempotent transfer creation
- Simple in-memory rate/quote engine (stub) with slippage guardrails
- Dockerfile + docker-compose for local dev
- Example `.env` and `.http` request collection

## Quick Start (Local)
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Copy env
cp .env.example .env

# Run API
uvicorn app.main:app --reload
```

API docs: http://localhost:8000/docs

## Docker
```bash
docker compose up --build
```

## Endpoints (Sketch)
- `POST /v1/quotes` → get route & FX quote
- `POST /v1/transfers` → create transfer (idempotent), returns deposit address/memo
- `GET /v1/transfers/{id}` → status
- `POST /v1/kyc/verify` → submit KYC (stub)
- `GET /v1/limits` → get user limits (stub)
- `POST /v1/webhooks/xrpl` → ledger events (stub)
- `POST /v1/webhooks/ramp` → on/off-ramp callbacks (stub)

## Next Steps
- Replace SQLite with Postgres; plug real KYC/AML provider
- Integrate real FX/rates sources and market-maker/DEX connectors
- Add auth (OIDC/JWT), rate limiting, and production logging
- Implement Travel Rule where applicable
- Build mobile/web client to consume this API
```