from fastapi import FastAPI
from dotenv import load_dotenv

#Routes import
from routes import spotify

load_dotenv()

app = FastAPI()

app.include_router(
    spotify.router,
    prefix="/spotify"
  )

@app.get("/health")
async def root():
    return {"status": "Im working"}