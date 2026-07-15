from sqlalchemy.orm import Session

from backend.app.db.database import SessionLocal


def get_db():
    """
    Creates a database session.

    FastAPI automatically closes it
    after the request finishes.
    """

    db: Session = SessionLocal()

    try:
        yield db

    finally:
        db.close()