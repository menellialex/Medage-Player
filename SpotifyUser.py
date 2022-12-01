# STILL WORK IN PROGRESS

import SpotifyCredentials as creds
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

class SpotifyUser:
    def __init__(self):
        self.clientID = creds.CLIENT_ID
        self.clientSecret = creds.CLIENT_SECRET
        self.redirectUri = creds.REDIRECT_URI

        self.sp = 0
        self.authorized = False

    def setup(self):
        # Will open up a page on the user's browser, prompting them to enter their Spotify credentials
        # They are then asked to enter the URL they were redirected to after entering their details
        scope = 'playlist-read-private user-library-read'
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=self.clientID, client_secret=self.clientSecret, redirect_uri=self.redirectUri, scope=scope))
        self.authorized = True

    def get_all_playlists(self):
        # Returns an array of 2D arrays representing each of the user's playlists (a 3D array)
        # Every 2D playlist array is built of arrays containing a song's metadata

        playlists = self.sp.current_user_playlists()
        #pprint.pprint(playlists)

        for this_playlist in playlists['items']:
            print(this_playlist['name'])
            print('  total tracks', this_playlist['tracks']['total'])

            results = self.sp.playlist(this_playlist['id'], fields="tracks,next")
            tracks = results['tracks']
            pprint.pprint(tracks)

    def get_top_artists(self):
        a = 0

    def get_top_songs(self):
        a = 0

    def get_saved_songs(self):
        a = 0

    def get_saved_albums(self):
        a = 0

    def get_liked_songs(self):
        a = 0

    def get_user_reccomendations(self):
        a = 0

    def static_song_to_array(track):
        a = 0