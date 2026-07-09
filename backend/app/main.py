from fastapi import FastAPI

from backend.app.core.config import settings
from backend.app.api.v1.health import router as health_router
from backend.app.core.logger import logger

logger.info("Starting Enterprise Multi-Agent RAG Platform")
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
)

app.include_router(health_router)


@app.get("/")
def home():
    logger.info("Home endpoint called")
    return {
        "message": f"Welcome to {settings.PROJECT_NAME}"
    }