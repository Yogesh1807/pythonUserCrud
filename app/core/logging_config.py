# app/core/logging_config.py
import logging
from app.core.config import settings

def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        filename=settings.LOG_FILE_PATH,
        filemode="a"
    )