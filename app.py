from flask import Flask, render_template, request, jsonify
import query_on_whoosh
import smtplib
import config
import sqlite3

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
    # don't yet know how different search topics will be implemented, so for now it's the current value by default
    search_topic = "Continental Divide"

    conn = sqlite3.connect('history.db')
    c = conn.cursor()
    
    search_term = request.args.get("q")
    search_page = request.args.get("p")

    c.execute("SELECT enable FROM settings WHERE name = 'search_history';")
    search_history_enabled = c.fetchone()[0]
    
    if not search_term:
        search_term = ""
    if not search_page:
        search_page = 1        
    else:
        search_page = int(search_page)

    if search_term != "" and search_page == 1 and search_history_enabled == 1:
        c.execute("INSERT INTO history (search_topic, search_term) VALUES (?, ?);", (search_topic, search_term))

    conn.commit()
    conn.close()

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

@app.route("/history", strict_slashes=False)
def handle_history():
    conn = sqlite3.connect('history.db')
    c = conn.cursor()
    
    # 'localtime' SHOULD do the function of '-5 hour' here but for whatever reason 'localtime' thinks I'm on UTC/GMT time.
    # using '-5 hour' to compensate for GMT to EST conversion
    c.execute("SELECT id, search_topic, search_term, datetime(search_time, '-5 hour') FROM history ORDER BY search_time DESC;")
    rows = c.fetchall()
    conn.close()

    return render_template("history.html", history_list=rows)

@app.route("/deletedHistory", strict_slashes=False)
def handle_delete():
    conn = sqlite3.connect('history.db')
    c = conn.cursor()
    
    deletedId = request.args.get("id")

    c.execute("DELETE FROM history WHERE id = (?);", (deletedId,))
    conn.commit()
    conn.close()

    return render_template("deletedHistory.html", id=deletedId)

@app.route("/settings", strict_slashes=False)
def handle_settings():
    return render_template("settings.html")

@app.route("/updatedSettings", strict_slashes=False)
def handle_updatedSettings():
    conn = sqlite3.connect('history.db')
    c = conn.cursor()
    
    search_history = request.args.get("search_history")
    if not search_history:
        enable_search_history = 0
    else:
        enable_search_history = 1

    c.execute("UPDATE settings SET enable = (?) WHERE name = 'search_history';", (enable_search_history,))
    conn.commit()
    conn.close()

    return render_template("updatedSettings.html")