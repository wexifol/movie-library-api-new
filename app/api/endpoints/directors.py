from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.director import DirectorRead
from app.crud.director import get_all_directors, get_director

router = APIRouter(prefix="/directors", tags=["Directors"])


@router.get("/", response_model=List[DirectorRead])
def directors(db: Session = Depends(get_db)):
    return get_all_directors(db)


@router.get("/{director_id}", response_model=DirectorRead)
def director_detail(director_id: int, db: Session = Depends(get_db)):
    return get_director(db, director_id)
