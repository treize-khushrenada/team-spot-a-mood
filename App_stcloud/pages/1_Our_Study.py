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
# display images
st.image(boxplot, caption='Songs Attributes')

st.image(pairplot, caption='Attributes Pairplot') 
st.image(elbowplot, caption='Elbow Plot')
st.image(cluster, caption='Embeddings Cluster')