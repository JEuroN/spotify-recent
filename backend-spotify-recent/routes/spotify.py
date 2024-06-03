from fastapi import APIRouter
import os
import requests

router = APIRouter()

@router.get("/")
async def root():
    print(os.environ.get('SPOTIFY_API_URL'))
    return {"message": "Hello World"}