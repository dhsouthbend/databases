[<<< Back](7-commonqueries.md) - [Next >>>](9-importcsv.md)

# Joins

Each of the queries up to now has just returned data from a single table in the database. This final query combines our "students" and "programs" tables using the `INNER JOIN` and `ON` clause:

```python
# Show all the records for students with information 
# about their respective programs
sql = """SELECT *
FROM students INNER JOIN programs
ON students.id_program = programs.id"""

cursor.execute(sql)

# Print results
print(cursor.fetchall())
```

This query should return what you see below:

```[(1, 'Josefina', 3, 3, 'Linguistics', 'Ph.D.'), (2, 'Cecilia', 2, 2, 'Biology', "Master's"), (3, 'Nico', 2, 2, 'Biology', "Master's"), (4, 'Sarah', 1, 1, 'Anthropology', "Master's"), (5, 'Josefina', 3, 3, 'Linguistics', 'Ph.D.'), (6, 'Cecilia', 2, 2, 'Biology', "Master's"), (7, 'Nico', 2, 2, 'Biology', "Master's"), (8, 'Sarah', 1, 1, 'Anthropology', "Master's")]```

This query demonstrates the power of relational databases by using the foreign key in the "students" table to coordinating data with the "programs" table.

### Challenge One

Write a query that returns only the name of each student and their respective program level. You can find a solution [here](solution5.sql).

### Challenge Two

Write a query that returns the name of each student, their program name, and their GPA with results sorted by GPA from low to high. You can find a solution [here](solution6.sql).

*_How can you make sure that the data from 'gpas', 'students', and 'programs' is aligning correctly?*

[<<< Back](7-commonqueries.md) - [Next >>>](9-importcsv.md)
