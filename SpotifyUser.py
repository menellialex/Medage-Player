# STILL WORK IN PROGRESS
import pprint

import SpotifyCredentials as creds
import spotipy
from spotipy.oauth2 import SpotifyOAuth

class SpotifyUser:
    def __init__(self):
        self.clientID = creds.CLIENT_ID
        self.clientSecret = creds.CLIENT_SECRET
        self.redirectUri = creds.REDIRECT_URI

        self.scope = 'playlist-read-private user-library-read user-top-read user-follow-read'
        self.ranges = ['short_term', 'medium_term', 'long_term']

        self.sp = None
        self.user_id = ''
        self.authorized = False


    def setup(self):
        # Will open up a page on the user's browser, prompting them to enter their Spotify credentials
        # They are then asked to enter the URL they were redirected to after entering their details

        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=self.clientID, client_secret=self.clientSecret, redirect_uri=self.redirectUri, scope=self.scope))
        self.authorized = True
        self.user_id = self.sp.me()['id']

    def get_all_playlists(self):
        # Returns an array of 2D arrays representing each of the user's playlists (a 3D array)
        # Every 2D playlist array is built of arrays containing a song's metadata
        # Playlist info list structure
        # [0] = Playlist name, [1] = Number of songs in playlist, [2] = Description, [3] = Link to playlist's cover image
        # Song axis structure
        # [0] = Song Name, [1] = Artist, [2] = Album Name, [3] = Popularity Number

        playlists = self.sp.current_user_playlists()
        all_playlists_list = []

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
                this_playlist_list.append(playlist_info_list)

                # Iterate through and append list of each song's metadata
                results = self.sp.playlist(playlist['id'], fields="tracks,next")
                tracks = results['tracks']
                this_playlist_list.append(self.song_metadata_to_list(tracks))
                while tracks['next']:
                    tracks = self.sp.next(tracks)
                    this_playlist_list.append(self.song_metadata_to_list(tracks))

            # Append the list of playlist's contents
            all_playlists_list.append(this_playlist_list)
        return all_playlists_list

    def get_top_artists(self):
        top_artists_list = []

        for sp_range in self.ranges:
            this_range_list = []
            results = self.sp.current_user_top_artists(time_range=sp_range, limit=50)
            for item in enumerate(results['items']):
                this_range_list.append(item['name'])

            top_artists_list.append(this_range_list)

        return top_artists_list

    def get_top_songs(self):
        top_songs_list = []
        #pprint.pprint(self.sp.current_user_top_tracks(time_range='short_term', limit=50))
        for sp_range in self.ranges:
            print("range:", sp_range)
            results = self.sp.current_user_top_tracks(time_range=sp_range, limit=50)
            top_songs_list = self.song_metadata_to_list(results)
            # for item in enumerate(results['items']):
            #    top_songs_list.append(self.song_to_list(results))
            #    print(i, item['name'], '//', item['artists'][0]['name'])
            return top_songs_list

    def get_saved_songs(self):
        saved_songs_list = []

        results = self.sp.current_user_saved_tracks()

        saved_songs_list.append(self.song_metadata_to_list(results))

        while results['next']:
            results = self.sp.next(results)
            saved_songs_list.append(self.song_metadata_to_list(results))

        return saved_songs_list

    def get_saved_albums(self):
        # Make a list for all of the user's albums
        saved_albums_list = []

        saved_albums = self.sp.current_user_saved_albums()

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

        return this_album_list


    def get_followed_artists(self):
        followed_artists_list = []

        followed_artists = self.sp.current_user_followed_artists()
        for artist in enumerate(followed_artists['artists']['items']):
            followed_artists_list.append(artist[1]['name'])
            followed_artists_list.append(artist[1]['genres'])

        print(followed_artists_list)

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

    # Utility function for the get_saved_albums() function
    def song_names_to_list(self, results):
        songs_names_list = []

        for item in enumerate(results['items']):
            songs_names_list.append(item[1]['name'])

        return songs_names_list