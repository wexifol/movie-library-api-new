from pydantic import BaseModel


class MovieRead(BaseModel):
    id: int
    title: str
    description: str
    trailer: str
    year: int
    rating: float
    genre_id: int
    director_id: int

    class Config:
        orm_mode = True
