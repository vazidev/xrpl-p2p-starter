from fastapi import APIRouter
from ..schemas import KYCRequest

router = APIRouter(prefix="/v1/kyc", tags=["kyc"])

@router.post("/verify")
def verify_kyc(req: KYCRequest):
    # Stub: always approve tier-1
    return {"user_id": req.user_id, "tier": "TIER_1", "status": "approved"}

@router.get("/limits")
def get_limits():
    return {"tier_1": {"daily": 500, "monthly": 2000}, "tier_2": {"daily": 2000, "monthly": 10000}}
