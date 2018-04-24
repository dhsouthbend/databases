# import sqlite library
import sqlite3

"""Make a connection to the 'firstdb.db' database."""
conn = sqlite3.connect("firstdb.db")
cursor = conn.cursor()

# insert multiple values into our 'programs' table
cursor.execute("""INSERT INTO programs (program_name) VALUES
("Anthropology"),
("Biology"),
("Linguistics")
)""")

# print out our table
cursor.execute("SELECT * FROM programs")
print(cursor.fetchall())
