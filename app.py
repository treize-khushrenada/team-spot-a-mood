import streamlit as st
import joblib
import pandas as pd
import numpy as np
 
from PIL import Image
from sentence_transformers import SentenceTransformer, util

# Project title 
st.title('Spot-A-Mood Playlist Recommendation')

# Sidebar
st.sidebar.header('Explain your mood')
st.sidebar.markdown('You can adjust your mood and \
                    text query below to receive out playlist')

# Mood range
mood_range = range(0,11)
mood_number = st.sidebar.select_slider('Choose your happiness level',
    options=mood_range, value=5)
st.sidebar.write('Mood Level:', mood_number*':smile:')

# Text query
query = st.sidebar.text_input('Please put your query here', placeholder='You are looking for songs related to?')
# st.sidebar.write('')

# Main body

st.markdown('This application is using BERT Sentence Transformer to help users interpret their query and mood into songs recommendation')


# BERT Query Explaination
st.subheader("Your query vector representation via BERT")
st.markdown('This might take a couple of minutes during your first run of this model')

# SBERT Sentence Transformer
model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(query)
with st.expander("Click to See Query Vector"):
    st.write(embeddings)

# Query embedding inside the song cluster visualization
# sample pic
image = Image.open('assets/Clustering.png')
st.image(image, caption='Query embedding inside the songs clusters')

# Songs recommendation list
# sample df
st.subheader('Songs Recommendation')
df = pd.read_csv('songsdata/songsdata_0.csv')
st.dataframe(df.sample(10))