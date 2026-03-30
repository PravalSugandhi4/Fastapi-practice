from sqlite3 import SQLITE_LIMIT_COMPOUND_SELECT

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models import Base

DATABASE_URL = "postgresql://postgres:1234@localhost:5432/test"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
