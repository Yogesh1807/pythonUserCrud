import logging

# Log SQL queries to app.log
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    filename="app.log",
    filemode="a"
)
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

from sqlmodel import Session, create_engine
from app.config import DATABASE_URL

engine = create_engine(DATABASE_URL)  # echo=True enables SQL logging

def get_session():
    with Session(engine) as session:
        yield session
