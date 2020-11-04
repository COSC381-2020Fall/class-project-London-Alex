from flask import Flask, render_template, request, jsonify
import query_on_whoosh

app = Flask(__name__)
app.config.update(dict(JSONIFY_PRETTYPRINT_REGULAR=True))

@app.route("/")
def handle_slash():
    requested_name = request.args.get("name")
    return render_template("index.html", user_name=requested_name)

@app.route("/query", strict_slashes=False)
def handle_query():
    search_term = request.args.get("q")
    search_page = int(request.args.get("p"))
    search_results, num_hits, num_pages = query_on_whoosh.performQuery(search_term, search_page, 10)
    return jsonify({"query_term": search_term, "num_hits": num_hits, "num_pages": num_pages, "search_results": search_results})

@app.route("/query_view", strict_slashes=False)
def handle_query_view():
    search_term = request.args.get("q")
    search_page = int(request.args.get("p"))
    search_results, num_hits, num_pages = query_on_whoosh.performQuery(search_term, search_page, 10)
    return render_template("query.html", results = search_results)