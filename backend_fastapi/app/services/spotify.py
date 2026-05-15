import spotipy

#gets user's top 5 spotify artists
def get_top_artists(access_token, time_range, limit=5):

    sp = spotipy.Spotify(auth=access_token)

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