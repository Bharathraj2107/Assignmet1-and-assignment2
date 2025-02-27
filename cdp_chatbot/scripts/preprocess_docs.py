import json
import re
import os

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = re.sub(r'<.*?>', '', text)  # Remove HTML tags
    return text.strip()

def preprocess_docs(input_file, output_file):
    with open(input_file, 'r') as f:
        docs = json.load(f)
    
    cleaned_docs = [clean_text(doc) for doc in docs]
    
    # Split into chunks of 500 characters
    chunks = []
    for doc in cleaned_docs:
        for i in range(0, len(doc), 500):
            chunks.append(doc[i:i+500])
    
    os.makedirs('data/processed', exist_ok=True)
    with open(output_file, 'w') as f:
        json.dump(chunks, f)

if __name__ == '__main__':
    # Preprocess documentation for all CDPs
    preprocess_docs("data/raw/segment_docs.json", "data/processed/segment_docs_cleaned.json")
    preprocess_docs("data/raw/mparticle_docs.json", "data/processed/mparticle_docs_cleaned.json")
    preprocess_docs("data/raw/lytics_docs.json", "data/processed/lytics_docs_cleaned.json")
    preprocess_docs("data/raw/zeotap_docs.json", "data/processed/zeotap_docs_cleaned.json")