import os

import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials


load_dotenv()


def get_playlist_songs(playlist_id):
    auth_manager = SpotifyClientCredentials(
        client_id=os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
    )
    sp = spotipy.Spotify(auth_manager=auth_manager)
    playlist = sp.playlist_tracks(playlist_id)

    return [
        f"{item['track']['artists'][0]['name']} {item['track']['name']}"
        for item in playlist["items"]
    ]
