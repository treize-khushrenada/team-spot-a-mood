import os
import sys
import json
import csv
import time
import spotipy
import lyricsgenius as lg

import numpy as np
import pandas as pd

from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials

# get environmental credentials from .env file
load_dotenv()

def get_songs_features(uri_list):
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    genius = lg.Genius(os.environ['GENIUS_ACCESS_TOKEN'])
    dict_list = []
    for uri in uri_list:
        songDict = {}
        try:
            song = spotify.track(uri)
            features = spotify.audio_features(uri)
            songDict['artist'] = song['album']['artists'][0]['name']
            songDict['title'] = song['name']
            songDict['danceability'] = features[0]['danceability']
            songDict['energy'] = features[0]['energy']
            songDict['key'] = features[0]['key']
            songDict['loudness'] = features[0]['loudness']
            songDict['mode'] = features[0]['mode']
            songDict['speechiness'] = features[0]['speechiness']
            songDict['acousticness'] = features[0]['acousticness']
            songDict['instrumentalness'] = features[0]['instrumentalness']
            songDict['liveness'] = features[0]['liveness']
            songDict['valence'] = features[0]['valence']
            songDict['tempo'] = features[0]['tempo']
            songDict['duration'] = features[0]['duration_ms']
            songDict['time_signature'] = features[0]['time_signature']
            song = genius.search_song(artist=songDict['artist'], title=songDict['title'])
            song_info = song.to_dict()
            if song_info['lyrics_state'] == 'complete':
                lyrics = song_info['lyrics']
            else:
                lyrics = None
            songDict['lyrics'] = lyrics
            song_id = song_info['id']
            song_annotation = genius.song_annotations(song_id)
            songDict['genius_id'] = song_id
            songDict['annotation'] = song_annotation

        except KeyboardInterrupt:
            print('Interrupted')
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)
        except:
            pass
        dict_list.append(songDict)
    df = pd.DataFrame.from_dict(dict_list)
    return df

if __name__ == '__main__':    
    df = pd.read_csv('../../wasabi_songs.csv', sep='\t', engine='python')
    df_chart = pd.read_csv('../../charts.csv')
    prep_df = df[(df.urlSpotify.notna())&(df.artist.isin(df_chart['artist']))]
    uri_list_data = prep_df.urlSpotify.tolist()
    start, end, step = 98500, 100000, 500
    for i in range(start, end, step):
        uri_list = uri_list_data[i: i+step]
        features_df = get_songs_features(uri_list)
        features_df.to_csv(f'../songsdata_{i}.csv', index= False, header=True)
        time.sleep(15)



