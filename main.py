import os
from operator import itemgetter
from itertools import chain
from flask import Flask, json, jsonify
from difflib import get_close_matches
from Levenshtein import jaro_winkler

app = Flask(__name__)

# This route provides access to all the data in the json file.
# TODO: I should add a limit to the amount of data returned once I have more data in the data.json file.
@app.route("/")
def get_all_products():
    # filename variable has the path to the data.json file.
    filename = os.path.join(os.path.dirname(__file__), "data.json")
    # open the data.json file as data using the filename variable.
    with open(filename) as data:
        # load the data within data.json file.
        data = json.load(data)
        # return the data in json format.
        # Might not need the jsonify function currently but might be necessary later.
        return jsonify(data)

# This route allows for the data to be filtered based on the "type" of the product.
# I've passed in a "filter" variable into the get _types function.
@app.route("/filter_type=<string:filter>")
def get_types(filter):
    # filename variable has the path to the data.json file.
    filename = os.path.join(os.path.dirname(__file__), "data.json")
    # open the data.json file as data using the filename variable.
    with open(filename) as data:
        # load the data within the data.json file.
        data = json.load(data)
        # filter the products into a new dict
        # based on whether the filter variable passed in is one of the types that the product falls under.
        results = {"products": [x for x in data["products"] if filter in x["type"]]}
        # return the data in json format
        return jsonify(results)

# This route allows for searches based on whether the query matches "keywords" of the product.
# I've passed in a "query" variable into the get_searche function.
@app.route("/search/q=<query>")
def get_search(query):
    # filename variable has the path to the data.json file.
    filename = os.path.join(os.path.dirname(__file__), "data.json")
    # open the data.json fle as data using the filename variable.
    with open(filename) as data:
        # load the data within the data.json file.
        data = json.load(data)
        # get a list of all the "keywords" and remove any duplicates.
        all_keywords = [x["keywords"] for x in data["products"]]
        keywords = list(set(chain.from_iterable(all_keywords)))
        # use get_close_matches from difflib to see if the query matches any of the keywords.
        matched_keywords = get_close_matches(query, keywords, len(data["products"]), 0.4)
        # use the keywords that match to get a list of all the products with that keyword.
        matches = [x for x in data["products"] if len([y for y in matched_keywords if y in x["keywords"]]) != 0]
        # use jaro_winkler from Levenshtein to rate how close to the search the "description" of each product is.
        sort_lst = [{"product": x, "rate": jaro_winkler(query, x["description"])} for x in matches]
        # sort the list based on how similar the "query" is to the "description".
        sort_lst.sort(key=itemgetter("rate"), reverse=True)
        # pass the list of sorted products into a new dict.
        results = {"products": [x["product"] for x in sort_lst]}
        # return the data in json format.
        return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)