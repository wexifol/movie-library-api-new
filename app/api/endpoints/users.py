from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.user import UserRead, UserUpdate, UserChangePassword
from app.api.dependencies import get_current_user
from app.crud.user import update_user, change_password
from app.services.auth import verify_password

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/me", response_model=UserRead)
def read_me(current_user=Depends(get_current_user)):
    return current_user


@router.patch("/me", response_model=UserRead)
def update_me(
    data: UserUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return update_user(db, current_user, data.dict(exclude_unset=True))


@router.put("/me/password")
def change_my_password(
    data: UserChangePassword,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    if not verify_password(data.old_password, current_user.hashed_password):
        return {"detail": "Wrong password"}

    change_password(db, current_user, data.new_password)
    return {"detail": "Password changed"}
