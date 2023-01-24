# Written by Niles Gleason
# Last modified 12/5/2022
# Trine University

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import SpotifyCredentials as creds

# This class handles getting data from Spotify without user authentication
class SpotifyData:
    def __init__(self):
        self.clientID = creds.CLIENT_ID
        self.clientSecret = creds.CLIENT_SECRET
        self.sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id = self.clientID, client_secret = self.clientSecret))
        self.authorized = True

    # This method returns a link to the cover art of a song that's passed to it
    def get_cover_art_by_song(self, name, artist):
        query = name + ' ' + artist
        result = self.sp.search(query, limit=1, type='track')

        items = result['tracks']['items']
        first_item = items[0]

        cover_image_url = first_item['album']['images'][0]['url']
        # Width and height of image are always 640

        return cover_image_url

    # Can add method for fetching cover art by album

    # Potentially add lyrics fetching method?

    def get_songs_by_artist(self, artist):
        query = artist
        result = self.sp.search(query, limit=5, type='track')

        items = result['tracks']['items']
        # first_item = items[0]

        # cover_image_url = first_item['album']['images'][0]['url']
        # # Width and height of image are always 640

        results = []

        for n in enumerate(items):
            results.append(n)

        return results
    
    def get_songs_by_album(self, album):
        query = album
        result = self.sp.search(query, limit=5, type='track')

        items = result['tracks']['items']
        # first_item = items[0]

        # cover_image_url = first_item['album']['images'][0]['url']
        # # Width and height of image are always 640

        results = []

        for n in enumerate(items):
            results.append(n)

        return results
    
    def get_songs_by_genre(self, genre):
        query = genre
        result = self.sp.search(query, limit=5, type='track')

        items = result['tracks']['items']
        # first_item = items[0]

        # cover_image_url = first_item['album']['images'][0]['url']
        # # Width and height of image are always 640

        results = []

        for n in enumerate(items):
            results.append(n)

        return results
    
    