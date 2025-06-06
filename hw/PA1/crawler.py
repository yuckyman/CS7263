# CS7263 Assignment 1
# Ian Taylor
# 2025-06-06

import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urljoin, urlparse, urlunparse
from time import sleep
import hashlib
import json
import os

class WebCrawler:
    def __init__(self):
        self.seed_url = "https://nlp.stanford.edu/IR-book/information-retrieval-book.html"
        self.visited_urls = set()
        self.discovered_urls = set()
        self.pages = []
        self.request_delay = 1  # seconds between requests
        self.output_dir = "crawled_pages"
        
        # Create output directory if it doesn't exist
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def is_url_valid(self, url):
        return url.startswith("http") and url not in self.visited_urls

    def get_url_hash(self, url):
        """Generate a hash for the URL to use as filename"""
        return hashlib.md5(url.encode()).hexdigest()

    def save_page(self, url, title, body):
        """Save page content to a JSON file"""
        # Generate filename from URL hash
        filename = f"{self.get_url_hash(url)}.json"
        filepath = os.path.join(self.output_dir, filename)
        
        # Create page data
        page_data = {
            "url": url,
            "title": title,
            "body": body
        }
        
        # Save to file
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(page_data, f, ensure_ascii=False, indent=2)
        
        # Also keep in memory
        self.pages.append(page_data)
        print(f"Saved: {filename}")

    def extract_info(self, url, title, body):
        return {"url": url, "title": title, "body": body}
    
    def get_outbound_links(self, url):
        """
        Get all outbound links from a given URL that match specific criteria:
        - Same domain as seed URL
        - Only http/https protocols
        - End with .html or .htm
        
        Args:
            url (str): The URL to scrape
            
        Returns:
            set: Set of discovered URLs (without anchors)
        """
        discovered_urls = set()
        seed_domain = urlparse(self.seed_url).netloc
        
        def normalize_url(url):
            """Remove anchor from URL"""
            parsed = urlparse(url)
            return urlunparse(parsed._replace(fragment=''))
        
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find all links
            for link in soup.find_all('a'):
                href = link.get('href')
                if href:
                    absolute_url = urljoin(url, href)
                    parsed_url = urlparse(absolute_url)
                    
                    # Check if URL matches all criteria
                    if (parsed_url.netloc == seed_domain and  # Same domain
                        parsed_url.scheme in ['http', 'https'] and  # Only http/https
                        (parsed_url.path.endswith('.html') or parsed_url.path.endswith('.htm'))):  # Correct extension
                        # Store URL without anchor
                        discovered_urls.add(normalize_url(absolute_url))
                        
        except Exception as e:
            print(f"Error scraping {url}: {str(e)}")
        
        return discovered_urls
    
    def crawl(self):
        """Crawl the web starting from the seed URL"""
        urls_to_visit = {self.seed_url}
        
        while urls_to_visit:
            current_url = urls_to_visit.pop()
            
            if current_url in self.visited_urls:
                continue

            # Check if the file already exists for this URL
            filename = f"{self.get_url_hash(current_url)}.json"
            filepath = os.path.join(self.output_dir, filename)
            if os.path.exists(filepath):
                print(f"Skipping (already saved): {current_url}")
                self.visited_urls.add(current_url)
                continue
                
            self.visited_urls.add(current_url)
            print(f"Crawling: {current_url}")
            
            try:
                # Add delay between requests
                sleep(self.request_delay)
                
                # Fetch and parse the page
                response = requests.get(current_url)
                soup = BeautifulSoup(response.text, 'html.parser')
                title = soup.title.string if soup.title else "No Title"
                body = soup.get_text()
                
                # Save the page information
                self.save_page(current_url, title, body)
                
                # Get new URLs to visit
                new_urls = self.get_outbound_links(current_url)
                urls_to_visit.update(new_urls - self.visited_urls)
                
            except Exception as e:
                print(f"Error processing {current_url}: {str(e)}")

if __name__ == "__main__":
    crawler = WebCrawler()
    crawler.crawl()