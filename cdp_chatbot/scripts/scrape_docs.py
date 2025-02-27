import requests
from bs4 import BeautifulSoup
import json
import os

def scrape_docs(url, output_file):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract all text from the page
    documentation = soup.get_text(separator=' ')
    
    # Save the documentation
    os.makedirs('data/raw', exist_ok=True)
    with open(output_file, 'w') as f:
        json.dump([documentation], f)

if __name__ == '__main__':
    # Scrape documentation for all CDPs
    scrape_docs("https://segment.com/docs/?ref=nav", "data/raw/segment_docs.json")
    scrape_docs("https://docs.mparticle.com/", "data/raw/mparticle_docs.json")
    scrape_docs("https://docs.lytics.com/", "data/raw/lytics_docs.json")
    scrape_docs("https://docs.zeotap.com/home/en-us/", "data/raw/zeotap_docs.json")