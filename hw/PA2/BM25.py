import os
import pickle
import math
import re
import json
from collections import defaultdict, Counter
from nltk.corpus import stopwords

class Indexer:
    def __init__(self, cfg):
        self.cfg = cfg
        self.index = {}
        if os.path.exists(cfg['idx_file']):
            print(f"loading index from {cfg['idx_file']}")
            with open(cfg['idx_file'], 'rb') as f:
                self.index = pickle.load(f)
        else:
            print(f"no index found; building from scratch...")
            self.create_index()
            with open(cfg['idx_file'], 'wb') as f:
                pickle.dump(self.index, f)

    def create_index(self):
        folder = self.cfg['data_dir']
        docs = []
        for fname in os.listdir(folder):
            if fname.endswith('.json'):
                with open(os.path.join(folder, fname), 'r', encoding='utf-8') as f:
                    tokens = json.load(f)
                    docs.append({'tokens': tokens, 'filename':fname})
        
        tok2idx = {}
        idx2tok = {}
        postings = defaultdict(list)
        doc_length = []
        did2fn = {}
        
        stop_words = set([w.lower() for w in stopwords.words('english')])
        
        for doc_id, doc in enumerate(docs):
            tokens = [t.lower() for t in doc['tokens'] if t.lower() not in stop_words]
            doc_length.append(len(tokens))
            did2fn[doc_id] = doc['filename']
            tf = Counter(tokens)

            for tok, freq in tf.items():
                if tok not in tok2idx:
                    idx = len(tok2idx)
                    tok2idx[tok] = idx
                    idx2tok[idx] = tok
                idx = tok2idx[tok]
                postings[idx].append((doc_id, freq))

        N = len(docs)
        avgdl = sum(doc_length) / N if N > 0 else 0
        df = {idx: len(postings[idx]) for idx in postings}

        self.index = {
            'tok2idx': tok2idx,
            'idx2tok': idx2tok,
            'postings': postings,
            'doc_length': doc_length,
            'did2fn': did2fn,
            'N': N,
            'avgdl': avgdl,
            'df': df,
            'docs': docs
        }

        print(f"index created with {len(tok2idx)} terms")
        print([w for w in list(tok2idx.keys())[:100]])


class SearchAgent:
    def __init__(self, indexer, cfg):
        self.index = indexer.index
        self.cfg = cfg
        from nltk.corpus import stopwords
        self.stop_words = set([w.lower() for w in stopwords.words('english')])

    def query(self, q_str):
        query_tokens = [t.lower() for t in q_str.split() if t.strip() not in self.stop_words]
        tok2idx = self.index['tok2idx']
        postings = self.index['postings']
        doc_scores = defaultdict(float)
        doc_length = self.index['doc_length']
        df = self.index['df']
        N = self.index['N']
        avgdl = self.index['avgdl']
        k1 = self.cfg['k1']
        b = self.cfg['b']

        for tok in query_tokens:
            if tok not in tok2idx:
                continue
            idx = tok2idx[tok]
            idf = math.log2((N - df[idx] + 0.5) / (df[idx] + 0.5))
            for doc_id, tf in postings[idx]:
                dl = doc_length[doc_id]
                denom = tf + k1 * (1 - b + b * dl / avgdl)
                score = idf * (tf * (k1 + 1)) / denom
                doc_scores[doc_id] += score
        
        ranked = sorted(doc_scores.items(), key=lambda x: x[1], reverse=True)
        results = []
        for doc_id, score in ranked:
            doc = self.index['docs'][doc_id]
            results.append({
                'doc_id': doc_id,
                'score': score,
                'filename': doc['filename'],
                'title': doc.get('title', doc['filename']),
                'snippet': ' '.join(doc['tokens'][:30])
            })
        self.display_results(results)
        return results
    
    def display_results(self, results):
        for r in results[:5]:
            print(f"DocID: {r['doc_id']}\nScore: {r['score']}\nFilename: {r['filename']}\nSnippet: {r['snippet']}\n")

CFG = {
    'idx_file': 'bm25_index.pkl',
    'data_dir': './processed_pages',
    'k1': 1.2,
    'b': 0.75
}

if __name__ == "__main__":
    i = Indexer(CFG)
    q = SearchAgent(i, CFG)
    import code
    code.interact(local=dict(globals(), **locals()))

# example usage:
# `q.query("machine learning")`
# `i.index['docs'][:5]`