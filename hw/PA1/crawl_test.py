import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, urlunparse

def get_outbound_links(url):
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
    seed_domain = urlparse(url).netloc
    
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

url = "https://nlp.stanford.edu/IR-book/information-retrieval-book.html"
discovered_urls = get_outbound_links(url)
print("\nOutbound links from seed URL (filtered, no anchors):")
for link in sorted(discovered_urls):
    print(f"- {link}")