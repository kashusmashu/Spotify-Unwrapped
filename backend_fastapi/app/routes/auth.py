from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from app.dependencies.spotify_auth import sp_oauth

router = APIRouter()

@router.get("/login")
def login():
    # return sp auth url, use get_authorize_url from spotipy
    auth_url = sp_oauth.get_authorize_url()

    # no redirect to url, just return to front end and redirect there
    return {"url": auth_url}

@router.get("/callback")
def callback(code: str):

    # get and store access token to use spotify api
    sp_oauth.get_access_token(code)

    # redirect back to main page
    return RedirectResponse(f"http://localhost:5173/")