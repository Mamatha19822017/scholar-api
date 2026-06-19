```python
from flask import Flask, request, jsonify
from flask_cors import CORS
from scholarly import scholarly

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Faculty Publication API Running Successfully"

@app.route('/fetch', methods=['GET'])
def test():
    return jsonify({
        "status": "success",
        "message": "API Working"
    })

@app.route('/fetch', methods=['POST'])
def fetch_publications():

    try:

        data = request.get_json()

        scholar_link = data.get('scholarLink', '')

        if not scholar_link:
            return jsonify({
                "error": "Scholar link is required"
            }), 400

        if "user=" not in scholar_link:
            return jsonify({
                "error": "Invalid Google Scholar profile link"
            }), 400

        # Extract Author ID
        author_id = scholar_link.split("user=")[1].split("&")[0]

        # Fetch Author Information
        author = scholarly.search_author_id(author_id)
        author = scholarly.fill(author)

        publications = []

        for pub in author['publications']:

            try:

                pub = scholarly.fill(pub)

                publications.append({

                    "title":
                    pub.get('bib', {}).get('title', ''),

                    "year":
                    pub.get('bib', {}).get('pub_year', ''),

                    "journal":
                    pub.get('bib', {}).get('venue', ''),

                    "citations":
                    pub.get('num_citations', 0)

                })

            except Exception:
                continue

        return jsonify(publications)

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
