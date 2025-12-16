from sqlalchemy.orm import Session
from app.models.genre import Genre


def get_genre(db: Session, genre_id: int):
    return db.query(Genre).filter(Genre.id == genre_id).first()


def get_all_genres(db: Session):
    return db.query(Genre).all()
