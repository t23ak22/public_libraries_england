import csv
import sqlite3

# open the connection to the database
conn = sqlite3.connect('public_libraries_data.db')
cur = conn.cursor()

# drop the data from the table so that if we rerun the file, we don't repeat values
conn.execute('DROP TABLE IF EXISTS libraries')
print("table dropped successfully")

# drop table 2 if it already exists
conn.execute('DROP TABLE IF EXISTS post_codes_table')
print("table dropped successfully")

# create table 1
conn.execute('CREATE TABLE libraries (LibraryID INTEGER PRIMARY KEY AUTOINCREMENT, Library_name TEXT, Library_service TEXT, Post_codes TEXT)')
print("table created successfully")

# create table 2
conn.execute('CREATE TABLE post_codes_table (Postcode TEXT PRIMARY KEY UNIQUE, Address TEXT)')
print("table created successfully")

# Insert data into table 1
with open('Librariesdata/Public_libraries_in_England-_extended_basic_dataset__as_on_1_July_2016_.csv', newline='',  errors = 'backslashreplace') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader) # skip the header line
    for row in reader:
        print(row)

        Library_name = row[1]
        Library_service = row[0]
        Post_codes = row[3]

        cur.execute('INSERT INTO libraries VALUES (NULL,?,?,?)', (Library_name, Library_service, Post_codes))
        conn.commit()
print("data parsed successfully")

# Insert data into table 2
with open('Librariesdata/Public_libraries_in_England-_extended_basic_dataset__as_on_1_July_2016_.csv', newline='',  errors = 'backslashreplace') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader) # skip the header line
    for row in reader:
        print(row)

        Post_code = row[3]
        Address = row[2]

        cur.execute('INSERT OR IGNORE INTO post_codes_table VALUES (?,?)', (Post_code, Address))
        conn.commit()
print("data parsed successfully")

conn.close()