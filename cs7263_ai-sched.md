## week 1 (05/26 – 06/01): course intro & web search basics

### objectives

- nail down what “information retrieval” really means (vs. dbs)
    
- understand the basic search pipeline: user query → inverted index → ranking
    
- get hands-on with a minimal search engine
    

### resources

- **textbook**: manning, raghavan & schütze, _introduction to information retrieval_, ch 1–2
    
- **paper**: “the anatomy of a large-scale hypertextual web search engine” (sergey brin & larry page)
    

### daily breakdown

- **monday**:
    
    - read syllabus + ch 1 (what is ir?)
        
    - sketch, on paper, each component of a search system
        
    - reflect: what assumptions underlie “matching” docs to queries?
        
- **tuesday**:
    
    - read ch 2 (inverted indexes)
        
    - hand-code a tiny inverted index in python (list of docs → dict term → postings list)
        
    - exercise: for a sample corpus (3-5 docs), show the postings lists
        
- **wednesday**:
    
    - study google’s pagerank paper intro (focus on link analysis teaser)
        
    - extend your index: add simple term-frequency weighting
        
    - test tf scores on your sample corpus
        
- **thursday**:
    
    - poke around a real search api (e.g., python whoosh or elasticsearch demo)
        
    - compare results vs. your mini-engine
        
    - journal: what’s missing in your toy engine?
        
- **friday**:
    
    - group/discussion (or solo reflection): pros & cons of basic boolean vs. ranked retrieval
        
    - write a 1-page summary: “what makes web search unique?”
        

## week 2 (06/02 – 06/08): web crawling

### objectives

- see the web as a directed graph
    
- implement polite, scalable crawling
    
- handle robots.txt, url normalization, breadth-first vs. depth-first
    

### resources

- **textbook**: ch 3 (web crawling)
    
- **tutorial**: scrapy quickstart or requests+beautifulsoup primer
    
- **article**: “best practices for web crawling at scale”
    

### daily breakdown

- **monday**:
    
    - read ch 3 (crawl architecture)
        
    - diagram, from first principles, how you’d crawl a small site
        
- **tuesday**:
    
    - code a basic crawler using requests + bs4 (limit to one domain)
        
    - implement URL queue (fifo for bfs)
        
- **wednesday**:
    
    - add robots.txt parsing (python’s `urllib.robotparser`)
        
    - enforce delays (politeness) and max depth
        
    - test on a dev site (e.g., example.com)
        
- **thursday**:
    
    - swap your crawler to scrapy (or play with its spider template)
        
    - compare your code vs. scrapy’s abstractions
        
    - note: what responsibilities does the framework take off your plate?
        
- **friday**:
    
    - optional deep dive: read a research paper on focused crawling
        
    - write a short notebook on trade-offs: breadth vs. depth, politeness vs. speed
        

## week 3 (06/09 – 06/15): graph analysis

### objectives

- formalize the web as a graph (nodes = docs/urls, edges = links)
    
- understand centrality measures (pagerank, hits)
    
- practice with networkx for analysis & visualization
    

### resources

- **textbook**: ch 4 (link analysis)
    
- **library**: networkx docs (pagerank, centrality)
    
- **paper**: “hub and authority search” (kleinberg)
    

### daily breakdown

- **monday**:
    
    - read ch 4 (theory of link analysis)
        
    - from first principles, derive the pagerank update rule
        
- **tuesday**:
    
    - build a small web-graph in networkx (10–20 nodes) using your crawler’s output
        
    - compute degree, in-degree, out-degree centrality
        
- **wednesday**:
    
    - implement pagerank via networkx’s `pagerank` fn
        
    - experiment: how do teleportation α and convergence threshold affect scores?
        
- **thursday**:
    
    - read kleinberg’s hubs & authorities
        
    - run hits on your graph; compare to pagerank results
        
- **friday**:
    
    - visualize your graph with node sizes proportional to pagerank/hub score
        
    - reflect: what insights emerge from link structure?
        
# module 2
## week 4 (06/16 – 06/22): text properties & language modeling

### objectives

- treat raw text as signal: understand tokenization, normalization, morphology
    
- build a basic n-gram language model, compute probabilities, and evaluate with perplexity
    
- see how preprocessing choices ripple through your model
    

### resources

- **slides**: text properties and language modeling
    
- **video**: text preprocessing
    
- **video**: language modeling
    
- **textbook**: _Introduction to Information Retrieval_, ch 5 (language models)
    

### daily breakdown

- **monday**
    
    - skim the “text properties” section of the slides
        
    - list all text “weirdness” you spot (case, punctuation, unicode, emojis, contractions)
        
    - reflect: what assumptions do you make when you map characters → tokens?
        
- **tuesday**
    
    - watch the text-preprocessing video
        
    - hand-write (or diagram) a pipeline: raw text → clean tokens
        
    - code up functions for lowercase, punctuation removal, whitespace normalization in python
        
- **wednesday**
    
    - extend your pipeline with stop-word filtering and simple stemming/lemmatization
        
    - test on a small sample (e.g. 5 news headlines): compare token sets before/after preprocessing
        
    - journal: how might each step hurt or help downstream tasks?
        
- **thursday**
    
    - watch the language-modeling video
        
    - from first principles, derive the formula for a bigram model
        
    - code a bigram counter: dict[(w₁,w₂)] → count, plus unigram counts
        
- **friday**
    
    - implement probability estimation (with add-one smoothing) for your bigram model
        
    - compute perplexity on a held-out mini-corpus (e.g., 10 sentences)
        
    - reflect: how does smoothing affect rare vs. common bigrams?
        

## week 5 (06/23 – 06/29): indexing & query processing

### objectives

- revisit inverted index with enhancements: positional data, skip pointers
    
- understand query parsing, boolean vs. ranked execution
    
- measure trade-offs in latency and accuracy
    

### resources

- **slides**: indexing and query process
    
- **textbook**: ch 2 (indexing), ch 6 (scoring, ranking)
    
- optional article: “efficient query evaluation strategies”
    

### daily breakdown

- **monday**
    
    - read the indexing slides top-to-bottom
        
    - from first principles, design a positional index entry for each term
        
    - sketch on paper how you’d answer a phrase query (e.g. “new york times”)
        
- **tuesday**
    
    - code your inverted index to store positions (doc ID → list of positions)
        
    - ingest your mini-corpus from week 1 and build this index
        
    - verify: extract all positions for a test term
        
- **wednesday**
    
    - implement phrase-query logic: intersect posting lists and check position offsets
        
    - test on queries like “machine learning” or “data science”
        
    - journal: what’s the runtime in terms of postings length?
        
- **thursday**
    
    - add skip pointers to your postings lists
        
    - benchmark boolean query speed (with vs. without skips) on a slightly larger corpus
        
    - reflect: when do skips help, and when do they not?
        
- **friday**
    
    - implement a simple ranked retrieval: compute tf-idf scores for a query
        
    - rank docs by cosine similarity or sum of scores
        
    - visualize (print) your top 5 results for a sample query and compare to boolean hits
        
# module 3
## week 1 (06/30 – 07/06): ir evaluation fundamentals

### objectives

- cast retrieval evaluation as a measurement problem: define relevance, judgments, pooling
    
- derive and implement core metrics: precision, recall, f₁, average precision, MAP, DCG/nDCG
    
- connect retrieval eval to classification eval: confusion matrix, ROC/AUC
    

### resources

- **slides**: evaluation methods for information retrieval systems
    
- **textbook**: _Introduction to Information Retrieval_, ch 8 (evaluation)
    
- **optional article**: overview of graded relevance & nDCG
    
- **note**: module 5 (document classification) reuses these metrics—skim it early if you’re curious
    

### daily breakdown

- **monday (06/30)**
    
    - read the lecture slides top-to-bottom
        
    - list evaluation challenges: binary vs. graded relevance, pooling bias
        
    - from first principles, derive precision = |retrieved ∩ relevant| / |retrieved| and recall = |retrieved ∩ relevant| / |relevant|
        
- **tuesday**
    
    - hand-calc precision, recall, f₁ for a toy query (e.g. 10 retrieved vs. 5 true relevant)
        
    - code a confusion matrix in python (tp, fp, fn, tn) treating retrieval as binary classifier
        
    - journal: what nuances does f₁ capture that precision@k misses?
        
- **wednesday**
    
    - derive average precision (AP) from ranked list definitions
        
    - code AP and compute MAP over a mini-set of 3 queries (5 docs each)
        
    - reflect: how does MAP smooth out per-query variance vs. single-point metrics?
        
- **thursday**
    
    - from first principles, derive DCG and nDCG formulas (experiment with linear vs. exponential gain)
        
    - implement nDCG for graded relevance (e.g. 0–3) on a sample ranking
        
    - test: how does changing the discount function affect your scores?
        
- **friday**
    
    - treat a single query’s score list as classifier probabilities → compute ROC curve & AUC using sklearn
        
    - compare PR curve vs. ROC in terms of what they reveal about ranking quality
        
    - journal: when might you prefer PR over ROC and vice versa?
        
- **weekend**
    
    - catch up or deep dive: read a TREC evaluation overview
        
    - optionally skim module 5’s doc-classification slides to see eval in a new light
        
    - write a 1-page summary: “why no single metric tells the whole story :)”
        
# module 4

# module 5
