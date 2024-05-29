import os
from math import ceil
from operator import itemgetter
from itertools import chain
from flask import Flask, request, json, jsonify
from difflib import get_close_matches
from Levenshtein import jaro_winkler

app = Flask(__name__)

# This route provides access to all the data in the json file.
@app.route("/")
def get_all_products():
    # get and store all the parameters as variables and assign any relevant variables as necessary
    filter_type = request.args.get("filter_type", default="all", type=str)
    page = request.args.get("page", default=1, type=int)
    per_page = request.args.get("per_page", default=10, type=int)
    start = page * per_page - per_page
    end = page * per_page
    # get the file path for data.json file and open and load the json file as data
    filename = os.path.join(os.path.dirname(__file__), "data.json")
    with open(filename) as data:
        data = json.load(data)
        products = data["products"]
        # filter products based on type if there is a filter_type value passed in that is not "all"
        if filter_type != "all":
            products = [x for x in products if filter_type in x["type"]]
        # return empty dict if no product and return status code 204 for no content
        if len(products) < start:
            return {}, 204
        num_products = len(products)
        num_pages = ceil(num_products/per_page)
        # get the list of products based on the per_page and page parameters and return them in json format with sttus code 404
        result = {
            "page": page,
            "pages": num_pages,
            "total_products": num_products,
            "products": products[start:end] if len(products) >= end else products[start:]
            }
        return jsonify(result), 200

# This route allows for searches based on whether the query matches "keywords" of the product.
# I've passed in a "query" variable into the get_search function.
@app.route("/search/<query>/")
def get_search(query:str):
    # get all the parameters as variables and assign any relevant variables as necessary
    filter_type = request.args.get("filter_type", default="all", type=str)
    page = request.args.get("page", default=1, type=int)
    per_page = request.args.get("per_page", default=10, type=int)
    if per_page > 50:
        per_page = 50
    elif per_page < 10:
        per_page = 10
    start = page * per_page - per_page
    end = page * per_page
    # get the file path for data.json and open and load the json file as data
    filename = os.path.join(os.path.dirname(__file__), "data.json")
    with open(filename) as data:
        data = json.load(data)
        products = data["products"]
        # filter products based on type if there is a filter_type value passed in that is not "all"
        if filter_type != "all":
            products = [x for x in products if filter_type in x["type"]]
        # get a list of all the "keywords" and remove any duplicates.
        all_keywords = [x["keywords"] for x in products]
        keywords = list(set(chain.from_iterable(all_keywords)))
        # use get_close_matches to get similar keywords and get all the products with those keywords.
        # then sort products based on relevance using jaro_winkler
        matched_keywords = get_close_matches(query, keywords, len(products), 0.7)
        matches = [x for x in products if len([y for y in matched_keywords if y in x["keywords"]]) != 0]
        sort_lst = [{"product": x, "relevance": jaro_winkler(query, x["description"])} for x in matches]
        sort_lst.sort(key=itemgetter("relevance"), reverse=True)
        # return empty dict if no relevant product and return status code 204 for no content
        if len(sort_lst) < start:
            return {}, 204
        num_products = len(sort_lst)
        num_pages = ceil(num_products/per_page) if per_page > num_products else num_products
        # get the list of products based on the per_page and page parameters and return them in json format with sttus code 404
        result = {
            "page": page,
            "pages": num_pages,
            "total_products": num_products,
            "products": sort_lst[start:end] if len(sort_lst) >= end else sort_lst[start:]
            }
        # return the data in json format.
        return jsonify(result)

@app.route("/id/<id>/")
def get_id(id:int):
    if not id.isdigit():
        return {}, 404
    id = int(id)
    filename = os.path.join(os.path.dirname(__file__), "data.json")
    with open(filename) as data:
        data = json.load(data)
        products = data["products"]
        if id > len(products) or id < 0:
            return {}, 204
        results = {
            "page": 1,
            "pages": 1,
            "total_products": 1,
            "products": products[id]
        }
        return jsonify(results), 200

@app.route("/similar/")
def get_similar():
    id = request.args.get("id", default=-1, type=int)
    search = request.args.get("search", default="", type=str)
    per_page = request.args.get("per_page", default=5, type=int)
    filename = os.path.join(os.path.dirname(__file__), "data.json")
    with open(filename) as data:
        data = json.load(data)
        products = data["products"]
        search_for = next((x["keywords"] for x in products if x["id"] == id), search.split())
        sort_lst = [
            {"product": x,
             "relevance": len(
                 [
                     y for y in search_for if y in x["keywords"]
                 ]
            )
            } for x in products]
        # sort_lst = [{"product": x, "relevance": sum(
        #     jaro_winkler(z, y) for z in search_for for y in x["keywords"]
        # )} for x in products]
        sort_lst.sort(key=itemgetter("relevance"), reverse=True)
        products = sort_lst[0:per_page+1] if len(sort_lst) >= per_page else sort_lst
        results = {
            "products": {"products": [x["product"] for x in products[1:]]}
        }
        return jsonify(results)


if __name__ == "__main__":
    app.run(debug=True)