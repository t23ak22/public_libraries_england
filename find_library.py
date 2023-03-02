from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)

@app.route('/', )
def index():
    return render_template("index.html")    

@app.route('/search_result', methods=["GET"])
def display_result():
    # Receiving post code from the user which the user entered in the web page
    pc=request.args.get("pc")

    # open the connection to the database
    conn = sqlite3.connect('public_libraries_data.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(f"select * from libraries JOIN post_codes_table ON libraries.Post_codes=post_codes_table.Postcode WHERE libraries.Post_codes='{pc}'")
    rows = cur.fetchall()
    conn.close()
    return render_template('result.html', rows=rows)