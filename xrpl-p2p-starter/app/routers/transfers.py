from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import get_db
from ..schemas import TransferCreate, TransferStatus
from ..models import Transfer
from ..services.xrpl_service import xrpl_service
from ..services.quote_engine import gen_id

router = APIRouter(prefix="/v1/transfers", tags=["transfers"])

@router.post("", response_model=TransferStatus)
def create_transfer(body: TransferCreate, db: Session = Depends(get_db)):
    # Idempotency: reuse transfer if exists
    existing = db.query(Transfer).filter(Transfer.quote_id == body.quote_id, Transfer.user_id == body.user_id).first()
    if existing:
        return TransferStatus(id=existing.id, status=existing.status)

    tx_id = gen_id("t")
    address, memo = xrpl_service.get_deposit_account()

    transfer = Transfer(
        id=tx_id,
        user_id=body.user_id,
        from_ccy=body.payout_details.get("from_ccy","UNKNOWN"),
        to_ccy=body.payout_details.get("to_ccy","UNKNOWN"),
        amount=body.payout_details.get("amount", 0.0),
        payout_type=body.payout_details.get("payout_type", "mobile_money"),
        status="pending_deposit",
        quote_id=body.quote_id,
        route={"path": ["fiat","xrp","fiat"]},
        deposit_address=address,
        deposit_memo=memo
    )
    db.add(transfer)
    db.commit()

    return TransferStatus(id=tx_id, status="pending_deposit")

@router.get("/{transfer_id}", response_model=TransferStatus)
def get_status(transfer_id: str, db: Session = Depends(get_db)):
    t = db.query(Transfer).get(transfer_id)
    if not t:
        raise HTTPException(status_code=404, detail="Not found")
    return TransferStatus(id=t.id, status=t.status)
