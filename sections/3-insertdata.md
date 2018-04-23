[<<< Back](2-buildtable.md) - [Next >>>](4-updatefield.md)

# Inserting data into an SQL table

Now that we have a table structure, we need to insert some data. We need to create a new file for our next steps. Call it "databases.py".

The syntax for inserting multiple records is:

```sql
INSERT INTO table_name (field_name) VALUES (record1), (record2), (record3)
```

Insert "Anthropology", "Biology", and "Linguistics" into the table we just created. Here is the SQL we need:

```sql
INSERT INTO programs (program_name) VALUES
("Anthropology"),
("Biology"),
("Linguistics");
```

In "databases.py", add these lines:

```python
# import sqlite library
import sqlite3

"""Make a connection to the 'firstdb.db' database."""
conn = sqlite3.connect("firstdb.db")
cursor = conn.cursor()

# insert multiple values into our 'programs' table
cursor.execute("""INSERT INTO programs (program_name) VALUES
("Anthropology"),
("Biology"),
("Linguistics")
)""")
```


[<<< Back](2-buildtable.md) - [Next >>>](4-updatefield.md)
