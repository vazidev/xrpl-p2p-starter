from fastapi import APIRouter, Request

router = APIRouter(prefix="/v1/webhooks", tags=["webhooks"])

@router.post("/xrpl")
async def xrpl_webhook(req: Request):
    payload = await req.json()
    # TODO: match memo/tag and advance transfer status
    return {"ok": True}

@router.post("/ramp")
async def ramp_webhook(req: Request):
    payload = await req.json()
    # TODO: update payout status
    return {"ok": True}
