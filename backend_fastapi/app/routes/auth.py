from fastapi import APIRouter
from app.util.spotify_auth import sp_oauth

router = APIRouter()

@router.get('/login')
def login():
    # return sp auth url, use get_authorize_url from spotipy
    auth_url = sp_oauth.get_authorize_url()
    
    return {
        "auth_url": auth_url
    }

@router.get("/callback")
def callback(code: str):

    # return access token to use spotify api
    token_info = sp_oauth.get_access_token(code)

    return {
        "access_token": token_info["access_token"]
    }