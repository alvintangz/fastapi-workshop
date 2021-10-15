# This file contains all of our settings which can be configured anytime. The reason we
# have this file is so that if we want to change something easily, we can do so without
# modifying any code. Usually, this is the place where you place secret keys, database
# credentials, etc. With Pydantic's BaseSettings, we're able to set environment
# variables and Pydantic will automatically read them into our app.
# Ref: https://fastapi.tiangolo.com/advanced/settings/#pydantic-settings

from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Notes APIs"
    PROJECT_DESCRIPTION: str = "REST APIs for a notes application."
    PROJECT_VERSION: str = "1.0.0"
    SECRET_KEY: str = "some-secret-key"

    # -- Documentation ---
    OPENAPI_URL: Optional[str] = "/openapi.json"
    SWAGGER_URL: Optional[str] = "/swagger"
    REDOC_URL: Optional[str] = "/redoc"

    # -- Database Connection ---
    SQLITE_DB_URL: str = "sqlite:///./db.sqlite3"

    # -- JWT Access Token ---
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 60


settings = Settings()
