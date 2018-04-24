[<<< Back](7-commonqueries.md) - [Next >>>](9-importcsv.md)

# Joins

Each of the queries up to now has just returned data from a single table in the database. This final query combines our "students" and "programs" tables using the `INNER JOIN` and `ON` clause:

```python
"""Show all the records for students with
information about their respective programs"""

sql = """SELECT *
FROM students INNER JOIN programs
ON students.id_program = programs.id"""

cursor.execute(sql)

# print results
print(cursor.fetchall())
```

This query should return what you see below:

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! add result

This query demonstrates the power of relational databases by using the foreign key in the "students" table to coordinating data with the "programs" table.

### Challenge

Write a query that returns only the name of each student and their respective program level.


### Solution

```sql
SELECT student, program_level
FROM students INNER JOIN programs
ON students.id_program = programs.id;
```

### Challenge

Write a query that returns the name of each student, their program name, and their GPA with results sorted by GPA from low to high.


### Solution

```sql
SELECT student, program_name, gpa
FROM students INNER JOIN gpas
ON gpas.id_student = students.id
INNER JOIN programs
ON programs.id = students.id_program
ORDER BY gpas.gpa ASC;
```

*__How can you make sure that the data from 'gpas', 'students', and 'programs' is aligning correctly?__*

[<<< Back](7-commonqueries.md) - [Next >>>](9-importcsv.md)
