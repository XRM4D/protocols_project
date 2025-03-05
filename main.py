from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
        print(db)
    finally:
        db.close()