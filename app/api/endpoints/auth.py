from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.user import UserCreate
from app.crud.user import create_user, authenticate_user, get_user_by_email
from app.services.auth import create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    if get_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail="Email already exists")

    new_user = create_user(
        db,
        user.email,
        user.password,
        user.first_name,
        user.last_name,
        user.favorite_genre_id
    )

    token = create_access_token({"user_id": new_user.id})
    return {"access_token": token}


@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = authenticate_user(db, email, password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    token = create_access_token({"user_id": user.id})
    return {"access_token": token}
