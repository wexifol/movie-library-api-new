from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.movie import MovieRead
from app.crud.movie import get_movies, get_movie

router = APIRouter(prefix="/movies", tags=["Movies"])


@router.get("/", response_model=List[MovieRead])
def movies(
    page: int | None = None,
    status: str | None = None,
    db: Session = Depends(get_db)
):
    return get_movies(db, page, status)


@router.get("/{movie_id}", response_model=MovieRead)
def movie_detail(movie_id: int, db: Session = Depends(get_db)):
    movie = get_movie(db, movie_id)
    if not movie:
        raise HTTPException(status_code=404)
    return movie
