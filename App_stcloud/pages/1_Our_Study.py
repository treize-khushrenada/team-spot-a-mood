import os

import streamlit as st
from PIL import Image

path = os.path.dirname(__file__)

st.markdown("# Spot-A-Mood")
st.sidebar.markdown("# Study Result")
#TODO: Findings and conclusions: your report interprets the outcome of your work. Numerical results are translated to insight on your problem. 
#TODO: Visuals: your report includes at least 3 original, legible, data visualizations. Visuals are explained and integrated in the body of the report.

# get image files
boxplot = Image.open(os.path.join(path,'..','assets','boxplot.png'))
pairplot = Image.open(os.path.join(path,'..','assets','pairplot.png'))
elbowplot = Image.open(os.path.join(path,'..','assets','elbow-plot.png'))
cluster = Image.open(os.path.join(path,'..','assets','cluster.png'))

# attributes
# text display from markdown files
with open(os.path.join(path,'songs_attributes.md')) as f:
    songs_attributes = f.read()
st.markdown(songs_attributes)

# display images
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        st.image(boxplot, caption='Songs Attributes')
    with col2:
        st.image(pairplot, caption='Attributes Pairplot') 

# clustering
with open(os.path.join(path,'clustering.md')) as f:
    clustering = f.read()
st.markdown(clustering)

# display images
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        st.image(elbowplot, caption='Elbow Plot')
    with col2:
        st.image(cluster, caption='Embeddings Cluster')

# results of our model evaluation
with open(os.path.join(path,'evaluation.md')) as f:
    evaluation = f.read()
st.markdown(evaluation)


