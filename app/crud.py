# This file contains our business logic, where we have reusable functions that interact
# with data in the database. If you've used other web frameworks before like Spring
# (a Java framework), this can be though of as the file that contains our "services".
# Ref: https://fastapi.tiangolo.com/tutorial/sql-databases/#crud-security

from typing import List, Optional

from sqlalchemy.orm import Session

from app import models, schemas, security


def get_user(
    db: Session,
    user_id: int,
) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(
    db: Session,
    email: str,
) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(
    db: Session,
    user: schemas.UserCreate,
) -> models.User:
    hashed_password = security.get_password_hash(user.password)
    db_user = models.User(
        email=user.email,
        hashed_password=hashed_password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate_user(
    db: Session,
    email: str,
    password: str,
) -> Optional[models.User]:
    user = get_user_by_email(db, email)
    if not user:
        return None
    if not security.validate_password(password, user.hashed_password):
        return None
    return user


# -------------------------------------------------------------------------------------


def get_note_by_user(
    db: Session,
    note_id: int,
    author_id: int,
) -> Optional[models.Note]:
    return (
        db.query(models.Note)
        .filter(models.Note.id == note_id)
        .filter(models.Note.author_id == author_id)
        .first()
    )


def get_notes_by_user(
    db: Session,
    author_id: int,
    skip: int = 0,
    limit: int = 10,
) -> List[models.Note]:
    return (
        db.query(models.Note)
        .filter(models.Note.author_id == author_id)
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_note(
    db: Session,
    note: schemas.NoteCreate,
    user_id: int,
) -> models.Note:
    db_note = models.Note(
        title=note.title,
        note=note.note,
        author_id=user_id,
    )
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note


def update_note(
    db: Session,
    db_note: models.Note,
    note: schemas.NoteUpdate,
) -> models.Note:
    db_note.title = note.title
    db_note.note = note.note
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note


def delete_note(
    db: Session,
    db_note: models.Note,
):
    db.delete(db_note)
    db.commit()
