import os
from dotenv import load_dotenv
from spotipy.cache_handler import MemoryCacheHandler

load_dotenv()

spotify_id = os.getenv("SPOTIFY_ID")
spotify_secret = os.getenv("SPOTIFY_SECRET")
redirect_uri = os.getenv("REDIRECT_URI")
lastfm_key = os.getenv("LASTFM_KEY")
lastfm_user = "spotify"
memory_cache = MemoryCacheHandler()