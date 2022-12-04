

# Team-Spot-A-Mood
*Arthur Cho Ka Wai, Rodolfo Layedra, Poom Khorchitmate*\
This project is a part of data science capstone project at MADS, University of Michigan


# Table of contents

- [Table of contents](#table-of-contents)
- [Project Overview](#project-overview)
- [Project Architecture](#project-architecture)
- [Installation](#getting-started)
- [Usage](#usage)
- [Development](#development)
    - [Data Extraction and Preprocessing](#data-extraction-and-preprocessing)
    - [Information Retrieval Model](#information-retrieval-model)
    - [Fine-Tuned Model](#fine-tuned-model)
- [Contributors](#contributors)

## Project Overview
This project aims to provide a new musical recommendation tool driven by semantic textual similarities between user inputs and specific lines of song lyrics, as well as, a 3D network that allows users to explore similar songs with topics on the level of the overall lyrics. Users can play with Streamlit App at [Spot-A-Mood](https://siads699-fa22-spot-a-mood.streamlit.app/) link here.

The project will rely on an information retrieval architecture to encode user input (image/ text) and song lyrics documents based on pre-trained and fine-tuned Bidirectional Encoder Representations from Transformers (BERT) models using the Sentence Transformer (Reimers, 2022) Python framework.

Our recommendation generation components and related visualizations will be interfaced through Streamlit (Streamlit Inc., 2022), an open-source app framework for Machine Learning and Data Science initiatives. The overall architecture is illustrated in the diagram below: 


## Project Architecture
[(Back to top)](#table-of-contents)
*Project status* **ACTIVE**\
\
![](assets/Spot-A-Mood-Pipeline.png)
## Getting Started
[(Back to top)](#table-of-contents)
To start learning more about our project with our app, run the following steps
1. Clone this repository (for help, follow this [tutorial](https://help.github.com/articles/cloning-a-repository/))
2. Raw data is being kept [here](https://drive.google.com/drive/u/0/folders/1SuxyMLJ0Y9wRp1tKfo0sMVleT8TqK2Mj)
3. Create virtualenv  then run `pip install -r requirements.txt`
4. To start the streamlit app run `streamlit run app.py`

## Usage
[(Back to top)](#table-of-contents)
<!-- what the app is offering and how to use it -->
## Development
[(Back to top)](#table-of-contents)
<!-- process of development -->

### **Data Extraction and Preprocessing** 
***Dataset:***

Our team scraped song lyrics from Genius API (Miller, 2020) and song features from Spotify API (Lamere, 2022). The song list is based on the Wasabi dataset (Michael Fell, 2020), a large song corpus with metadata. We cannot directly use the Wasabi dataset, as the lyrics cannot be saved for download due to copyright issues. The available data are all trained embedding results. With a large corpus of over 2 million songs, we filtered out only songs with Spotify ID and from artists in the top 100 billboards since 1958. With the time limitation and the rate limit from APIs, we only work with 100,000 songs for our corpus of study.

***Data Cleaning:***

Our song’s lyrics are based on the Genius API which is community-curated content. Some song lyrics are extracted from a concert which contains a lot of spoken words by the singer. Some lyrics are just plain historical text. We notice that normal songs have line lengths that are not too long to fit within the song tempo, so we look for average and standard deviations of the songs’ line length and remove those that are over 2 standard deviations of the average range. 

### **Information Retrieval Model** 

***Feature Engineering and Embedding Generation:***

With our lyrics dataset, we first employed a pre-trained RoBERTa model (Yinhan Liu, 2019) through the Sentence Transformer framework to generate fixed-sized dense vectors. From the lyrics embeddings, we can then compare the transformed text query using the same model to find the embeddings’ similarity.
We will also fine-tune our model using the song lyrics and annotations from the Genius community as an attempt to generate embeddings that could have higher accuracy rates in terms of semantic similarity.

***Semantic Similarity:***

With all the embeddings generated from the models, a K-nearest neighbor model (KNN) is fit to the matrix, when a new embedding is generated from a user query, we could retrieve the top n candidates from the KNN model. We planned to use the widely-adopted cosine distance between the embeddings as the metric for semantic textual similarity  (Briggs, 2021).

***Results Ranking:***

We will incorporate compositional similarity scores in the ranked results, including overall song similarity score using average similarity from lyrics lines-user query pairs, as well as the scores of individual lines. To make the average similarity score more sensitive to sentences that are highly similar to a user query, we have made a function to penalize lines with low similarity scores.

### **Fine-Tuned Model** 

***Degrees of similarity for lyrics data***
- lyrics text in the same song to have high similarity
- lyrics text in the same verse should have high similarity
- annotation text and the respective lyrics text portion should have high similarity
- lyrics text with same artist/ same song-writer to have high similarity

## blog post outline:
1. motivation and overview: Improve media curation experience with semantically sensitive recommendation algorithms
2. recommender system: input/output relationships and ranking algorithm/ any related models and data
3. content affinity representation: semantic textual similarity/ nlp algorithms/ any related models and data
4. tooling: from notebook to an interactive tool/ any related technologies and services

## Generating similarity:

- lyrics can be a large input sequence (https://www.sbert.net/examples/applications/computing-embeddings/README.html#input-sequence-length) - should consider per line of per verse(https://huggingface.co/blog/playlist-generator#sentence-transformers-embeddings-and-semantic-search)

## Contributors
[(Back to top)](#table-of-contents)
## Resources
[(Back to top)](#table-of-contents)
1.      Lamere, P. (2022, Jun 26). Spotipy. From Read the Docs: https://spotipy.readthedocs.io/en/2.21.0/
2.  	Markelle Kelly, K. M. (2021, Feb). An Exploration of BERT for Song Classification and. From kaimalloy: https://kaimalloy.com/172B_Project.pdf
3.  	Michael Fell, E. C. (2020, Mar 15). Cornell University. From Arxiv: https://arxiv.org/abs/1912.02477
4.  	Miller, J. W. (2020). lyrics genius. From Read the Docs: https://lyricsgenius.readthedocs.io/en/master/
5.  	Reimers, N. (2022). Sbert.net. From Sentence-Transformer: https://www.sbert.net/docs/publications.html
6.  	Streamlit Inc. (2022). Streamlit. From Streamlit Documentation: https://docs.streamlit.io/
7.  	Yinhan Liu, M. O. (2019, Jul 26). RoBERTa: A Robustly Optimized BERT Pretraining Approach. From Arxiv: https://arxiv.org/abs/1907.11692
8.      Briggs, J. (2021). NLP similarity metrics | towards data science. Similarity Metrics in NLP, from https://towardsdatascience.com/similarity-metrics-in-nlp-acc0777e234c

#(pending edit): Project statement: your report explains the problem you attempted to solve at a level appropriate for a broad audience.

#(pending edit): Statement of work: your report contains a statement identifying the contributions of each team member.
Statement of work, Project statement

#(pending edit): An appendix: Show us what you left out. Create an appendix to describe any other efforts you made that did not get included in the main report. 

