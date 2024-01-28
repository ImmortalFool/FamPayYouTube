from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route("/get-data/<search_query>")
def get_data(search_query):
    return "Return List of data"


if __name__ == "__main__":
    app.run(debug=True)

