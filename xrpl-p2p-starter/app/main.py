from fastapi import FastAPI
from .db import Base, engine
from .routers import quotes, transfers, kyc, webhooks

Base.metadata.create_all(bind=engine)

app = FastAPI(title="XRPL P2P Starter API", version="0.1.0")

app.include_router(quotes.router)
app.include_router(transfers.router)
app.include_router(kyc.router)
app.include_router(webhooks.router)
