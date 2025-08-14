from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    XRPL_NETWORK: str = "testnet"
    XRPL_RPC_URL: str | None = None
    XRPL_DEMO_SECRET: str | None = None
    BASE_CURRENCY: str = "USD"
    SLIPPAGE_BPS: int = 30
    DATABASE_URL: str = "sqlite:///./dev.db"

    class Config:
        env_file = ".env"

settings = Settings()
