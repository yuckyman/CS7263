import json
import os
import re
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
import hashlib

# Download NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

# Download stopwords
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

# create hash for excluded bibliography page
def get_file_hash(url):
    return hashlib.md5(url.encode()).hexdigest()

# bibliography page to exclude
EXCLUDED_URL = "http://nlp.stanford.edu/IR-book/html/htmledition/bibliography-1.html"
EXCLUDED_HASH = get_file_hash(EXCLUDED_URL)

def process_text(text):
    # Remove HTML tags if they exist
    if '<' in text and '>' in text:
        soup = BeautifulSoup(text, 'html.parser')
        text = soup.get_text()
    
    # Convert to lowercase
    text = text.lower()
    
    # Remove redundant spaces and newlines
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Remove punctuation and special characters
    text = re.sub(r'[^\w\s]', '', text)
    
    # Tokenize
    tokens = word_tokenize(text)
    
    return tokens

def process_all_files():
    """Process all files in the crawled_pages directory and save processed tokens to processed_pages directory"""
    crawled_pages_dir = 'crawled_pages'
    processed_dir = 'processed_pages'
    
    # Create processed_pages directory if it doesn't exist
    if not os.path.exists(processed_dir):
        os.makedirs(processed_dir)
    
    # Loop through all files in crawled_pages directory
    for filename in os.listdir(crawled_pages_dir):
        if filename.endswith('.json'):
            # Skip the specific file using the hashed URL
            if filename == f"{EXCLUDED_HASH}.json":
                print(f"Skipping file: {filename} (URL: {EXCLUDED_URL})")
                continue
                
            input_file = os.path.join(crawled_pages_dir, filename)
            output_file = os.path.join(processed_dir, filename)
            
            # Skip if the processed file already exists
            if os.path.exists(output_file):
                print(f"Processed file already exists: {output_file}")
                continue
            
            try:
                with open(input_file, 'r', encoding='utf-8') as f:
                    page_data = json.load(f)
                
                # Process the content
                if 'body' in page_data:
                    processed_tokens = process_text(page_data['body'])
                    
                    print(f"\nProcessing results for {input_file}:")
                    print(f"Original content length: {len(page_data['body'])} characters")
                    print(f"Number of tokens after processing: {len(processed_tokens)}")
                    print("\nFirst 20 tokens:")
                    print(processed_tokens[:20])
                    
                    # Save processed tokens to a new JSON file
                    with open(output_file, 'w', encoding='utf-8') as f:
                        json.dump(processed_tokens, f, indent=2)
                    print(f"Processed tokens saved to {output_file}")
                else:
                    print(f"No 'body' field found in {input_file}")
                    
            except Exception as e:
                print(f"Error processing {input_file}: {str(e)}")

def compute_corpus_stats():
    """Compute and print statistical representations of the processed corpus"""
    processed_dir = 'processed_pages'
    if not os.path.exists(processed_dir):
        print("Processed pages directory does not exist.")
        return
    
    all_tokens = []
    doc_lengths = []
    doc_tokens = []
    
    # Loop through all processed files
    for filename in os.listdir(processed_dir):
        if filename.endswith('.json'):
            # Skip the specific file using the hashed URL
            if filename == f"{EXCLUDED_HASH}.json":
                print(f"Skipping file: {filename} (URL: {EXCLUDED_URL})")
                continue
                
            file_path = os.path.join(processed_dir, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    tokens = json.load(f)
                    all_tokens.extend(tokens)
                    doc_lengths.append(len(tokens))
                    doc_tokens.append(set(tokens))
            except Exception as e:
                print(f"Error reading {file_path}: {str(e)}")
    
    # Compute statistics
    total_docs = len(doc_lengths)
    total_tokens = len(all_tokens)
    unique_tokens = len(set(all_tokens))
    avg_tokens_per_doc = total_tokens / total_docs if total_docs > 0 else 0
    
    # Compute token frequency distribution
    token_freq = Counter(all_tokens)
    most_common_tokens = token_freq.most_common(30)
    
    # Compute document frequency
    doc_freq = Counter()
    for doc in doc_tokens:
        for token in doc:
            doc_freq[token] += 1
    
    # Remove stop words and compute top 30 most frequent words
    stopwords = set(nltk.corpus.stopwords.words('english'))
    filtered_tokens = [token for token in all_tokens if token not in stopwords]
    filtered_freq = Counter(filtered_tokens)
    most_common_filtered = filtered_freq.most_common(30)
    
    # Print statistics
    print("\nCorpus Statistics:")
    print(f"Total number of documents: {total_docs}")
    print(f"Total number of tokens: {total_tokens}")
    print(f"Number of unique words: {unique_tokens}")
    print(f"Average page length (in words): {avg_tokens_per_doc:.2f}")
    
    print("\nTop 30 most frequent words (with collection and document frequencies):")
    for token, freq in most_common_tokens:
        print(f"{token}, Collection Freq: {freq}, Document Freq: {doc_freq[token]}")
    
    print("\nTop 30 most frequent words after removing stop words:")
    for token, freq in most_common_filtered:
        print(f"{token}: {freq}")

if __name__ == "__main__":
    process_all_files()
    compute_corpus_stats()
