import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "GoodSpace Data Engine"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "super-secret-key-for-goodspace-ai")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    DATA_RAW_PATH: str = "C:/Users/hp/AppData/Local/Temp/opencode/goodspace-data-engine/data/raw_tracking.csv"
    DATA_PROCESSED_PATH: str = "C:/Users/hp/AppData/Local/Temp/opencode/goodspace-data-engine/data/processed_features.parquet"
    DASHBOARD_PORT: int = 8501

    class Config:
        env_file = ".env"

settings = Settings()
