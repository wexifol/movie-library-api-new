from sqlalchemy.orm import Session
from app.models.movie import Movie


def get_movie(db: Session, movie_id: int):
    return db.query(Movie).filter(Movie.id == movie_id).first()


def get_movies(db: Session, page: int | None = None, status: str | None = None):
    query = db.query(Movie)

    if status == "new":
        query = query.order_by(Movie.year.desc())

    if page:
        query = query.offset((page - 1) * 12).limit(12)

    return query.all()
