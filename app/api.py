# This file contains our "controllers", where each controller is responsible for taking
# in a request and returning a response. Each controller calls on services defined in
# crud.py to do what needs to be done. Think of each controller (or function in here)
# as a manager and each manager sends out a task for worker(s) (i.e. crud function(s))
# to do and then collects all of the work done and returns the final result.

from typing import List

from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session

from app import crud, models, schemas, security
from app.dependencies import get_current_user, get_db

user_router = APIRouter(tags=["Users"])


@user_router.post("/register", response_model=schemas.User)
def register_user(
    user: schemas.UserCreate,
    db: Session = Depends(get_db),
):
    """
    Create a new user account.
    """
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@user_router.post("/login/access-token", response_model=schemas.Token)
def login_access_token(
    login_data: schemas.UserLogin,
    db: Session = Depends(get_db),
):
    """
    Get an access token, given a valid e-mail and password.
    """
    user = crud.authenticate_user(
        db, email=login_data.email, password=login_data.password
    )
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    return schemas.Token(access_token=security.create_user_access_token(user))


@user_router.get("/me", response_model=schemas.User)
def retrieve_me(
    current_user: models.User = Depends(get_current_user),
):
    """
    Retrieves information about the current user.
    """
    return current_user


# -------------------------------------------------------------------------------------

note_router = APIRouter(tags=["Notes"])


@note_router.get("/{note_id}", response_model=schemas.Note)
def retrieve_note(
    note_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    """
    Retrieve a note that the current user has access to.
    """
    db_note = crud.get_note_by_user(db, note_id=note_id, author_id=current_user.id)
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return db_note


@note_router.get("", response_model=List[schemas.Note])
def list_notes(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    """
    List notes that the current user has access to.
    """
    db_notes = crud.get_notes_by_user(db, current_user.id, skip, limit)
    return db_notes


@note_router.post("", response_model=schemas.Note)
def create_note(
    note: schemas.NoteCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    """
    Create a note.
    """
    db_note = crud.create_note(db, note, current_user.id)
    return db_note


@note_router.put("/{note_id}", response_model=schemas.Note)
def update_note(
    note_id: int,
    note: schemas.NoteUpdate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    """
    Update a note, provided an id.
    """
    db_note = crud.get_note_by_user(db, note_id, current_user.id)
    if not db_note:
        raise HTTPException(status_code=404, detail="Note not found")
    db_note = crud.update_note(db, db_note, note)
    return db_note


@note_router.delete("/{note_id}", status_code=204)
def delete_note(
    note_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    """
    Delete a note, provided an id.
    """
    db_note = crud.get_note_by_user(db, note_id, current_user.id)
    if not db_note:
        raise HTTPException(status_code=404, detail="Note not found")
    crud.delete_note(db, db_note)
    return Response(status_code=204)
