# team-spot-a-mood


(some thoughts/ findings from Arthur)
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