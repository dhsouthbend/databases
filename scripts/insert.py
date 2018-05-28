# import sqlite library
import sqlite3

"""Make a connection to the 'firstdb.db' database."""
conn = sqlite3.connect("first.db")
cursor = conn.cursor()

sql = """INSERT INTO programs (program_name) VALUES
('Anthropology'),
('Biology'),
('Linguistics')
"""

# insert multiple values into our 'programs' table
cursor.execute(sql)

conn.commit()

# print out our table
cursor.execute("SELECT * FROM programs")
print(cursor.fetchall())
