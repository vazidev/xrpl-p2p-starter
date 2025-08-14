from loguru import logger
from typing import Optional, Tuple
from ..settings import settings

class XRPLService:
    def __init__(self, network: str, rpc_url: Optional[str] = None):
        self.network = network
        self.rpc_url = rpc_url

    def get_deposit_account(self) -> Tuple[str, str]:
        """Return a (address, memo) for deposits. In production, generate unique memos/tags."""
        # For demo: static address and memo
        address = "rPT1Sjq2YGrBMTttX4GZHjKu9dyfzbpAYe"  # Example/test address
        memo = "DEMO-MEMO"
        logger.info(f"Provided deposit address {address} with memo {memo}")
        return address, memo

    def observe_incoming(self, memo: str) -> Optional[str]:
        """Stub: In production, poll or subscribe to XRPL and match transactions by memo/tag."""
        logger.info(f"Observing XRPL for memo/tag={memo}")
        return None  # Return tx hash when seen

xrpl_service = XRPLService(settings.XRPL_NETWORK, settings.XRPL_RPC_URL)
