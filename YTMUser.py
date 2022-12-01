from ytmusicapi import YTMusic
import YTMCredentials as cred

class YTMUser:
    def __init__(self):
        self.headers = cred.headersString
        self.authorized = False

    def setup(self):
        YTMusic.setup(filepath="headers_auth.json", headers_raw=self.headers)
        self.authorized = True

# To Do: Duplicate functionality of SpotifyUser
# Shelved for now
# But class left in for potential addition








