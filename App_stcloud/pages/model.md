### Our Model

According to the architecture above, we gathered our data from many sources which has already been detailed on our github repository README. We want to elaborate futher on both our models and feature engineering here. 

With our project architecture of information retrieval from songs database that we gathered, we were able to create embeddings of lyrics line for each song with the pre-trained model called **"all-distilroberta-v1"**. With the embedding, we can then use semantic_search function of sentence_transformers library to return the result cosine similarity distance of the query embedding to the lyrics line embeddings on the vector space. With this cosine distance with each lyrics line, we want to weight each song's line with the higher relevance line. For example, a song might contain 2 lines that is really close to the query embedding and some other lines that are far from the query embedding. We want to reduce the important of those lines by suppressing lines with cosine similarity score less than 0.6. then we sum the score for lines of each song. This is the resulting score that we see in our recommendations section.

With these songs data we then created a pair set of embeddings and annotations for each lyrics line extracted from the Genius API, which we then used it to fine-tuned the pre-trained model. We used this Genius's website users annotation in understanding that this will help the model expand its scope of lyrics comprehension. We expected this fine-tuned model to produce new embedding for the same songs set as pre-trained models, so that we can compare the performance of the recommendations of the two models as can be seen in the evaluation result under **Our Study** page





