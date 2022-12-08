import pprint
import SpotifyUser as User

if __name__ == '__main__':

    data = User.SpotifyUser()

    while(1):
        print('\n0: Exit\n'
              '1: Setup\n'
              '2: See All Playlists\n'
              '3: See Top Songs\n'
              '4: See Top Artists\n'
              '5: See Saved Songs\n'
              '6: See Saved Albums\n'
              '7: See Followed Artists\n')

        user_input = input('Enter Selection: ')

        if user_input == '1':
            print('')
            data.setup()
        elif user_input == '2':
            print('')
            pprint.pprint(data.get_all_playlists())
        elif user_input == '3':
            print('')
            pprint.pprint(data.get_top_songs())
        elif user_input == '4':
            print('')
            pprint.pprint(data.get_top_artists())
        elif user_input == '5':
            print('')
            pprint.pprint(data.get_saved_songs())
        elif user_input == '6':
            print('')
            pprint.pprint(data.get_saved_albums())
        elif user_input == '7':
            print('')
            pprint.pprint(data.get_followed_artists())
        else:
            exit(0)