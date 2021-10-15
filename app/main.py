import uvicorn
from fastapi import FastAPI

from app import api, models
from app.database import engine
from app.settings import settings

models.Base.metadata.create_all(bind=engine)


app = FastAPI(
    # title=settings.PROJECT_NAME,
    # description=settings.PROJECT_DESCRIPTION,
    # version=settings.PROJECT_VERSION,
    # openapi_url=settings.OPENAPI_URL,
    # docs_url=settings.SWAGGER_URL,
    # redoc_url=settings.REDOC_URL,
)

# Starting Task: Create a controller "test", that will return the following JSON
# {"example": "This is a test"} when a user hits `GET /api/test`

# app.include_router(api.user_router, prefix="/api/users")

# app.include_router(api.note_router, prefix="/api/notes")


if __name__ == "__main__":
    uvicorn.run("app.main:app", port=8000, log_level="info", reload=True)
