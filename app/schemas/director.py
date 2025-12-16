from pydantic import BaseModel


class DirectorRead(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
