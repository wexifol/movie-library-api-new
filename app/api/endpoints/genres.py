from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.genre import GenreRead
from app.crud.genre import get_all_genres, get_genre

router = APIRouter(prefix="/genres", tags=["Genres"])


@router.get("/", response_model=List[GenreRead])
def genres(db: Session = Depends(get_db)):
    return get_all_genres(db)


@router.get("/{genre_id}", response_model=GenreRead)
def genre_detail(genre_id: int, db: Session = Depends(get_db)):
    return get_genre(db, genre_id)
