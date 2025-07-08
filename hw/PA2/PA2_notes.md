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

practically, this means:

- the more a query word shows up in a document, the higher the score (with diminishing returns).
- longer documents don't get unfairly high scores just because they have more words.
- rare words across all documents are more important than common ones.

# TODO:

- [ ] load documents (crawled webpages) from PA1
- [ ] extract text
- [ ] preprocess
  - [ ] tokenize
  - [ ] case fold
  - [ ] remove stopwords (nltk)
  - [ ] remove punctuation & digits
  - [ ] lemmatize
- [ ] build vocabulary, create two dictionaries
  - [ ] tok2idx: word -> unique index
  - [ ] idx2tok: index -> word
- [ ] build inverted index (postings list)
  - [ ] for each term, keep list of (doc_id, frequency) pairs
- [ ] extra info for BM25
  - [ ] for each doc: store length (token number after preprocessing)
  - [ ] for whole corpus: store average doc length (avgdl)
  - [ ] for each term: store doc frequency
  - [ ] total number of docs
- [ ] save index
  - [ ] use `pickle`
- [ ] implement search agent
  - [ ] for query,
    - [ ] preprocess it
    - [ ] for each term, look up in postings list
    - [ ] for each doc in list, calculate bm25 score
    - [ ] sum up scores for all query terms per doc
    - [ ] sort docs by score, highest first
  - [ ] display doc_id, score, url, filename, maybe `head`/`tail`
- [ ] code structure
  - [ ] `Indexer.__init__` (load data, preprocess, build index)
  - [ ] `Indexer.text_preprocessing` (cleaning steps)
  - [ ] `Indexer.create_index` (build inverted index)
  - [ ] `SearchAgent.__init__` (load index)
  - [ ] `SearchAgent.query` (run search)
  - [ ] `SearchAgent.display_results` (print results)
