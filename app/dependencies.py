# This file contains all the dependencies that controllers in api.py depend on.
# Ref: https://fastapi.tiangolo.com/tutorial/dependencies/
# Ref: https://pyjwt.readthedocs.io/en/latest/

import jwt
from fastapi import Depends, HTTPException
from fastapi.security import APIKeyHeader
from sqlalchemy.orm import Session

from app import crud, models
from app.database import SessionLocal
from app.settings import settings

api_key_header = APIKeyHeader(name="Authorization")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(api_key_header)
) -> models.User:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
    except (jwt.ExpiredSignatureError):
        raise HTTPException(status_code=403, detail="The credentials are expired")
    except:
        raise HTTPException(status_code=403, detail="The token is invalid")

    user = crud.get_user(db, payload["id"])
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
