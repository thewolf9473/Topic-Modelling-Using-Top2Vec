# Topic-Modelling-Using-Top2Vec


Install Requirements.txt for the required libraries.<br/>
Topic modeling is a type of statistical modeling for discovering the abstract “topics” that occur 
in a collection of documents.<br/>
<br/>
For many years, Latent Dirichlet Allocation (LDA) has been the most commonly used algorithm for topic modeling. Though problem with LDA is that it does not predict the numbers of topics by its own so we will have to set the number of topic manually which sometimes lead to ignoring minor but different topics if number of topics are not 
set precisely.<br/>
<br/>
## Top2Vec
Top2Vec is an algorithm that detects topics present in the text and generates jointly embedded topic, document, and word vectors. At a high level, the algorithm performs the following steps to discover topics in a list of documents.<br/>
  * Generate embedding vectors for documents and words.
  * Perform dimensionality reduction on the vectors using an algorithm such as UMAP.
  * Cluster the vectors using a clustering algorithm such as HDBSCAN.
  * Assign topics to each cluster.
 LDA is a generative statistical model while Top2Vec use an embedding approach.<br/>
 As Top2Vec depends on embedding approach it does not need any preprocessing and works on the original data for transformer models.<br/>
 Output are 2 csv files 
   * First CSV return the topic number with the words related to it
   * Second csv returns the document with the corresponding topic number
For further information:-https://towardsdatascience.com/how-to-perform-topic-modeling-with-top2vec-1ae9bb4e89dc
                         https://analyticsindiamag.com/how-can-the-top2vec-model-be-used-for-topic-modelling
    
