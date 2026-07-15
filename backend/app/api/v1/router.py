from fastapi import APIRouter

from backend.app.api.v1.health import router as health_router
from backend.app.api.v1.info import router as info_router
from backend.app.api.v1.users import router as users_router
from backend.app.api.v1.auth import router as auth_router

api_router = APIRouter()

# Health Endpoints
api_router.include_router(health_router)

# Info Endpoints
api_router.include_router(info_router)

# User Endpoints
api_router.include_router(users_router)

# Authentication Endpoints
api_router.include_router(auth_router)