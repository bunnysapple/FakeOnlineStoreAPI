import os
from operator import itemgetter
from itertools import chain
from flask import Flask, json, jsonify
from difflib import get_close_matches
from Levenshtein import jaro_winkler

app = Flask(__name__)

@app.route("/")
def get_all_products():
    filename = os.path.join(os.path.dirname(__file__), "data.json")
    with open(filename) as data:
        data = json.load(data)
        return jsonify(data)

@app.route("/filter_type=<string:filter>")
def get_types(filter):
    filename = os.path.join(os.path.dirname(__file__), "data.json")
    with open(filename) as data:
        data = json.load(data)
        results = {"products": [x for x in data["products"] if filter in x["type"]]}
        return jsonify(results)

@app.route("/search/q=<query>")
def get_search(query):
    query = query
    filename = os.path.join(os.path.dirname(__file__), "data.json")
    with open(filename) as data:
        data = json.load(data)
        all_keywords = [x["keywords"] for x in data["products"]]
        keywords = list(set(chain.from_iterable(all_keywords)))
        matched_keywords = get_close_matches(query, keywords, len(data["products"]), 0.4)
        matches = [x for x in data["products"] if len([y for y in matched_keywords if y in x["keywords"]]) != 0]
        sort_lst = [{"product": x, "rate": jaro_winkler(query, x["description"])} for x in matches]
        sort_lst.sort(key=itemgetter("rate"), reverse=True)
        return {"products": [x["product"] for x in sort_lst]}

if __name__ == "__main__":
    app.run(debug=True)