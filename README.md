

# Team-Spot-A-Mood
*Arthur Cho Ka Wai, Rodolfo Layedra, Poom Khorchitmate*\
This project is a part of data science capstone project at MADS, University of Michigan

## Project Overview
This project aims to provide a new musical recommendation tool driven by semantic textual similarities between user inputs and specific lines of song lyrics, as well as, a 3D network that allows users to explore similar songs with topics on the level of the overall lyrics. Users can play with Streamlit App at [Spot-A-Mood](https://siads699-fa22-spot-a-mood.streamlit.app/) link here.

The project will rely on an information retrieval architecture to encode user input (image/ text) and song lyrics documents based on pre-trained and fine-tuned Bidirectional Encoder Representations from Transformers (BERT) models using the Sentence Transformer (Reimers, 2022) Python framework.

Our recommendation generation components and related visualizations will be interfaced through Streamlit (Streamlit Inc., 2022), an open-source app framework for Machine Learning and Data Science initiatives. The overall architecture is illustrated in the diagram below: 


## Project Architecture
*Project status* **ACTIVE**\
\
![](assets/Spot-A-Mood-Pipeline.png)
## Getting Started
To start learning more about our project with our app, run the following steps
1. Clone this repository (for help, follow this [tutorial](https://help.github.com/articles/cloning-a-repository/))
2. Raw data is being kept [here](https://drive.google.com/drive/u/0/folders/1SuxyMLJ0Y9wRp1tKfo0sMVleT8TqK2Mj)
3. Create virtualenv  then run `pip install -r requirements.txt`
4. To start the streamlit app run `streamlit run app.py`

## blog post outline:
1. motivation and overview: Improve media curation experience with semantically sensitive recommendation algorithms
2. recommender system: input/output relationships and ranking algorithm/ any related models and data
3. content affinity representation: semantic textual similarity/ nlp algorithms/ any related models and data
4. tooling: from notebook to an interactive tool/ any related technologies and services

## Generating similarity:

- lyrics can be a large input sequence (https://www.sbert.net/examples/applications/computing-embeddings/README.html#input-sequence-length) - should consider per line of per verse(https://huggingface.co/blog/playlist-generator#sentence-transformers-embeddings-and-semantic-search)

## Fine-tune model

Degrees of similarity for lyrics data
- lyrics text in the same song to have high similarity
- lyrics text in the same verse should have high similarity
- annotation text and the respective lyrics text portion should have high similarity
- lyrics text with same artist/ same song-writer to have high similarity

## Resources

1.     	Lamere, P. (2022, Jun 26). Spotipy. From Read the Docs: https://spotipy.readthedocs.io/en/2.21.0/
2.  	Markelle Kelly, K. M. (2021, Feb). An Exploration of BERT for Song Classification and. From kaimalloy: https://kaimalloy.com/172B_Project.pdf
3.  	Michael Fell, E. C. (2020, Mar 15). Cornell University. From Arxiv: https://arxiv.org/abs/1912.02477
4.  	Miller, J. W. (2020). lyrics genius. From Read the Docs: https://lyricsgenius.readthedocs.io/en/master/
5.  	Reimers, N. (2022). Sbert.net. From Sentence-Transformer: https://www.sbert.net/docs/publications.html
6.  	Streamlit Inc. (2022). Streamlit. From Streamlit Documentation: https://docs.streamlit.io/
7.  	Yinhan Liu, M. O. (2019, Jul 26). RoBERTa: A Robustly Optimized BERT Pretraining Approach. From Arxiv: https://arxiv.org/abs/1907.11692
8.      Briggs, J. (2021). NLP similarity metrics | towards data science. Similarity Metrics in NLP, from https://towardsdatascience.com/similarity-metrics-in-nlp-acc0777e234c
