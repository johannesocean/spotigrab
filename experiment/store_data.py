"""
Created on 2022-11-04 15:46
@author: johannes
"""
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from utils import load_env, func_timer, get_username

load_env()
USER_NAME = get_username()

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


@func_timer
def get_playlist(list_id):
    return sp.playlist(list_id)['tracks']['items']


def get_playlist_ids():
    return [{k: pl.get(k) for k in ('id', 'name')}
            for pl in sp.user_playlists(USER_NAME)['items']]


def get_artists_from_playlist(playlist):
    _data = []
    for pl in playlist:
        _data.extend([item.get('name') for item in pl['track']['artists']])
    return _data


if __name__ == '__main__':
    ids = get_playlist_ids()
    data = {}
    for id_item in ids:
        playlist_item = get_playlist(id_item.get('id'))
        artists = get_artists_from_playlist(playlist_item)
        data.setdefault('artists', []).extend(artists)
        data.setdefault('playlists', []).extend(
            [id_item.get('name')] * len(artists)
        )

    with open('data.json', "w") as outfile:
        json.dump(data, outfile, indent=4)
