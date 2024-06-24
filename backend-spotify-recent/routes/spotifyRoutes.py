from fastapi import APIRouter
from services import spotifyAPI

router = APIRouter()

@router.get("/search/id/{artistId}")
async def getArtistById(artistId: str):
    if(artistId == False):
        return {
            'error': 'Missing field in request', "code": 400, "status": 'error/bad request'
        }
    return await spotifyAPI.getSpotifyArtistById(artistId)

@router.get("/search/name/{artistName}")
async def getElementByName(artistName: str, type: str, market: str | None = None, limit = 10, offset=0, external: str | None = None):
    if(artistName == False):
        return {
            'error': 'Missing field in request', "code": 400, "status": 'error/bad request'
        }
    return await spotifyAPI.getSpotifyElementByName(artistName, type, market, limit, offset, external)

@router.get("/user/token")
async def getSpotifyToken():
    return await spotifyAPI.getSpotifyUserToken()

@router.get("/client/token")
async def getSpotifyToken():
    return await spotifyAPI.getSpotifyClientToken()


#This is for user auth
@router.get('/code/{code}')
async def handleShopifyRedirect(code):
    return await spotifyAPI.handleShopifyToken(code)

@router.get("/callback")
async def codeHandler(code: str | None = None, error: str | None = None):
    if(error):
        return {
            'error': error, "code": 400, "status": 'error/bad request'
        }
    return await spotifyAPI.getSpotifyAccessTokenForUser(code)
