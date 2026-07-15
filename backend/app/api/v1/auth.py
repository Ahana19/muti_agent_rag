from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app.db.dependencies import get_db

from backend.app.schemas.auth import (
    RegisterRequest,
    LoginRequest,
    TokenResponse
)

from backend.app.schemas.user import UserResponse

from backend.app.services.user_service import user_service

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=201
)
def register(
    user: RegisterRequest,
    db: Session = Depends(get_db)
):

    try:

        return user_service.create_user(
            db=db,
            username=user.username,
            email=user.email,
            password=user.password
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    user: LoginRequest,
    db: Session = Depends(get_db)
):

    try:

        return user_service.login(
            db=db,
            username=user.username,
            password=user.password
        )

    except ValueError as e:

        raise HTTPException(
            status_code=401,
            detail=str(e)
        )