# app/core/config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    ENV: str = os.getenv("ENV", "development")
    LOG_FILE_PATH: str = os.getenv("LOG_FILE_PATH", "app.log")
    ALLOWED_ORIGINS: list = os.getenv("ALLOWED_ORIGINS", "http://localhost").split(",")
    REDIS_HOST: str = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT: int = int(os.getenv("REDIS_PORT", 6379))

settings = Settings()