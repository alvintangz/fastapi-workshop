# Python helper functions that are common to use throughout the app for security.
# Ref: https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#hash-and-verify-the-passwords
# Ref: https://pyjwt.readthedocs.io/en/latest/

from datetime import datetime, timedelta

import jwt
from passlib.context import CryptContext

from app import models
from app.settings import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def validate_password(plain_password, hashed_password) -> str:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password) -> str:
    return pwd_context.hash(password)


def create_user_access_token(user: models.User) -> str:
    expires = datetime.utcnow() + timedelta(
        minutes=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode = {"id": user.id, "email": user.email, "exp": expires}
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm="HS256")
