# app/core/logging_config.py
import logging
from app.core.config import settings

def configure_logging():
    if settings.ENV.lower() == "production":
        # Log to console only (stdout)
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s %(levelname)s %(message)s"
        )
    else:
        # Log to file in development only
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s %(levelname)s %(message)s",
            filename=settings.LOG_FILE_PATH,
            filemode="a"
        )