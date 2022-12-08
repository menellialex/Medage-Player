import pprint
import SpotifyUser as User
import SpotifyData as Data

if __name__ == '__main__':

    user = User.SpotifyUser()
    data = Data.SpotifyData()

    while(1):
        print('\n0: Exit\n'
              '1: Setup\n'
              '2: All Playlists\n'
              '3: Top Songs\n'
              '4: Top Artists\n'
              '5: Saved Songs\n'
              '6: Saved Albums\n'
              '7: Followed Artists\n'
              '8: Cover Art\n')

        user_input = input('Enter Selection: ')

        if user_input == '1':
            print('')
            user.setup()
        elif user_input == '2':
            print('')
            pprint.pprint(user.get_all_playlists())
        elif user_input == '3':
            print('')
            pprint.pprint(user.get_top_songs())
        elif user_input == '4':
            print('')
            pprint.pprint(user.get_top_artists())
        elif user_input == '5':
            print('')
            pprint.pprint(user.get_saved_songs())
        elif user_input == '6':
            print('')
            pprint.pprint(user.get_saved_albums())
        elif user_input == '7':
            print('')
            pprint.pprint(user.get_followed_artists())
        elif user_input == '8':
            print('')
            name = input('Enter name of song: ')
            artist = input('Enter song artist: ')
            print('')
            print(data.get_cover_art_by_song(name, artist))
        else:
            exit(0)