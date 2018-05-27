# import sqlite library
import sqlite3

# create a database and make a connection.
conn = sqlite3.connect("first.db")
cursor = conn.cursor()

sql = """UPDATE programs
SET program_level = 'Master''s'
WHERE program_name IN ('Anthropology', 'Biology')"""
cursor.execute(sql)


sql = """INSERT INTO students(student, id_program) VALUES
('Josefina', 3),
('Cecilia', 2),
('Nico', 2),
('Sarah', 1)
"""
cursor.execute(sql)

conn.commit()
