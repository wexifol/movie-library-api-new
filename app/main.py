from fastapi import FastAPI
from app.database import Base, engine
from app.api.endpoints import auth, users, movies, genres, directors, favorites

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Movie Library API")

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(movies.router)
app.include_router(genres.router)
app.include_router(directors.router)
app.include_router(favorites.router)
