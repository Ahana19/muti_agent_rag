from backend.app.db.database import engine

from backend.app.models.user import User

from backend.app.db.database import Base


def init_db():

    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":

    init_db()

    print("Database created.")