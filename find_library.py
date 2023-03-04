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
    pc_uppercase=pc.upper()

    # open the connection to the database.
    conn = sqlite3.connect('public_libraries_data.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    #Here, I am using backward slash (\) to tell python to ignore new lines in the sql query.
    cur.execute(f"select * from libraries \
        JOIN post_codes_table \
        ON libraries.Post_codes=post_codes_table.Postcode \
        WHERE REPLACE(libraries.Post_codes,' ','')=REPLACE('{pc_uppercase}', ' ', '')")
    #Stores all details fetched using the query to a list named rows.
    rows = cur.fetchall()

    #Closing the connection to database.
    conn.close()
    if not pc:
        return "please enter a valid post code within England"
    return render_template('library_details.html', rows=rows)
