sql = """SELECT program_name, program_level
FROM programs;"""

cursor.execute(sql)

print(cursor.fetchall())
