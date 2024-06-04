from fastapi import APIRouter
from services import spotifyAPI

router = APIRouter()

@router.get("/search/id/{artistId}")
async def getArtistById(artistId):
    return await spotifyAPI.getSpotifyArtist(artistId)
    

@router.get("/user/token")
async def getSpotifyToken():
    tokenValue = await spotifyAPI.getSpotifyUserToken()
    return {"token": tokenValue}

@router.get("/client/token")
async def getSpotifyToken():
    tokenValue = await spotifyAPI.getSpotifyClientToken()
    return {"token": tokenValue}

#This is for user auth
@router.get('/code/{code}')
async def handleShopifyRedirect(code):
    await spotifyAPI.handleShopifyToken(code)
    return {"token": code}

@router.get("/callback")
async def codeHandler(code: str | None = None, error: str | None = None):
    if(error):
        return {
            'error': error
        }
    await spotifyAPI.getSpotifyAccessTokenForUser(code)
    return {
        "fino": 'hjola'
    }