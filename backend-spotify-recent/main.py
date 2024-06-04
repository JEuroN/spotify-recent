from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()

#Routes import
from routes import spotifyRoutes


app = FastAPI()

app.include_router(
    spotifyRoutes.router,
    prefix="/spotify"
  )

@app.get("/health")
async def healCheck():
    return {"status": "Im working"}