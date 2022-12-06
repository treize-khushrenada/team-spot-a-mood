#### Songs Lyrics Clustering

Based on the data and SBERT model called **"all-distilroberta-v1"**. This model is a pretrained model based on various selection of trained model corpus. The reason that we chose this model is due to the size of the model and its performance. The model size is almost half that, 290MB, of the 1st and 2nd best performing pretrained models. Once we get the embedding of the lyrics from the sample songs that we sampled from the dataset, we then performed analysis on what is the best number of cluster using elbow plot. From the elbow plot below, we can see that the best number of cluster using the embedding of the songs is 7 clusters. We then perform the clustering on our dataset using MiniBatchKmean to help with the speed of the clustering considering the embedding size and samples.

Finally, we can observe from the results of the clustering of lyrics line that it clustered quite well which users can play with the interactive plot of the cluster on the main app screen. From this cluster, however, we discover that there are multiple lines with empty lyrics and some lines which contains the lyrics partition such as ***Chorus*** or ***Acoustic***, while some contains other songs attributes. This means we need to clean up the lyrics line much more to make sure that the cluster are only repreesenting important lyrics lines that matter. This however, do not interfere with the recommendation ranking since the ranking is based on the overall songs similarity based on all the lines in the song while suppressed scores for line that are less similar to query than the rest.