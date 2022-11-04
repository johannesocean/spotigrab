"""
Created on 2022-11-04 15:34
@author: johannes
"""
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from utils import load_env, get_username

load_env()

username = get_username()

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlist = sp.playlist('62M8W4Tc04E7BZ9P9V1yAB')

# for playlist in playlists['items']:
#     # print(playlist['name'])
#     pprint.pprint(playlist)
