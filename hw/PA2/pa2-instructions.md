# Programming Assignment 2: Simple Indexer and Retriever

**Due: July 13th**

*This is an **individual** assignment. You may discuss the assignment with your classmates, but you must write your own code and submit your own work. You will be using Python to complete this assignment. *

## Overview

In this programming assignment, you will build a simple indexer and document search engine. This program will load a dataset with documents (i.e., the IR book webpages that we crawled in PA1), build an inverted-index of all documents. Given a user's input query, your search engine will retrieve relevant documents ordered by the BM25 scores.

After successfully completing this assignment. You will learn how to build a simple inverted index and how to use it to retrieve documents. You will also have better understanding of how a ranking model-based search engines work.

## Getting Started

You will use the crawled IR Book webpages from your previous assignment. In case, you were not able to complete the previous assignment, you can use the provided dataset. The dataset is a collection of
minimally processed webpages. Each file contains (1) the URL to the webpage, (2) the access time, (3) the title, and (4) the content of the webpage. The dataset is in a plain TXT file. Hence, you need to write your code to read and load the data from the provided files.

## Building a Vocabulary

The first step in building an inverted index is to create a vocabulary of all unique terms in the dataset. You will need to read each file, extract the text, and preprocess it.

### Text Preprocessing

Search engines typically perform some preprocessing on the text before indexing it. This includes:

- **Tokenization**: Splitting the text into individual words or tokens.
- **Lowercasing**: Converting all tokens to lowercase to ensure case insensitivity.
- **Stopword Removal**: Removing common words that do not carry significant meaning (e.g., "the", "is", "and").
- **Punctuation Removal**: Removing punctuation marks or special characters from the text.
- **Digit Removal**: Removing digits from the text.
- **Lemmatization**: Reducing words to their base or root form (e.g., "running" to "run").

Note that you should run the same preprocessing on the query string before searching. You can use the `nltk` library for tokenization, stopword removal, and lemmatization.

### Vocabulary Creation

One common approach to creating a vocabulary is to use two complementary dictionaries: `tok2idx` and `idx2tok`. The tok2idx dictionary maps each unique token to a unique index, while the idx2tok dictionary maps each index back to the corresponding token. This allows you to easily look up the index of a token and vice versa.

Following is an example of how to create the `tok2idx` and `idx2tok` dictionaries:

```python
from collections import defaultdict

tok2idx = defaultdict(lambda: len(tok2idx))
idx2tok = dict()

for token in tokens:
    if token not in tok2idx:
        # Assign a new index to the token
        idx2tok[self.tok2idx[token]] = token
```

## Inverted-Index Structure and Creating Postings Lists

Before you start writing your code, you need to have a good understanding of the inverted index structure. Please read the lecture slides and the textbook chapters on inverted indexes.

In essence, an inverted index is a dictionary that maps each term in the corpus to a list of documents (postings) that contain the term. Each posting may contain the document ID and the frequency of the term in that document.

So, your postings list might be structured as follows:

```python
{
    'term1': [(doc_id1, freq1), (doc_id2, freq2), ...],
    'term2': [(doc_id3, freq3), (doc_id4, freq4), ...],
    ...
}
```

## Qurying using a Ranking Model (Okapi BM25)

BM25 is a probabilistic ranking model that estimates the relevance of documents to a given query. It is widely used in information retrieval systems. The BM25 score for a document `d` with respect to a query `q` is calculated as follows:

$$
BM25(d, q) = \sum_{t \in q} IDF(t) \cdot \frac{f(t, d) \cdot (k1 + 1)}{f(t, d) + k1 \cdot \left(1 - b + b \cdot \frac{|d|}{avgdl}\right)}

$$

For an instance, you can use the following to calculate BM25 scores, given a document frequency (df) and term frequency (tf):

$$
\sum_{t \in q} \log_2 \left(\frac{N - df + 0.5}{df + 0.5}\right) \cdot \frac{tf \cdot (k1 + 1)}{tf + k1 \cdot \left(1 - b + b \cdot \frac{|d|}{avgdl}\right)}

$$

As you can see, you need to have the information of the document frequency (df) of each term in the query, the term frequency (tf) of each term in the document, the average document length (avgdl), total number of documents (N), and the length of the document (|d|) to calculate the BM25 score.

## Suggested Code Structure

### Indexer Class

This class will be responsible for reading the dataset (the crawled webpage files), creating an inverted index, and saving the index to a file (also loading it if it exists). The indexer will also be responsible for preprocessing the text.

Suggested methods are as follows:

- `__init__`: constructor to initialize the indexer and load the dataset.
- `text_preprocessing`: preprocess the text (tokenization, lemmatization, stopword removal, etc.).
- `create_index`: create the inverted index and postings lists.

The first run of the program will create the index and save it to a file. The second run and after will load the index from the file. You can use `pickle` library to save and load the index.

The index to be saved may contain the following information:

- avgdl
- vocab (tok2idx, idx2tok)
- corpus (list of documents), where you can store url, title, and content
- did2fn (document ID to filename mapping)
- postings (inverted index)

### SearchAgent Class

This class will be responsible for querying the indexer and calculating the BM25 scores. Given a query and the scoring results, it will display the results in a ranked list of documents with their scores, titles, and snippets.

Suggested methods are as follows:

- `__init__`: constructor to initialize the search agent and load the indexer.
- `query`: take a query string from a user, run the same clean_text process, calculate BM25 scores, sort the results by the scores in descending order, and display the result.
- `display_results`: display the results in a user-friendly format.

A skeleton code is provided below. You will need to fill in the details of the methods and classes.

```python
import os
import configparser
import code
from collections import defaultdict, Counter
import pickle
import math
import operator

from tqdm import tqdm
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

class Indexer:
    def __init__(self, cfg):
        raise NotImplementedError("Delete this lien and write your code here.")

    def text_preprocessing(self, text):
        raise NotImplementedError("Delete this lien and write your code here.")

    def create_index(self):
        raise NotImplementedError("Delete this lien and write your code here.")

class SearchAgent:
    def __init__(self, indexer, cfg):
        raise NotImplementedError("Delete this lien and write your code here.")

    def query(self, q_str):
        raise NotImplementedError("Delete this lien and write your code here.")

    def display_results(self, results):
        raise NotImplementedError("Delete this lien and write your code here.")


CFG = {
    'idx_file': 'irbook.idx',
    'data_dir': './data',
    'k1': 1.2,
    'b': 0.75,
}

if __name__ == "__main__":
    i = Indexer(CFG)
    q = SearchAgent(i, CFG)
    code.interact(local=dict(globals(), **locals()))
```

## Example Run

The following run shows what would happen when you run the code.

```
(ir) ➜  my-solution python se-bm25-irbook.py
Reading and processing files...
100%|█████████████████████████████████████████████████████████████████████████████████| 268/268 [00:11<00:00, 22.90it/s]
Creating postings list...
100%|███████████████████████████████████████████████████████████████████████████████| 268/268 [00:00<00:00, 3100.84it/s]
Python 3.11.10 (main, Oct 28 2024, 15:22:01) [Clang 16.0.0 (clang-1600.0.26.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> len(i.index['corpus'])
268
>>> len(i.index['tok2idx'])
5923
>>> q.query('bm25')
DocID: 22
Score: 5.391182025803886
URL: https://nlp.stanford.edu/IR-book/html/htmledition/probabilistic-information-retrieval-1.html
filename: probabilistic-information-retrieval-1.html.txt

DocID: 192
Score: 5.282126533788744
URL: https://nlp.stanford.edu/IR-book/html/htmledition/okapi-bm25-a-non-binary-model-1.html
filename: okapi-bm25-a-non-binary-model-1.html.txt

DocID: 141
Score: 5.17033813179183
URL: https://nlp.stanford.edu/IR-book/html/htmledition/tree-structured-dependencies-between-terms-1.html
filename: tree-structured-dependencies-between-terms-1.html.txt

DocID: 133
Score: 5.144611143408942
URL: https://nlp.stanford.edu/IR-book/html/htmledition/bayesian-network-approaches-to-ir-1.html
filename: bayesian-network-approaches-to-ir-1.html.txt

DocID: 105
Score: 4.811327655088995
URL: https://nlp.stanford.edu/IR-book/html/htmledition/language-modeling-versus-other-approaches-in-ir-1.html
filename: language-modeling-versus-other-approaches-in-ir-1.html.txt


>>> q.query('maximum likelihood estimation')
DocID: 209
Score: 10.568356431788068
URL: https://nlp.stanford.edu/IR-book/html/htmledition/ponte-and-crofts-experiments-1.html
filename: ponte-and-crofts-experiments-1.html.txt

DocID: 221
Score: 10.271738613511555
URL: https://nlp.stanford.edu/IR-book/html/htmledition/probability-estimates-in-theory-1.html
filename: probability-estimates-in-theory-1.html.txt

DocID: 64
Score: 9.362725412608494
URL: https://nlp.stanford.edu/IR-book/html/htmledition/estimating-the-query-generation-probability-1.html
filename: estimating-the-query-generation-probability-1.html.txt

DocID: 43
Score: 8.689562814057743
URL: http://nlp.stanford.edu/IR-book/html/htmledition/irbook.html
filename: irbook.html.txt

DocID: 168
Score: 8.586672880413573
URL: https://nlp.stanford.edu/IR-book/html/htmledition/naive-bayes-text-classification-1.html
filename: naive-bayes-text-classification-1.html.txt


>>>
```

## What to submit:

- Submit your code (a single plain Python code). Please do not submit Jupyter notebooks (Otherwise, penalty will be applied).
- 5 mins of video presentation (demo + code explanation). You can submit a link to your video (e.g., YouTube, MS Teams, etc.). Please make sure that the link is accessible to the instructor. Also uploading the video to the D2L course website is acceptable.
