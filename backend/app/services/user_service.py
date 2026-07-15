from sqlalchemy.orm import Session

from backend.app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
)
from backend.app.repositories.user_repository import user_repository


class UserService:

    def create_user(
        self,
        db: Session,
        username: str,
        email: str,
        password: str
    ):

        existing_username = user_repository.get_by_username(
            db,
            username
        )

        if existing_username:
            raise ValueError("Username already exists.")

        existing_email = user_repository.get_by_email(
            db,
            email
        )

        if existing_email:
            raise ValueError("Email already exists.")

        hashed_password = hash_password(password)

        return user_repository.create_user(
            db,
            username,
            email,
            hashed_password
        )

    def get_all_users(
        self,
        db: Session
    ):
        return user_repository.get_all(db)

    def get_user(
        self,
        db: Session,
        user_id: int
    ):

        user = user_repository.get_by_id(
            db,
            user_id
        )

        if not user:
            raise ValueError("User not found.")

        return user

    def update_user(
        self,
        db: Session,
        user_id: int,
        username: str,
        email: str
    ):

        user = user_repository.get_by_id(
            db,
            user_id
        )

        if not user:
            raise ValueError("User not found.")

        return user_repository.update_user(
            db,
            user,
            username,
            email
        )

    def delete_user(
        self,
        db: Session,
        user_id: int
    ):

        user = user_repository.get_by_id(
            db,
            user_id
        )

        if not user:
            raise ValueError("User not found.")

        user_repository.delete_user(
            db,
            user
        )

    def login(
        self,
        db: Session,
        username: str,
        password: str
    ):

        user = user_repository.authenticate_user(
            db,
            username
        )

        if not user:
            raise ValueError("Invalid username or password.")

        if not verify_password(
            password,
            user.password
        ):
            raise ValueError("Invalid username or password.")

        token = create_access_token(
            {
                "sub": user.username
            }
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }


user_service = UserService()