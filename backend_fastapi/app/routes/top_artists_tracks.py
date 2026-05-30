from fastapi import APIRouter
from app.services.spotify import get_top_artists
from app.services.lastfm import get_top_tracks

router = APIRouter()

@router.get("/top-artists-tracks")
def top_artists_tracks(time_range: str = "short_term"):

    artists = get_top_artists(time_range)

    results = []

    for artist in artists:
        top_tracks = get_top_tracks(artist["name"])
        results.append({
            "artist": artist,
            "top_tracks": top_tracks
        })

    return results