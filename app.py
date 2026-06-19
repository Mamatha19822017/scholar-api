from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "API Running Successfully"

@app.route('/fetch', methods=['GET'])
def fetch_test():
    return jsonify({
        "status": "success",
        "message": "Fetch API Working"
    })

@app.route('/fetch', methods=['POST'])
def fetch_publications():

    data = request.get_json()

    faculty = data.get('faculty', '')
    scholar_link = data.get('scholarLink', '')

    sample_data = [
        {
            "title": "Sample Publication 1",
            "year": "2025",
            "citations": 15,
            "journal": "IEEE Access"
        },
        {
            "title": "Sample Publication 2",
            "year": "2024",
            "citations": 8,
            "journal": "Springer"
        }
    ]

    return jsonify(sample_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
