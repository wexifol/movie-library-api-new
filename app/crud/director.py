from sqlalchemy.orm import Session
from app.models.director import Director


def get_director(db: Session, director_id: int):
    return db.query(Director).filter(Director.id == director_id).first()


def get_all_directors(db: Session):
    return db.query(Director).all()
