import os
from services import spotifyAPI

async def setSpotifyToken():
    response = await spotifyAPI.getSpotifyClientToken()
    os.environ['SPOTIFY_API_TOKEN'] = response
