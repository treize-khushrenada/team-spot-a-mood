#### Evaluation Result

The relevant score based on the recommendations for each personas can be found [HERE](https://docs.google.com/spreadsheets/d/14-rDjElKSgE7tY9WPnVKfQh8Xt4Wmcwfw1W3DnsS6SU/edit#gid=869230475)). The result shown in the table above indicated that the fine-tuned model performed worse than the pre-trained RoBerta model. Based on our limited number of songs and annotation pair of 100 songs, it is possible the lyrics might be emphasizing some semantic meanings more than others. With this small training set, it can consequently lead to overfitting of the model trying to incorporate every semantic on the lyrics and annotation pairs (Espejel, 2022). Another explanation is that the lyrics and annotation pairs from the Genius API, which is community curated content, are not necessarily imply a match in the meanings. This would cause the fine-tuned model to learn unrelated pairs of meanings which result in poor embeddings. This can somewhat been seen in the clustering of the fine-tuned model, where the query embedding is far off from the cluster.

#### Study Improvement Plan

Based on our analysis we found that we can improve the performance of the information retrieval algorithm by using a cleaner dataset. With Genius API, it is nice to have a large corpus of songs curated by various users and authors, however, some lyrics and annotation are not verifiable. Some other option for songs lyrics database is MusixMatch API which is a commercial API for songs' lyrics. For lyrics and annotation pairs, we might have to sample a larger dataset of songs and clean up more thoroughly to prevent unrelevant lyrics artifacts to mix in with the fine-tuning data.

As for the fine-tunning part, we might also have to cross validate different learning rates to prevent model from overfitting.

In summary, the songs recommended from the based pre-trained model works quite well compare to the fine-tuned ones. This could be the result of overfitting during the fine-tuning process which can be improved in the future.

#### Resources

1.      Espejel, O. (2022, August 10). Train and Fine-Tune Sentence Transformers Models. Retrieved from Hugging Face: https://huggingface.co/blog/how-to-train-sentence-transformers




