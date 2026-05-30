import spotipy
from app.dependencies.spotify_auth import sp_oauth
from app.dependencies.config import memory_cache

# checks if access token is valid, refreshes if necessary
def get_valid_token():

    cached = memory_cache.get_cached_token()

    if cached is None:
        raise Exception("User not logged in")

    # if token is expired, refresh automatically and return valid token_info
    token_info = sp_oauth.validate_token(cached)

    if token_info is None:
        raise Exception("Could not validate token")
    
    return spotipy.Spotify(auth = token_info["access_token"])

#gets user's top 5 spotify artists
def get_top_artists( time_range, limit=5):

    sp = get_valid_token()

    #sends api request to access user's top 5 artists w spotipy
    response = sp.current_user_top_artists(
        limit=limit,
        time_range=time_range
    )

    artists = []

    # goes through response json and returns the name, spotify id, image of every eartist
    for artist in response["items"]:
        artists.append({
            "name": artist["name"],
            "spotify_id": artist["id"],
            "image": (
                artist["images"][0]["url"]
                if artist["images"]
                else None
            )
        })

    return artists