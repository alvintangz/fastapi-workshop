# This file allows us to define database models. Each model corresponds to a table in
# our relational database. If you've use web frameworks that utilize the
# Model-View-Controller (MVC) architecture, this is a part of the Model portion of that
# architecture, where we define the data structures in our database.
# Ref: https://fastapi.tiangolo.com/tutorial/sql-databases/#create-the-database-models

from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    notes = relationship("Note", back_populates="author")


class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    note = Column(Text)
    author_id = Column(Integer, ForeignKey("users.id"))

    author = relationship("User", back_populates="notes")
