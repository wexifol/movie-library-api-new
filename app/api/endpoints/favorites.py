from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.api.dependencies import get_current_user
from app.crud.favorite import add_favorite_movie, remove_favorite_movie, get_favorites

router = APIRouter(prefix="/favorites", tags=["Favorites"])


@router.post("/movies/{movie_id}")
def add_favorite(
    movie_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    add_favorite_movie(db, current_user.id, movie_id)
    return {"detail": "Added to favorites"}


@router.delete("/movies/{movie_id}")
def remove_favorite(
    movie_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    remove_favorite_movie(db, current_user.id, movie_id)
    return {"detail": "Removed from favorites"}


@router.get("/me")
def my_favorites(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return get_favorites(db, current_user.id)
