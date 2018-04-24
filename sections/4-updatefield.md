[<<< Back](3b-pythonic.md) - [Next >>>](5-foreignkeys.md)

# Updating fields

Another step, another file to work on. Create "update.py".

You can alter tables after they've been created. The SQL syntax below adds another field to the existing table and then populates that field with data.

```sql
ALTER TABLE programs    --selects the "programs" table to update
ADD program_level VARCHAR;    --adds a "program_level" column, which is a string
```

1. Create a connection to our database.

```python
# import sqlite library
import sqlite3

# create a database and make a connection.
conn = sqlite3.connect("firstdb.db")
cursor = conn.cursor()
```

2. Add another field for "program_level" to the existing table.

```python
sql = """ALTER TABLE programs
	ADD program_level VARCHAR"""
cursor.execute(sql)

conn.commit()
```

2. Now, let's populate the new empty "program_level" field with some data. Can you manage with only the SQL?

```sql
UPDATE programs		--select the table to update
SET program_level = "Ph.D."		--select the field and value to update
WHERE program_name = 'Linguistics';		--select the condition for updating
```

### Challenge

Update the "program_level" field for "Biology" and "Anthropology" with "Master's".

Hint: You can do this with one statement using_ `IN`







#### Solution

```sql
UPDATE programs
SET program_level = "Master's"
WHERE program_name IN ("Anthropology", "Biology");
```

[<<< Back](3b-pythonic.md) - [Next >>>](5-foreignkeys.md)
