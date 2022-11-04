"""
Created on 2022-11-04 15:11
@author: johannes
"""
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from utils import load_env, get_username
import pprint

load_env()

username = get_username()

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlists = sp.user_playlists(username)

for playlist in playlists['items']:
    # print(playlist['name'])
    pprint.pprint(playlist)
