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

class butler:
    def __init__(self):
        self.af
        self.Title
        self.Artist
        self.Album
        self.Genre

    def updateAF(self):
        if self.af != None:
            self.Title = self.af.tag.title
            self.Artist = self.af.artist
            self.Album = self.af.album
            self.Genre = self.af.genre
    
    def load(self, songdir):
        self.af = eyed3.load(songdir)
        self.updateAF()
    
    def query(self, service):
        print("Songs relevant to Artist")
        query_list_artist = service.query(self.Artist) # -> list format specified by service (ie, Spotify or YT Music)
        print(query_list_artist)
        print("\nSongs relevant to Album")
        query_list_album = service.query(self.Album)
        print(query_list_album)
        print("\nSongs relevant to Genre")
        query_list_genre = service.query(self.Genre)
        print(query_list_genre)
