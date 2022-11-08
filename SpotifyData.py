import spotipy
from spotipy.oauth2 import SpotifyOAuth


class SpotifyData:
    def __init__(self):
        self.clientID = '58cd455662ae4fe39739f99bc8b684df'
        self.clientSecret = 'ab7ab15e8562406599ca21bbd55d2473'
        self.authorized = False

    def authorize(self):
        self.authorized = True
