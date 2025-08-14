from pydantic import BaseModel, Field
from typing import Optional, Literal, Dict, Any

class QuoteRequest(BaseModel):
    from_ccy: str = Field(..., example="KES")
    to_ccy: str = Field(..., example="PHP")
    amount: float = Field(..., gt=0)
    payout_type: Literal["bank","mobile_money","cash"] = "mobile_money"

class QuoteResponse(BaseModel):
    quote_id: str
    rate: float
    fee: float
    slippage_bps: int
    route: dict
    eta_seconds: int

class TransferCreate(BaseModel):
    idempotency_key: str
    quote_id: str
    user_id: str
    payout_details: Dict[str, Any] = {}

class TransferStatus(BaseModel):
    id: str
    status: str
    final_rate: Optional[float] = None
    fees: Optional[float] = None

class KYCRequest(BaseModel):
    user_id: str
    name: str
    country: str
    id_number: str
