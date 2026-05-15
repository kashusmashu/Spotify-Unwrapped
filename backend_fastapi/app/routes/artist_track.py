from fastapi import APIRouter, Header
from app.services.spotify import get_top_artists
from app.services.lastfm import get_top_tracks

router = APIRouter()

@router.get("/top-artists-tracks")
def top_artists_tracks(authorization: str = Header(None)):

    access_token = authorization.split(" ")[1]

    artists = get_top_artists(access_token, "short_term")

    results = []

    for artist in artists:

        top_tracks = get_top_tracks(artist["name"])
        results.append({
            "artist": artist,
            "top_tracks": top_tracks
        })

    return results