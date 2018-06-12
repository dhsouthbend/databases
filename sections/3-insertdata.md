[<<< Back](2-buildtable.md) - [Next >>>](3b-pythonic.md)

# Inserting data into an SQL table

Now that we have a table structure, we can insert some data. Let's make a table of departments in a school. We need to create a new file for our next steps. Call it `insert.py`.

The syntax for inserting multiple records is:

```sql
INSERT INTO table_name (field_name) VALUES (record1), (record2), (record3);
```

Insert `Anthropology`, `Biology`, and `Linguistics` into the table we just created. Here is the SQL we need:

```sql
INSERT INTO programs (program_name) VALUES
("Anthropology"),
("Biology"),
("Linguistics");
```

In `insert.py`, add these lines:

```python
# import sqlite library
import sqlite3

# Make a connection to the 'firstdb.db' database.
conn = sqlite3.connect("first.db")

cursor = conn.cursor()

# insert multiple values into our 'programs' table
cursor.execute("""INSERT INTO programs (program_name) VALUES

('Anthropology'),
('Biology'),
('Linguistics');
""")

conn.commit()

# print out our table
cursor.execute("SELECT * FROM programs")
# the 'fetchall()' function will return all of the results of a query
print(cursor.fetchall())
```
Run `insert.py`. If you see the programs we added to the database, it worked! 

[<<< Back](2-buildtable.md) - [Next >>>](3b-pythonic.md)
