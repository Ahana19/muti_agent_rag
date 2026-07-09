from fastapi import APIRouter

from backend.app.schemas.info import ProjectInfoResponse

router = APIRouter()


@router.get(
    "/info",
    response_model=ProjectInfoResponse
)
def project_info():

    return ProjectInfoResponse(
        project="Enterprise Multi-Agent RAG Platform",
        version="1.0.0",
        status="Development"
    )