from sqlalchemy import Column, Integer, String
from application.database.sqlite import Base

class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True)
    year = Column(Integer, index=True)
    title = Column(String)
    studios = Column(String)
    producers = Column(String)
    winner = Column(String)
