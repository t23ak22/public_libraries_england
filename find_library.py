from flask import Flask, render_template, request
import re
import sqlite3
app = Flask(__name__)

@app.route('/', )
def index():
    return render_template("index.html")  

#Defining a function that checks the format of postcode entered by user using regular expression.
def check_postcode_validity(postcode):
  regex = r'^[A-Za-z]{1,2}\d{1,2}[A-Za-z]?\s?\d[A-Za-z]{2}$' 
  if re.match(regex, postcode):
    return True
  else:
    return False 

@app.route('/search_result', methods=["GET"])
def display_result():
    # Receiving post code from the user which the user entered in the web page
    pc=request.args.get("pc")
    pc_uppercase=pc.upper()

    try:
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

    except:
      print("Error on connecting to database.")

    finally:
      #Closing the connection to database.
      conn.close()

    #Checking if the postcode entered is a valid one using regular expression.
    if check_postcode_validity(pc_uppercase):
      return render_template('library_details.html', rows=rows)
    return "Please try again with a valid post code within England."
