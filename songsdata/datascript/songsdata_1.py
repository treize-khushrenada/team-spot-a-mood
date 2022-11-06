import os
import json
import csv
import time
import spotipy
import lyricsgenius as lg

import numpy as np
import pandas as pd

import dotenv
from spotipy.oauth2 import SpotifyClientCredentials

df = pd.read_csv('charts.csv')
artists = sorted(set(df['artist']))


spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
genius = lg.Genius(os.environ['GENIUS_ACCESS_TOKEN'])

# get songs' lyrics from artist
def get_lyrics(artist):
    artist = genius.search_artist(artist, sort='popularity')
    songs = artist.songs
    lyrics = songs.to_dict()
    print(lyrics)
    return lyrics

# search songs name and artist for spotify uri
def get_spotify_uri(artist, song_title):

    return None


# get song features from spotify
def get_features(uri):

    return None

# get data from artist list
def get_data(artists_list):

    return None

# for artist in artists
# search songs by artist from genius
# for song in songs:
# get the lyrics
# spotipy search for song + artist to get the features
# add info in the dict
songs_list = []
for artist in artists:
    # search for artist id
    artist_info = genius.search(artist)
    artist_id = artist_info['hits'][0]['result']['primary_artist']['id']
    # get songs list
    songs = genius.artist_songs(artist_id)
    for song in songs['songs']:
        # filter only songs with that artist as a singer not composer
        if song['artist_names'] == artist:
            song_id = song['id']
            song_title = song['title']
            lyrics = genius.lyrics(song_id)
            annotation = genius.song_annotations(song_id)
            
# name = 'ed sheeran'
# track = 'bad habits'
# result = spotify.search(q= f'artist: + {name}, track: + {track}', type='artist,track')
# print(json.dumps(result, indent=4, sort_keys=False))


if __name__ == '__main__':
    artists_list = artists[2500]
    # print(artists)
    get_lyrics('drake')
    # print(df)
