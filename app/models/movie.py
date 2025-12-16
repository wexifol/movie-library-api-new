from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    trailer = Column(String)
    year = Column(Integer)
    rating = Column(Float)

    genre_id = Column(Integer, ForeignKey("genres.id"))
    director_id = Column(Integer, ForeignKey("directors.id"))

    genre = relationship("Genre", back_populates="movies")
    director = relationship("Director", back_populates="movies")
