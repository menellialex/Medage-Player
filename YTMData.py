from ytmusicapi import YTMusic
import YTMCredentials as cred

class YTMData:
    def __init__(self):
        self.headers = cred.headersString
        self.authorized = False

    def setup(self):
        YTMusic.setup(filepath="headers_auth.json", headers_raw=self.headers)
        self.authorized = True

#Method to get song's album cover
#Method to get user playlists
#Method to get user's request headers with GUI?









