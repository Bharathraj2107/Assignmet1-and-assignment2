from flask import request, jsonify, render_template
from app.nlp import preprocess_question, search_docs
from app import app

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_question = request.json.get('question')
    processed_question = preprocess_question(user_question)
    answer = search_docs(processed_question)
    return jsonify({"answer": answer})