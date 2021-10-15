# This file allows us to define the properties that are exposed or consumed via the API.
# With Pydantic, we define properties for schemas via Python type annotations and then
# we use these schemas to validate data coming in or out of each API endpoint in api.py.
# If you've used other web frameworks before like Spring (a Java framework) or Django
# with the Django Rest Framework (another Python framework), this can be though of
# as the file that contains our "serializers" in a sense.
# Ref: https://fastapi.tiangolo.com/tutorial/sql-databases/#create-the-pydantic-models
# Ref: https://fastapi.tiangolo.com/features/#pydantic-features

from pydantic import BaseModel, EmailStr

from app.models import Note


# Shared properties
class UserBase(BaseModel):
    email: EmailStr


# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str


# Properties to return via API
class User(UserBase):
    id: int

    class Config:
        orm_mode = True


# Properties to recieve via API on login
class UserLogin(UserBase):
    email: EmailStr
    password: str


# Shared properties
class NoteBase(BaseModel):
    title: str
    note: str


# Properties to receive via API on creation
class NoteCreate(NoteBase):
    pass


# Properties to receive via API on update
class NoteUpdate(NoteBase):
    pass


# Properties to return via API
class Note(NoteBase):
    id: int
    author_id: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
