import random, time, hashlib
from ..settings import settings

def gen_id(prefix: str) -> str:
    raw = f"{prefix}-{time.time()}-{random.random()}".encode()
    return hashlib.sha256(raw).hexdigest()[:16]

def get_quote(from_ccy: str, to_ccy: str, amount: float, payout_type: str):
    rate = 3.50 if (from_ccy, to_ccy) == ("KES","PHP") else 1.00
    fee = max(0.25, amount * 0.005)
    route = {
        "path": ["fiat", "xrp", "fiat"],
        "bridge": "XRP",
        "notes": "Demo quote only"
    }
    eta = 20  # seconds
    return {
        "quote_id": gen_id("q"),
        "rate": rate,
        "fee": round(fee, 2),
        "slippage_bps": settings.SLIPPAGE_BPS,
        "route": route,
        "eta_seconds": eta
    }
