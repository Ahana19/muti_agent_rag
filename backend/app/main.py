from fastapi import FastAPI

from backend.app.core.config import settings
from backend.app.core.logger import logger

from backend.app.api.v1.router import api_router

# Database imports
from backend.app.db.database import Base, engine

# Import ALL models before create_all()
from backend.app.models.user import User

# Create database tables
Base.metadata.create_all(bind=engine)

logger.info("Starting Enterprise Multi-Agent RAG Platform")

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
)

app.include_router(api_router, prefix="/api/v1")


@app.get("/")
def home():
    logger.info("Home endpoint called")
    return {
        "message": f"Welcome to {settings.PROJECT_NAME}"
    }