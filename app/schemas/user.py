from pydantic import BaseModel, EmailStr
from typing import Optional


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    favorite_genre_id: Optional[int] = None


class UserRead(BaseModel):
    id: int
    email: EmailStr
    first_name: str
    last_name: str
    favorite_genre_id: Optional[int]

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    favorite_genre_id: Optional[int] = None


class UserChangePassword(BaseModel):
    old_password: str
    new_password: str
