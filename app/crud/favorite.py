from sqlalchemy.orm import Session
from app.models.favorite import Favorite
from app.models.movie import Movie


def add_favorite_movie(db: Session, user_id: int, movie_id: int):
    favorite = Favorite(user_id=user_id, movie_id=movie_id)
    db.add(favorite)
    db.commit()


def remove_favorite_movie(db: Session, user_id: int, movie_id: int):
    favorite = db.query(Favorite).filter(
        Favorite.user_id == user_id,
        Favorite.movie_id == movie_id
    ).first()
    if favorite:
        db.delete(favorite)
        db.commit()


def get_favorites(db: Session, user_id: int):
    return (
        db.query(Movie)
        .join(Favorite, Favorite.movie_id == Movie.id)
        .filter(Favorite.user_id == user_id)
        .all()
    )
