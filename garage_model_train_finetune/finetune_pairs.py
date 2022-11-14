import os
import json
import csv
import time
import lyricsgenius as lg
import re
import numpy as np
import pandas as pd

#import credential
import requests


def lyrics_annotations_gen_id(list_genius_song_id):

    CLIENT_ACCESS_TOKEN = "xXeju4S5sFpDZOv5SAjWMwmOjcjTChruhQj6o3rK6O5ROA5mlA9MLx0Zth4S8ljG"
    genius = lg.Genius(CLIENT_ACCESS_TOKEN)
    
    l_pairs = []
    l_genius_song_idx = []


    for genius_song_id in list_genius_song_id:
        try:
            genius_song_id = int(genius_song_id)
            annotations_sample_song = genius.song_annotations(genius_song_id)
        except:
            continue
    
        for annotation_pair in annotations_sample_song:

            if annotation_pair[0] is None or len(str(annotation_pair[0])) <1 :

                continue
            
            lyrics_ref = annotation_pair[0]

            cond_empty_ref = len(lyrics_ref) <1 or lyrics_ref.isspace()
            cond_ref_chorus = re.match(r"(?i)^\[chorus\s*\d*\]$", lyrics_ref)
            cond_ref_verse = re.match(r"(?i)^\[verse\s*\d*\]$", lyrics_ref)
            
            # Ignore hanlding for "empty reference"
            if cond_empty_ref or cond_ref_chorus or cond_ref_verse:

                continue

            annotation = annotation_pair[1][0][0]
            t_pair = (lyrics_ref, annotation)
            l_pairs.append(t_pair)
            l_genius_song_idx.append(genius_song_id)

    return l_pairs, l_genius_song_idx