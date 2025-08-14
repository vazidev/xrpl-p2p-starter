from sqlalchemy import Column, Integer, String, Float, DateTime, JSON
from sqlalchemy.sql import func
from .db import Base

class Transfer(Base):
    __tablename__ = "transfers"
    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, index=True)
    from_ccy = Column(String, index=True)
    to_ccy = Column(String, index=True)
    amount = Column(Float)
    payout_type = Column(String)  # e.g., 'bank', 'mobile_money', 'cash'
    status = Column(String, index=True)  # created, pending_deposit, in_flight, paid_out, failed, expired
    quote_id = Column(String, index=True)
    route = Column(JSON)
    deposit_address = Column(String)
    deposit_memo = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
