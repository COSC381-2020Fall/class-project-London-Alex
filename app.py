from flask import Flask, render_template, request, jsonify
import query_on_whoosh
import smtplib
import config

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
    if not search_term:
        search_term = ""

    search_page = request.args.get("p")
    if not search_page:
        search_page = 1
    else:
        search_page = int(search_page)

    search_results, num_hits, num_pages = query_on_whoosh.performQuery(search_term, search_page, 10)
    return render_template("query.html", results=search_results, query_term=search_term, page_count=num_pages)

@app.route("/about", strict_slashes=False)
def handle_about():
    return render_template("about.html")

@app.route("/success", strict_slashes=False)
def handle_request():
    new_data = request.args.get("new_data")
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("alondon6@emich.edu", config.gmail_password)
    message = "Subject: {}\n\n{}".format("Request to add new data", "Request to add " + new_data)
    server.sendmail("alondon6@emich.edu", "alondon6@emich.edu", message)
    return render_template("success.html", new_data=new_data)