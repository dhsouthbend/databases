# import sqlite library
import sqlite3

# create a database and make a connection.
conn = sqlite3.connect("firstdb.db")
cursor = conn.cursor()

sql = """ALTER TABLE programs
    ADD program_level VARCHAR"""
cursor.execute(sql)

# commit the changes
conn.commit()



# ALTERing the table
sql = """ALTER TABLE programs
    ADD program_level VARCHAR"""
cursor.execute(sql)

# commit the changes
conn.commit()



# UPDATEing the records
sql = """UPDATE programs
SET program_level = 'Ph.D.'
WHERE program_name = 'Linguistics'"""
cursor.execute(sql)

# commit the changes
conn.commit()



# more UPDATEs
sql = """UPDATE programs
SET program_level = 'Master\'s'
WHERE program_name IN ('Anthropology', 'Biology');"""
cursor.execute(sql)

# commit the changes
conn.commit()
