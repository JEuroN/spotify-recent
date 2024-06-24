import requests
import os
import base64

from enum import Enum

apiUrl = os.environ.get('SPOTIFY_API_URL')
spotifyClientId = os.environ.get('SPOTIFY_CLIENT_ID')
spotifySecretId = os.environ.get('SPOTIFY_CLIENT_SECRET')

searchArtistType = Enum('album', 'artist', 'playlist', 'track', 'show', 'episode', 'audiobook')


async def getSpotifyArtistById(artistId):
    try:
        print()
        response = requests.get(f'{apiUrl}artists/{artistId}', headers={"Authorization": f"Bearer {os.environ['SPOTIFY_API_TOKEN']}"})
        if(response.status_code == 200):
            data = response.json()
            return {'data': data, 'status': 'ok', 'code':200}
        return {'data': response.json(), 'status': 'error', 'code': response.status_code}
    except requests.exceptions.HTTPError as error:
        return {'data': error, 'status': 'error', 'code': response.status_code}

async def getSpotifyElementByName(search: str, type: searchArtistType, market: str | None = None, limit = 10, offset=0, external: str | None = None):
    try:
        url = f'q={search}&type={type}'
        if(market):
            url += f'&market={market}'
        if(limit):
            url += f'&limit={limit}'
        if(offset):
            url += f'&offset={offset}'
        if(external):
            url += f'&include_external={external}'
    
        response = requests.get(f'{apiUrl}search?{url}', headers={"Authorization": f"Bearer {os.environ['SPOTIFY_API_TOKEN']}"})
        if(response.status_code == 200):
            data = response.json()
            return {'data': data, 'status': 'ok', 'code':200}
        return {'data': response.json(), 'status': 'error', 'code': response.status_code}
    except requests.exceptions.HTTPError as error:
        return {'data': error, 'status': 'error', 'code': response.status_code}



#This is for api calls non-user related
async def getSpotifyClientToken():
    try:
        authString = spotifyClientId + ':' + spotifySecretId
        params = {'grant_type': 'client_credentials'}
        headers = {'content-type': 'application/x-www-form-urlencoded', "Authorization": 'Basic ' + base64.b64encode(authString.encode()).decode()}
        response = requests.post('https://accounts.spotify.com/api/token', headers=headers, params=params)
        if(response.status_code == 200):
            return response.json()['access_token']
        return 'error getting token'
    except requests.exceptions.HTTPError as error:
        print('error ' + error)



#This is for user auth related token
async def getSpotifyUserToken():
    try:
        return f'https://accounts.spotify.com/authorize?client_id={spotifyClientId}&scopes=&response_type=code&redirect_uri=http://localhost:8000/spotify/callback'
    except requests.exceptions.HTTPError as error:
        print('error ' + error)

async def getSpotifyAccessTokenForUser(code):
    try:
        authString = spotifyClientId + ':' + spotifySecretId
        params = {'code': code, 'redirect_uri': 'http://localhost:8000/spotify/callback', 'grant_type': 'authorization_code'}
        headers = {'content-type': 'application/x-www-form-urlencoded', "Authorization": 'Basic ' + base64.b64encode(authString.encode()).decode()}
        response = requests.post('https://accounts.spotify.com/api/token', params=params, headers=headers)
        print(response.json())
    except requests.exceptions.HTTPError as error:
        print('error ' + error)
