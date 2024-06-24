from fastapi import FastAPI
from dotenv import load_dotenv
from contextlib import asynccontextmanager

load_dotenv()

#Routes import
from routes import spotifyRoutes

#Get spotify token
from services.getSpotifyToken import setSpotifyToken

@asynccontextmanager
async def lifespan(app: FastAPI):
    await setSpotifyToken()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(
    spotifyRoutes.router,
    prefix="/spotify"
  )

@app.get("/health")
async def healCheck():
    return {"status": "Im working"}