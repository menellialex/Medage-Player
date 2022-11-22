import SpotifyCredentials as sc
import spotipy
from spotipy.oauth2 import SpotifyOAuth

class SpotifyData:
    def __init__(self):
        self.clientID = sc.CLIENT_ID
        self.clientSecret = sc.CLIENT_SECRET
        self.redirectUri = sc.REDIRECT_URI

        self.sp = 0
        self.authorized = False

    def setup(self):
        #Redirects browser and prompts terminal input
        scope = "user-library-read"
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=self.clientID, client_secret=self.clientSecret, redirect_uri=self.redirectUri, scope=scope))
        self.authorized = True

#Method to get song's album cover
#Method to get user playlists