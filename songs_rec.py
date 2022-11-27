# Import packages
# Data manipulation
import re
import pickle
import math
import numpy as np
import pandas as pd
import nltk
#first time usage: download addtional packages form nltk first:
#nltk.download()
from nltk.tokenize import word_tokenize
from sentence_transformers import SentenceTransformer, util

# Ranking Generation

# Helper functions to main ranking function

# Get closest lyrics lines matches from user text input
def text_get_similar_lyrics_lines(user_text_input, embeddings, arr_lyrics_idx, model_name = "all-distilroberta-v1"):
    model = SentenceTransformer(model_name)
    input_emb = model.encode(user_text_input, convert_to_tensor=True)
    res_cos_sim = util.semantic_search(input_emb, embeddings, score_function=util.cos_sim, top_k=100)
    # Convert results and mapped lyrics id as pd dataframe
    res_df = pd.DataFrame(res_cos_sim[0])
    res_df.rename(columns = {'corpus_id':'lyrics_id'}, inplace = True)
    res_df['lyrics_line'] = arr_lyrics_idx[res_df['lyrics_id']]
    return res_df

# For invert indexing // Look up ids of corresponding songs
def lyrics_id_mapping(res_df, arr_lyrics_idx):
    arr_lyrics_id = res_df['lyrics_id'].to_numpy()
    arr_idx = arr_lyrics_id.astype(int)
    arr_song_row_idx = arr_lyrics_idx[arr_idx]
    res_df['song_idx'] = arr_song_row_idx
    return res_df

# Suppress utterances which have low similarity scores
def score_low_sim_weighting(df, threshold = 0.9, weight_low_sim = 1):
    df['score_weighted'] = df['score'].apply(lambda x: x * weight_low_sim if x < threshold else x)
    return df

# Re-rank on songs level based on average lyrics line scores
def songs_ranking(df_results_lyrics_mapped):
    res = df_results_lyrics_mapped.groupby('song_idx')['score_weighted'].mean()
    res = res.sort_values(ascending=False)
    return res

# Combine songs information to ranked songs
def combine_songs_info(s_songs_ranking, sample_artists_set, results_limit = 10):
    df_songs_candidates = sample_artists_set.filter(items = s_songs_ranking.index, axis=0)
    df_songs_candidates['score'] = s_songs_ranking
    df_songs_candidates['song_idx'] = s_songs_ranking
    res_df = df_songs_candidates[['artist', 'title', 'score']][:10]
    return res_df

# Helper function to support getting songs/ lyrics results

# Look up relevant lyrics lines an their similarity scores
def lyrics_scores_lookup(song_id, df_results_lyrics_mapped):
    res = df_results_lyrics_mapped[df_results_lyrics_mapped['song_idx'] == song_id][['lyrics_line', 'score']]
    res = res.sort_values(by=['score'], ascending=False)
    return res

# Generate output on both songs and lyrics level, as a list of dictionaries
def similar_songs_lyrics_ranked(df_results_songs, df_results_lyrics_mapped):

    result_list = []

    for song_id in df_results_songs.index:
        song_title = df_results_songs['title'].loc[song_id]
        song_artist = df_results_songs['artist'].loc[song_id]
        song_score = df_results_songs['score'].loc[song_id]
        song_id = song_id
        df_lyrics_scores = lyrics_scores_lookup(song_id, df_results_lyrics_mapped)
        d_lyrics = dict(zip(df_lyrics_scores['lyrics_line'], df_lyrics_scores['score']))
        dict_object = {"song_id": song_id, "artist":song_artist, "song title":song_title, "song_score":song_score, "lyrics_scores":d_lyrics}
        result_list.append(dict_object)
    
    return result_list

# Overall function to generate songs ranking based on lyrics lines semantic textual similarity 
def similar_songs_ranked(user_input, embeddings, sample_artists_set, lyrics_set, arr_song_idx):
    df_results_lyrics = text_get_similar_lyrics_lines(user_input, embeddings, lyrics_set)
    df_results_lyrics_mapped = lyrics_id_mapping(df_results_lyrics, arr_song_idx)
    df_results_lyrics_mapped = score_low_sim_weighting(df_results_lyrics_mapped)
    s_songs_ranking = songs_ranking(df_results_lyrics_mapped)
    df_results_songs = combine_songs_info(s_songs_ranking, sample_artists_set)
    return df_results_songs, df_results_lyrics_mapped

# Main Function to return songs/lyrics ranking 
def main(user_input, embeddings, sample_artists_set, arr_lyrics_idx, arr_song_idx):
    df_results_songs, df_results_lyrics_mapped = similar_songs_ranked(user_input, embeddings, sample_artists_set, arr_lyrics_idx, arr_song_idx)
    result = similar_songs_lyrics_ranked(df_results_songs, df_results_lyrics_mapped)
    
    return result

if __name__ == "__main__":
    main()