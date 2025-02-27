import spacy
from whoosh.index import open_dir
from whoosh.qparser import QueryParser

nlp = spacy.load("en_core_web_sm")
ix = open_dir("indexdir")

def preprocess_question(question):
    doc = nlp(question)
    tokens = [token.lemma_ for token in doc if not token.is_stop]
    return " ".join(tokens)

def search_docs(question):
    with ix.searcher() as searcher:
        query = QueryParser("content", ix.schema).parse(question)
        results = searcher.search(query, limit=1)
        if results:
            return results[0]['content']
        else:
            return "Sorry, I couldn't find an answer to your question."