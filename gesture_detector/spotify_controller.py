import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()
class SpotifyController:
    def __init__(self):
        # Set up Spotify OAuth authentication
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=os.getenv("SPOTIPY_CLIENT_ID"),
            client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
            redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
            scope="user-modify-playback-state,user-read-playback-state"
        ))

    def control_spotify(self, gesture):
        if gesture == "swipe_left":
            self.previous_track()
        elif gesture == "swipe_right":
            self.next_track()

    def next_track(self):
        self.sp.next_track()

    def previous_track(self):
        self.sp.previous_track()
