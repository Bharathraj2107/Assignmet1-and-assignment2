from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/save', methods=['POST'])
def save():
    data = request.json
    # Save data to a file or database
    return jsonify({"message": "Data saved successfully"})

@app.route('/load', methods=['GET'])
def load():
    # Load data from a file or database
    return jsonify({"data": []})

if __name__ == '__main__':
    app.run(debug=True)