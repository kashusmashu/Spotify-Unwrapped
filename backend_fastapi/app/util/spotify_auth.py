from spotipy.oauth2 import SpotifyOAuth
from app.core.config import *

# SCOPE = "playlist-modify-public playlist-modify-private user-top-read user-read-recently-played"
SCOPE = "user-top-read"

sp_oauth = SpotifyOAuth(
    client_id = spotify_id,
    client_secret = spotify_secret,
    redirect_uri = redirect_uri,
    scope = SCOPE
)