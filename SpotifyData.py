import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import SpotifyCredentials as creds

class SpotifyData:
    def __init__(self):
        self.clientID = creds.CLIENT_ID
        self.clientSecret = creds.CLIENT_SECRET
        self.sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id = self.clientID, client_secret = self.clientSecret))
        self.authorized = True

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