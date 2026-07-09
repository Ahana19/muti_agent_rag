from pydantic import BaseModel


class ProjectInfoResponse(BaseModel):
    project: str
    version: str
    status: str