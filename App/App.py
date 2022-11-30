import streamlit as st
from st_aggrid import AgGrid, GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder

import joblib
import pickle

import pandas as pd
import numpy as np

from PIL import Image
from sentence_transformers import SentenceTransformer, util

import songs_rec

st.markdown("# Home")
st.sidebar.markdown("# Home")

# Project title 
st.title('Spot-A-Mood Playlist Recommendation')
# Sidebar
st.sidebar.header('Explain your mood')
st.sidebar.markdown('You can adjust your mood and \
                    text query below to receive out playlist')

# Mood range
#mood_range = range(0,11)
#mood_number = st.sidebar.select_slider('Choose your happiness level',
    #options=mood_range, value=5)
#st.sidebar.write('Mood Level:', mood_number*':smile:')

# valence_range
valence_range = st.sidebar.slider('Choose your happiness level',0, 10, (0, 10))

# Text query
text_input = st.sidebar.text_input('Please put your query here', placeholder='You are looking for songs related to?')
query = text_input
# Image upload
image_input = st.sidebar.file_uploader("Or upload an image", type=['.png','jpg'], accept_multiple_files=False)
if image_input is not None:
    st.sidebar.image(image_input, caption='uploaded image')
if text_input is not None:
    with open('./pickle_objects/sample_song_lyrics_set.obj', 'rb') as f:
        l_pickle = pickle.load(f)
    
    # PLEASE REFER TO preprocessing.ipynb FOR PREPROCESSING STEP
    #with open(PARENT_PATH+ '/pickle_objects/sample_song_lyrics_set.obj', 'rb') as f:
        #l_pickle = pickle.load(f)

    sample_artists_set = l_pickle[0]
    lyrics_set = l_pickle[1]

    # PLEASE REFER TO get_embeddings.ipynb FOR EMBEDDINGS GENERATION STEP
    with open('./pickle_objects/embeddings_indices.obj', 'rb') as f:
        l_pickle = pickle.load(f)

    embeddings = l_pickle[0]
    arr_song_idx = l_pickle[1] 
    arr_lyrics_idx = l_pickle[2]

    valence_min = valence_range[0]/10
    valence_max = valence_range[1]/10
            
    results = songs_rec.main(text_input, embeddings, sample_artists_set, arr_lyrics_idx, arr_song_idx, [valence_min, valence_max])

    df = pd.DataFrame(results)
    df_results = df[['song title', 'artist', 'song_score']]

#TODO @ARTHUR: logic to decide input + "search" button
#else:
    
    #df = pd.read_csv('songsdata/songsdata_0.csv')

    
# st.sidebar.write('')

# Main body

st.markdown('This application is using BERT Sentence Transformer to help users interpret their query and mood into songs recommendation')


# BERT Query Explaination
st.subheader("Your query vector representation via BERT")
st.markdown('This might take a couple of minutes during your first run of this model')

# SBERT Sentence Transformer
# model = SentenceTransformer('all-MiniLM-L6-v2')
# embeddings = model.encode(query)
# with st.expander("Click to See Query Vector"):
#     st.write(embeddings)

# Query embedding inside the song cluster visualization
# sample pic
# image = Image.open('assets/Clustering.png')
# st.image(image, caption='Query embedding inside the songs clusters')

# Songs recommendation list
col1, col2 = st.columns([2, 1])
with col1:
    st.subheader('Songs Recommendation')

    gd = GridOptionsBuilder.from_dataframe(df_results)
    gd.configure_selection(selection_mode='single', pre_selected_rows=[0], use_checkbox=False)
    gridoptions = gd.build()

    grid_table = AgGrid(df_results, height=400, width=100, gridOptions=gridoptions, update_mode=GridUpdateMode.SELECTION_CHANGED, fit_columns_on_grid_load=True)
with col2:
    st.subheader('Relevant Lyrics')
    selected_row = grid_table["selected_rows"]
    if selected_row is not None:
        
        try:
            selected_row_index = selected_row[0]['_selectedRowNodeInfo']['nodeRowIndex']
            dic_lyrics_results = df['lyrics_scores'].iloc[int(selected_row_index)]
            for key in dic_lyrics_results.keys():
                original_title = '<p style="font-size: {0}px;">{1}</p>'.format(str(48*float(dic_lyrics_results[key])), key)
                st.markdown(original_title, unsafe_allow_html=True)
        except:

            pass