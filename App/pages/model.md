### Our Model

According to the architecture above, we gathered our data from many sources which have already been detailed on our GitHub repository README. We want to elaborate further on both our models and feature engineering here. 

With our project architecture of information retrieval from the songs database that we gathered, we were able to create embeddings of lyrics lines for each song with the pre-trained sentence-transformer model called **all-distilroberta-v1** (Hugging Face Inc., 2021), which originated from [OpenWebTextCorpus](https://skylion007.github.io/OpenWebTextCorpus/) and further fine-tuned on 1 billion sentence pairs with the objective to predict semantically similar sentences given any sentence input.

The objective of our recommender system was to suggest songs that contain *lyrics lines* that match user's input. After comparing different models such as [StarSpace](https://github.com/facebookresearch/StarSpace) (Meta Inc., 2017), we found the rationale behind **all-distilroberta-v1** highly aligned to our system's objective and could be used as our baseline model. Each sequence of lyrics line or user text input would be encoded as a 768-dimensions dense vector.

With the embeddings, we employed the `semantic_search` utility function of the  sentence_transformers library to return the resulted cosine similarities between the query embedding to the lyrics line embeddings on the vector space. The utility function worked as fitting the query input in a K-Nearest Neighbor model of lyrics line embeddings. For the purpose of our system, we defined k=100 for sufficient lyrics line results.

With the similarity results, we wanted to weigh each song's line with the higher relevance line. For example, a song might contain only 1 line with 0.99 cosine similarity towards the query embedding, but 10 other lines that are far from the query embedding in the vector space, and these 11 lines can appear in the top 100 candidates. If we calculate the song-wise similarity scores by only averaging out the line scores in the ranking algorithm, the resulting song similarity score would be low, while aggregating the scores would favor songs that have a lot of low similarity lines (e.g. a song with 10 lines that have 0.1 similarity score would score higher than the song with 1 line that has 0.99 similarity score). 

We had to emphasize the sensitivity to highly matched lyrics line. To address the issue, we reduced the importance of those lines by suppressing line scores to 50% with a cosine similarity score of less than 0.6. then we sum the score for the lines of each song. This is the resulting `song_score` in our recommendations section.

Learning that pre-trained embeddings can be used to encode not only text input, we also implemented an image search module using the same similarity matching and ranking algorithm, but with the [OpenAI CLIP Model](https://github.com/openai/CLIP) pre-tained with image and text pairs (OpenAI Inc., 2021). The main purpose of the implementation was to showcase how our recommender algorithm could be connected to different pre-trained embeddings and support media curation from various input types. Evaluation and data pipeline discussion of the model is not in our project scope. 

Knowing the fact that this pre-trained model was based on general sentence similarity purposes, we attempted to develop a domain-specific model for song lyrics in English. We discovered annotations provided by the Genius community could be a good proxy of similar text sequence with respect to the lines of the lyrics, for example:

*Lyrics: "Now I got them Steadily depressin’, low down mind-messin’ Workin’ at the carwash blues"*

*Annotation: 'He just can’t comprehend that between his attitude and his past, he might not yet be ready for white-collar work. It makes him sad. 😢')*

With these songs data, we created a pair set of lyrics and annotations for each song extracted from the Genius API, which we then used it to fine-tuned the pre-trained model. Annotations from the community were used in understanding that this will help the model expand its scope of lyrics comprehension. 

The pre-trained model is an improvement on the original BERT model. The strategy is basically to remove the Next Sentence Prediction in BERT and insead introduce a dynamic masking so that the masked token changes during each epoch which focuses the model to learn to predict intentionally hidden meanings of the text. 

Our pair set of lyrics are basically similar sentences without a label; this requires us to choose a suitable loss function that can be used with this data structure. Once we figured out the proper loss function, the fine-tuning tasks can be easily implemented assuming the right computing infrastructure is in place. We leveraged Google Colab Pro to run our fine-tuning. RoBERTa, just like BERT, requires a lot of computing resources; Colab allowed us to use GPU and High-RAM.

We expected this fine-tuned model to produce new embeddings for the same songs set as pre-trained models so that we can compare the performance of the recommendations of the two models as can be seen in the evaluation result under **Our Study** page.

Finally, to improve the usability of the recommender system, users could filter songs with respect to the valence score fetched from Spotify API; We have also stated that the tool was not developed to encourage self-harming and unethical behaviors.

## Resources
1.      Hugging Face Inc. (2021). all-distilroberta-v1. Model card from huggingface: https://huggingface.co/sentence-transformers/all-distilroberta-v1
2.      Open AI Inc. (2021). CLIP. Open AI Blog: https://openai.com/blog/clip/

