# import sqlite library
import sqlite3

# create a database and make a connection.
conn = sqlite3.connect("firstdb.db")
cursor = conn.cursor()

sql = """CREATE TABLE gpas (
    id INTEGER PRIMARY KEY,
    gpa DOUBLE PRECISION,
    id_student INTEGER,
    FOREIGN KEY (id_student) REFERENCES students(id)
)"""
cursor.execute(sql)

sql = """INSERT INTO gpas (gpa, id_student) VALUES
    (2.67, 2),
    (3.9, 1),
    (1.23, 3),
    (4.0, 4)"""
cursor.execute(sql)

# commit the changes
conn.commit()
