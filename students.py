# import sqlite library
import sqlite3

# create a database and make a connection.
conn = sqlite3.connect("firstdb.db")
cursor = conn.cursor()

sql = """CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    student VARCHAR,
    id_program INTEGER,
    FOREIGN KEY (id_program) REFERENCES programs(id)
)"""
cursor.execute(sql)

conn.commit()



# CHALLENGE
sql = """INSERT INTO students(student, id_program) VALUES
('Josefina', 3),
('Cecilia', 2),
('Nico', 2),
('Sarah', 1)
)"""
cursor.execute(sql)

conn.commit()
