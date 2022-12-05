# Written by Niles Gleason
# Last modified 12/5/2022
# Trine University

from ytmusicapi import YTMusic
import YTMCredentials as cred

# This class creates an object to get YouTube Music user data from
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








