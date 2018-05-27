# import sqlite library
import sqlite3

"""create a database and make a connection. This command will create a
new database if it doesn't already exist."""
conn = sqlite3.connect("first.db")
cursor = conn.cursor()

# create a table inside our database
cursor.execute("""CREATE TABLE programs  (
    id INTEGER PRIMARY KEY,
    program_name VARCHAR
)""")
conn.commit()
