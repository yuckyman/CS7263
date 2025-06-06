import json
import re
import os
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize

# Download NLTK data if not already downloaded
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

def process_text(text):
    
    # Convert to lowercase
    text = text.lower()
    
    # Remove redundant spaces and newlines
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Remove punctuation and special characters
    text = re.sub(r'[^\w\s]', '', text)
    
    # Tokenize
    tokens = word_tokenize(text)
    
    return tokens

def test_process_crawled_page():
    """Test processing a crawled page from the crawled_pages directory"""
    # Get the first .json file from crawled_pages directory
    crawled_pages_dir = 'crawled_pages'
    json_files = [f for f in os.listdir(crawled_pages_dir) if f.endswith('.json')]
    
    if not json_files:
        print("No JSON files found in crawled_pages directory")
        return
    
    # Process the first file
    test_file = os.path.join(crawled_pages_dir, json_files[0])
    
    # Create processed_pages directory if it doesn't exist
    processed_dir = 'processed_pages'
    if not os.path.exists(processed_dir):
        os.makedirs(processed_dir)
    
    # Check if the processed file already exists
    output_file = os.path.join(processed_dir, os.path.basename(test_file))
    if os.path.exists(output_file):
        print(f"Processed file already exists: {output_file}")
        return
    
    try:
        with open(test_file, 'r', encoding='utf-8') as f:
            page_data = json.load(f)
            
        # Process the content
        if 'body' in page_data:
            processed_tokens = process_text(page_data['body'])
            
            print(f"\nProcessing results for {test_file}:")
            print(f"Original content length: {len(page_data['body'])} characters")
            print(f"Number of tokens after processing: {len(processed_tokens)}")
            print("\nFirst 20 tokens:")
            print(processed_tokens[:20])
            
            # Save processed tokens to a new JSON file
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(processed_tokens, f, indent=2)
            print(f"Processed tokens saved to {output_file}")
            
            return processed_tokens
        else:
            print(f"No 'body' field found in {test_file}")
            
    except Exception as e:
        print(f"Error processing {test_file}: {str(e)}")

if __name__ == "__main__":
    test_process_crawled_page()
