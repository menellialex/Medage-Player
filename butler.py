# AI Recommendation Subsystem for MeDaGe Player
# It takes in a song with metadata and fetches songs based on a priority list below of given metadata
#   Artist
#   Album
#   Year
#   Genre
# 
# This uses eyeD3 to examine music metadata. As of now, butler relies on detailed music metadata. Perhaps functionality to add data from a public repository?
# 
# This fulfills RO[27]

import eyed3
# import bulter_service
from SpotifyData import SpotifyData as sd_service

class butler:
    def __init__(self):
        # self.af
        # self.Title
        # self.Artist
        # self.Album
        # self.Genre
        pass

    def printSongInfo(self):
        print(f"Title :{self.Title}")
        print(f"Artist :{self.Artist}")
        print(f"Album :{self.Album}")
        print(f"Genre :{self.Genre}")

    def updateAF(self):
        # if self.af != None:
        self.Title = self.af.tag.title
        self.Artist = self.af.tag.artist
        self.Album = self.af.tag.album
        self.Genre = self.af.tag.genre
    
    def load(self, songdir):
        self.af = eyed3.load(songdir)
        self.updateAF()
    
    def query(self):
        # Coded for SpotifyData functions. Could potentially make more generic
        print("Songs relevant to Artist")
        query_list_artist = sd_service().get_songs_by_artist(self.Artist) # -> list format specified by service (ie, Spotify or YT Music)
        print(query_list_artist)
        print("\nSongs relevant to Album")
        query_list_album = sd_service().get_songs_by_album(self.Album)
        print(query_list_album)
        print("\nSongs relevant to Genre")
        query_list_genre = sd_service().get_songs_by_genre(self.Genre)
        print(query_list_genre)
        
if __name__ == "__main__":
    Jesse = butler()
    print("Hello and welcome to Butler! You can call me Jesse")
    # current_song_dir = input("What's the directory of the song you want me to load? ")
    Jesse.load("./Songs/sf.mp3")        # BUG/ISSUE eyed3 reports non standard names, clogs up output
    print("Here's the current song info")
    Jesse.printSongInfo()
    Jesse.query()