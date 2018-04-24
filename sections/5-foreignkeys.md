[<<< Back](4-updatefield.md) - [Next >>>](6-buildtable_challenge.md)

# Relating tables with foreign keys

At this point, we're going to create a second table called "students" to illustrate the relational nature of relational databases. We use the same syntax that we used to create the "programs" table, but with one extra element: **a foreign key**. Let's work in a new file that we call "students.py".

1. As before, create a connection to the "firstdb.db" database.

```python
# import sqlite library
import sqlite3

# create a database and make a connection.
conn = sqlite3.connect("firstdb.db")
cursor = conn.cursor()
```

2. Create a table called "students" with a field for: (1) a primary key, (2) student name, and (3) a foreign key that will reference the "programs" table. If the SQL looks like this:

```sql
CREATE TABLE students (
	id INTEGER PRIMARY KEY,
	student VARCHAR,
	id_program INTEGER,
	FOREIGN KEY (id_program) REFERENCES programs(id) -- this establishes the reference!
);
```

Then our Python file should look like this:

```python
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

```

The foreign key points to a primary key in another table, in this case the "programs" table. This relationship is specified with the clause `FOREIGN KEY (id_program) REFERENCES programs(id)`, which links the "id_program" field in the "students" table to the "id" field in the "programs" table.

All records in the "students" table must point to a valid primary key in the "programs" table.

3. The last step is to add some data to the new "students" table.

	*Try this on your own before looking below.*

	- **Remember:**
		- The primary key will be generated automatically.
		- The foreign keys must be entered manually - YOU decide which program to associate with each student.


```sql
INSERT INTO students(student, id_program) VALUES
('Josefina', 3),
('Cecilia', 2),
('Nico', 2),
('Sarah', 1);
```

_**We will make use of the foreign key in the next step!**_

[<<< Back](4-updatefield.md) - [Next >>>](6-buildtable_challenge.md)
