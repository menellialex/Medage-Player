# Written by Niles Gleason
# Last modified 12/5/2022
# Trine University

import SpotifyCredentials as creds
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# This class creates an object to get Spotify user data from
class SpotifyUser:
    def __init__(self):
        self.clientID = creds.CLIENT_ID
        self.clientSecret = creds.CLIENT_SECRET
        self.redirectUri = creds.REDIRECT_URI

        self.scope = 'playlist-read-private user-library-read user-top-read user-follow-read'
        self.ranges = ['short_term', 'medium_term', 'long_term']
        # Short term is around 4 weeks, medium term is around 6 months, and long term is since beginning of account

        self.sp = None
        self.user_id = ''
        self.authorized = False

    # This method is needed for the other methods to work
    # Separated from init() to for better control of when log-in prompt appears
    # This method will open up a page on the user's browser, prompting them to enter their Spotify credentials
    # They are then asked to enter the URL they were redirected to after entering their details
    def setup(self):
        try:
            self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=self.clientID, client_secret=self.clientSecret, redirect_uri=self.redirectUri, scope=self.scope))
        except:
            print("Setup Failed")
            return
        self.authorized = True
        self.user_id = self.sp.me()['id']

    def get_all_playlists(self):
        # Returns an array of 2D lists representing each of the user's playlists (a 3D list)
        # Every 2D playlist list is built of lists containing a song's metadata
        # Playlist info lists structure
        # [0] = Playlist name, [1] = Number of songs in playlist, [2] = Description, [3] = Link to playlist's cover image
        # Song lists structure
        # [0] = Song Name, [1] = Artist, [2] = Album Name, [3] = Popularity Number
        # Format of returned list is:
        # [ [[playlistData1 list], [songData1 list], [songData2 list], ...], [[playlistData2 list], [songData1 list], [songData2 list], ...]  ]

        all_playlists_list = []
        
        try:
            playlists = self.sp.current_user_playlists()
        except:
            return "no"

        for playlist in playlists['items']:
            if playlist['owner']['id'] == self.user_id:
                this_playlist_list = []

                # Create and append list of information about playlist to index[0]
                playlist_info_list = []
                playlist_info_list.append(playlist['name'])
                playlist_info_list.append(playlist['tracks']['total'])
                try:
                    playlist_info_list.append(playlist['description'])
                except:
                    playlist_info_list.append('')
                try:
                    playlist_info_list.append(self.sp.playlist_cover_image(playlist['id'])[0]['url'])
                except:
                    playlist_info_list.append('')
                # Add that as first entry among playlists
                this_playlist_list.append(playlist_info_list)

                # Iterate through and append list of each song's metadata
                results = self.sp.playlist(playlist['id'], fields="tracks,next")
                tracks = results['tracks']
                this_playlist_list += self.song_metadata_to_list(tracks)

            # Append the list of playlist's contents
            all_playlists_list.append(this_playlist_list)
        return all_playlists_list

    # This method is meant to return a list containing exactly 3 lists
    # The lists contain the names of the user's top artists for the short, medium, and long terms, in that order
    # This is the only method I couldn't test myself, so it may not work as expected
    def get_top_artists(self):
        top_artists_list = []

        for sp_range in self.ranges:
            this_range_list = []
            results = self.sp.current_user_top_artists(time_range=sp_range, limit=50)
            for item in enumerate(results['items']):
                this_range_list.append(item['name'])

            top_artists_list.append(this_range_list)

        return top_artists_list

    # This method returns a list of exactly 3 2D list of the user's top songs, for short, medium, and long term, in that order
    # Each of the 3 2D song lists are in the same format as the song lists in the all playlists method
    # Format is [ [[songName, artistName, albumName, popularityValue], ...](for short term), [ ... ](medium), [ ... ](long) ]
    def get_top_songs(self):
        top_songs_list = []

        for sp_range in self.ranges:
            results = self.sp.current_user_top_tracks(time_range=sp_range, limit=50)
            songs_for_this_range = self.song_metadata_to_list_top_songs(results)
            top_songs_list.append(songs_for_this_range)

        return top_songs_list

    def get_saved_songs(self):
        try:
            raw_saved_songs = self.sp.current_user_saved_tracks()
        except:
            return "no"
        
        saved_songs_list = self.song_metadata_to_list(raw_saved_songs)
        return saved_songs_list

    # This method returns a list of the user's saved albums
    # Each saved album is represented as a list of song names, but the first item contains the album's name and artist
    # Format is [ [artistName, albumName], songName1, songName2, ... ]
    def get_saved_albums(self):
        # Make a list for all the user's albums
        saved_albums_list = []
        
        try:
            saved_albums = self.sp.current_user_saved_albums()
        except:
            return "no"

        for album in saved_albums['items']:
            # First create a list for this album's songs
            this_album_list = []

            # Then create a list for the album's info, and put it before the songs
            album_info_list = []
            album_info_list.append(album['album']['name'])
            album_info_list.append(album['album']['artists'][0]['name'])
            this_album_list.append(album_info_list)

            # Then get the names of all the songs and populate the rest of the list
            tracks = album['album']['tracks']
            this_album_list.append(self.song_names_to_list(tracks))
            while tracks['next']:
                tracks = self.sp.next(tracks)
                this_album_list.append(self.song_names_to_list(tracks))

            # Finally, add the albums list to the list of all the albums
            saved_albums_list.append(this_album_list)

        return saved_albums_list

    # This method returns a 2D list of the user's followed artists
    # Format of list is [ [artistName1,[genre1, genre2, ...]], [artistName2[genre1, genre2, ...]], ...]
    def get_followed_artists(self):
        followed_artists_list = []
        
        try:
            followed_artists = self.sp.current_user_followed_artists()
        except:
            return "no"

        for artist in enumerate(followed_artists['artists']['items']):
            this_artist = []
            this_artist.append(artist[1]['name'])
            this_artist.append(artist[1]['genres'])
            followed_artists_list.append(this_artist)

        return followed_artists_list

# Utility Functions

    # Utility function to format select song metadata into a list and return it
    def song_metadata_to_list(self, results):
        songs_list = []

        for item in enumerate(results['items']):
            song_info_list = []
            track = item[1]['track']
            song_info_list.append(track['name'])
            song_info_list.append(track['artists'][0]['name'])
            song_info_list.append(track['album']['name'])
            song_info_list.append(track['popularity'])
            songs_list.append(song_info_list)

        return songs_list

    # Utility function for the get_top_songs() method
    def song_metadata_to_list_top_songs(self, results):
        songs_list = []

        for item in enumerate(results['items']):
            song_info_list = []
            track = item[1]
            song_info_list.append(track['name'])
            song_info_list.append(track['artists'][0]['name'])
            song_info_list.append(track['album']['name'])
            song_info_list.append(track['popularity'])
            songs_list.append(song_info_list)

        return songs_list

    # Utility function for the get_saved_albums() method
    def song_names_to_list(self, results):
        songs_names_list = []

        for item in enumerate(results['items']):
            songs_names_list.append(item[1]['name'])

        return songs_names_list