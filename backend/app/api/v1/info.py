from fastapi import APIRouter

from backend.app.schemas.info import ProjectInfoResponse
from backend.app.core.logger import logger
router = APIRouter()


@router.get(
    "/info",
    response_model=ProjectInfoResponse
)
def project_info():
    logger.info("Health check endpoint called")

    return ProjectInfoResponse(
        project="Enterprise Multi-Agent RAG Platform",
        version="1.0.0",
        status="Development"
    )