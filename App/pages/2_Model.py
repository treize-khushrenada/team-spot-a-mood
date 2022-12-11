import os
import streamlit as st
from PIL import Image

path = os.path.dirname(__file__)

st.markdown("# Information Retrieval")
st.sidebar.markdown("# Architect")
#TODO: Methodology: your report explains how you attempted to solve the problem and justifies your methodological approach.
#TODO: Technical depth: your report demonstrates mastery of learning objectives from multiple MADS courses.
#TODO: Context: your report cites at least 3 studies, blogs, academic articles, or other sources that are relevant to your project. All references in your report are correctly formatted with a consistent citation style (such as MLA or APA).

# open image file
pipeline = Image.open(os.path.join(path,'..','assets','Spot-A-Mood-Pipeline.png'))
st.image(pipeline, caption='Information Retrieval Architecture')

with open(os.path.join(path,'model.md')) as f:
    model = f.read()
st.markdown(model) 