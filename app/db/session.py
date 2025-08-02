# Remove or comment out any logging.basicConfig(...) here!
import logging
# ...existing code...
# DO NOT configure logging here!

from sqlmodel import Session, create_engine
from app.config import DATABASE_URL

engine = create_engine(DATABASE_URL, echo=True)  # echo=True enables SQL logging

def get_session():
    with Session(engine) as session:
        yield session
