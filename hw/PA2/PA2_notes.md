# BM25
- ranking function used by serach engines to find out relevance of a document to a query
- features:
    - bag of words model (word order doesn't matter)
    - more nuanced than TF-IDF

formula:
$$
\text{score}(q, d) = \sum_{i=1}^{|q|} \text{IDF}(q_i) \cdot \frac{ \text{TF}(q_i, d) \cdot (k_1 + 1) }{ \text{TF}(q_i, d) + k_1 \left( 1 - b + b \cdot \frac{|d|}{\text{avgdl}} \right) }
$$

formula breakdown:
- $q_i$ is a term in the query
- $f(q_i, d)$ is the frequency of $q_i$ in document $d$, how many times $q_i$ appears in $d$
- $|D|$ is the length of document $d$ in words
- $avgdl$ is the average length of all documents in the collection
- $k_1$ and $b$ are tuning parameters, $k_1$ is typically 1.2-2.0 and $b$ is 0.75
    - $k_1$ controls term frequency scaling
    - $b$ controls length normalization, 0 means no normalization, 1 means full normalization
- $IDF(q_i)$ is the inverse document frequency of $q_i$
    - $IDF(q_i) = \log (\frac{N-n(q_i)+0.5}{n(q_i)+0.5}+1)$
    - $N$ is the total number of documents in the collection
    - $n(q_i)$ is the number of documents containing $q_i$
    - $0.5$ is a smoothing term to avoid division by zero








# BM25F