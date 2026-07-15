from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from backend.app.core.security import verify_token
from backend.app.db.dependencies import get_db
from backend.app.repositories.user_repository import user_repository

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/login"
)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):

    username = verify_token(token)

    if username is None:

        raise HTTPException(
            status_code=401,
            detail="Invalid authentication credentials."
        )

    user = user_repository.get_by_username(
        db,
        username
    )

    if user is None:

        raise HTTPException(
            status_code=401,
            detail="User not found."
        )

    return user