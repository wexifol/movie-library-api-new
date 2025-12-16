from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base


class Director(Base):
    __tablename__ = "directors"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    movies = relationship("Movie", back_populates="director")
