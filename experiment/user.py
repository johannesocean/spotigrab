"""
Created on 2022-11-04 15:09
@author: johannes
"""
from utils import load_env, get_username
import pprint
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_env()

username = get_username()

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace = True
user = sp.user(username)
pprint.pprint(user)
