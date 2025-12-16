from pydantic import BaseModel


class GenreRead(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
