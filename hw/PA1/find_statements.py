import json
import os
import re
from pathlib import Path

def find_statements_with_phrase():
    # directory containing processed pages
    processed_dir = Path("processed_pages")
    
    # pattern to match sentences containing "i need to"
    pattern = r'[^.!?]*i need to[^.!?]*[.!?]'
    
    # store all matching statements
    matching_statements = []
    
    # iterate through all json files
    for json_file in processed_dir.glob("*.json"):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
                # get the text content
                text = data.get('text', '')
                
                # find all matching statements
                matches = re.findall(pattern, text, re.IGNORECASE)
                
                # add to our collection
                matching_statements.extend(matches)
                
        except Exception as e:
            print(f"Error processing {json_file}: {e}")
    
    # print results
    print(f"\nFound {len(matching_statements)} statements containing 'i need to':\n")
    for i, statement in enumerate(matching_statements, 1):
        print(f"{i}. {statement.strip()}")

if __name__ == "__main__":
    find_statements_with_phrase() 