from sqlalchemy.orm import Session

from backend.app.models.user import User


class UserRepository:

    def get_by_username(
        self,
        db: Session,
        username: str
    ):
        return (
            db.query(User)
            .filter(User.username == username)
            .first()
        )

    def get_by_email(
        self,
        db: Session,
        email: str
    ):
        return (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

    def get_by_id(
        self,
        db: Session,
        user_id: int
    ):
        return (
            db.query(User)
            .filter(User.id == user_id)
            .first()
        )

    def get_all(
        self,
        db: Session
    ):
        return db.query(User).all()

    def create_user(
        self,
        db: Session,
        username: str,
        email: str,
        password: str
    ):
        user = User(
            username=username,
            email=email,
            password=password
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return user

    def update_user(
        self,
        db: Session,
        user: User,
        username: str,
        email: str
    ):
        user.username = username
        user.email = email

        db.commit()
        db.refresh(user)

        return user

    def delete_user(
        self,
        db: Session,
        user: User
    ):
        db.delete(user)
        db.commit()

    def authenticate_user(
        self,
        db: Session,
        username: str
    ):
        return (
            db.query(User)
            .filter(User.username == username)
            .first()
        )


user_repository = UserRepository()