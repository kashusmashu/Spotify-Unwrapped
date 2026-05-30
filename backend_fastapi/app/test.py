import requests
import spotipy
import json
from spotipy.oauth2 import SpotifyOAuth
from dependencies.config import *

# get authorization from personal spotify account, get user display name
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id = spotify_id,
    client_secret = spotify_secret,
    redirect_uri = redirect_uri,
    scope = "playlist-read-private"
))

results = sp.me()["display_name"]
print(json.dumps(results, indent=2))


# get request to fm api, get spotify account's username
r = requests.get('http://ws.audioscrobbler.com/2.0/', params={
    'method': 'user.getinfo',
    'user': 'spotify',
    'api_key': lastfm_key,
    'format': 'json'
})
print(r.json()["user"]["name"])