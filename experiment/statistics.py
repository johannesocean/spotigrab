"""
Created on 2022-11-04 16:48
@author: johannes
"""
import json
from pprint import pprint
from collections import Counter


def get_data(path):
    with open(path, 'r') as fd:
        return json.load(fd)


if __name__ == '__main__':
    data = get_data('data.json')
    counter = Counter(data['artists'])
    unique_artist = {artist: counter[artist] for artist in set(data['artists'])}
    popular = {a: n for a, n in unique_artist.items() if n >= 10}
    pprint(popular)
