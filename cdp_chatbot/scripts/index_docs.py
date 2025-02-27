from whoosh.fields import Schema, TEXT, ID
from whoosh.index import create_in
import json
import os

schema = Schema(title=TEXT(stored=True), content=TEXT(stored=True), path=ID(stored=True))

if not os.path.exists("indexdir"):
    os.makedirs("indexdir")

ix = create_in("indexdir", schema)
writer = ix.writer()

# Index documentation for all CDPs
cdps = ["segment", "mparticle", "lytics", "zeotap"]
for cdp in cdps:
    with open(f'data/processed/{cdp}_docs_cleaned.json', 'r') as f:
        docs = json.load(f)
    
    for i, doc in enumerate(docs):
        writer.add_document(title=f"{cdp.capitalize()} Chunk {i}", content=doc, path=f"/{cdp}/chunk/{i}")

writer.commit()