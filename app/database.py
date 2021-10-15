# This file allows us to define a database session and set a base for each of the
# database models.
# Ref: https://fastapi.tiangolo.com/tutorial/sql-databases/#create-the-sqlalchemy-parts

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.settings import settings

engine = create_engine(
    settings.SQLITE_DB_URL,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()
