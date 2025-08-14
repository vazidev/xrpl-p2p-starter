from fastapi import APIRouter
from ..schemas import QuoteRequest, QuoteResponse
from ..services.quote_engine import get_quote

router = APIRouter(prefix="/v1/quotes", tags=["quotes"])

@router.post("", response_model=QuoteResponse)
def quote(req: QuoteRequest):
    q = get_quote(req.from_ccy.upper(), req.to_ccy.upper(), req.amount, req.payout_type)
    return q
