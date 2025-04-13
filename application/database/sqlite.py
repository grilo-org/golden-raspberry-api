from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

# session memory
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

# memory persistent
# SQLALCHEMY_DATABASE_URL = "sqlite:///./temp.db"

# create with poolclass for share conection
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False},poolclass=StaticPool)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# start database
def init():
    # create local session
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
