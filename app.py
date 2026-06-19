from flask import Flask, request, jsonify
from flask_cors import CORS
from scholarly import scholarly

app = Flask(__name__)
CORS(app)

@app.route('/fetch', methods=['POST'])
def fetch_publications():

    data = request.json

    faculty_name = data['faculty']
    scholar_link = data['scholarLink']

    author_id = scholar_link.split("user=")[1].split("&")[0]

    author = scholarly.search_author_id(author_id)
    author = scholarly.fill(author)

    publications = []

    for pub in author['publications']:

        try:

            pub = scholarly.fill(pub)

            publications.append({
                "title": pub['bib'].get('title', ''),
                "year": pub['bib'].get('pub_year', ''),
                "journal": pub['bib'].get('venue', ''),
                "citations": pub.get('num_citations', 0)
            })

        except:
            pass

    return jsonify(publications)

if __name__ == "__main__":
    app.run()
