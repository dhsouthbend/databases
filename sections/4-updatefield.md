[<<< Back](3b-pythonic.md) - [Next >>>](5-foreignkeys.md)

# Updating Fields

Another step, another file to work on. Create `update.py`.

You can alter tables after they've been created. The SQL syntax below adds another field to the existing table and then populates that field with data.

```sql
ALTER TABLE programs    --selects the "programs" table to update
ADD program_level VARCHAR;    --adds a "program_level" column, which is a string
```

XXX Put an explanation of SQL comments in here XXX

Create a connection to our database:

```python
# import sqlite library
import sqlite3

# create a database and make a connection.
conn = sqlite3.connect("firstdb.db")
cursor = conn.cursor()
```

Next, add another field for `program_level` to the existing table:

```python
sql = """ALTER TABLE programs
	ADD program_level VARCHAR"""
cursor.execute(sql)

# commit the changes
conn.commit()
```

Now, let's populate the new empty "program_level" field with some data. Can you manage with only the SQL?

```sql
UPDATE programs		--select the table to update
SET program_level = "Ph.D."		--select the field and value to update
WHERE program_name = 'Linguistics';		--select the condition for updating
```

### Challenge

Update the `program_level` field for `Biology` and `Anthropology` with `Master's`.

Hint: You can do this with one statement using_ `IN`. The solution is [here](solution1.sql).

[<<< Back](3b-pythonic.md) - [Next >>>](5-foreignkeys.md)
