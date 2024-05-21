import os
from flask import Flask, json, jsonify

app = Flask(__name__)

@app.route("/")
def get_products():
    filename = os.path.join(os.path.dirname(__file__), "data.json")
    with open(filename) as data:
        data = json.load(data)
        return jsonify(data)



if __name__ == "__main__":
    app.run(debug=True)