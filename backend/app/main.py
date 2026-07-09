from fastapi import FastAPI

from backend.app.core.config import settings
from backend.app.api.health import router as health_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
)

app.include_router(health_router)


@app.get("/")
def home():
    return {
        "message": f"Welcome to {settings.PROJECT_NAME}"
    }