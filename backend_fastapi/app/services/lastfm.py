import requests
from app.util.config import lastfm_key

lastfm_url = "http://ws.audioscrobbler.com/2.0/"

def get_top_tracks(artist_name, limit=5):
    params = {
        "method": "artist.getTopTracks",
        "artist": artist_name,
        "api_key": lastfm_key,
        "format": "json",
        "limit": limit
    }

    # request top 5 tracks of artist
    response = requests.get(lastfm_url, params=params)
    data = response.json()

    tracks = []

    #return track rank, track name, # of plays of track
    for track in data["toptracks"]["track"]:
        
        tracks.append({
            "track rank": track["@attr"]["rank"],
            "name": track["name"],
            "playcount": track["playcount"]
        })


    return tracks