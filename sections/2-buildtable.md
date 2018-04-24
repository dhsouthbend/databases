[<<< Back](1-builddb.md) - [Next >>>](3-insertdata.md)

# Building tables

The next step is to create tables to hold your data. From here onwards, we are going to be using Python and SQL together to execute database queries.

The syntax for creating a table in SQLite is:

```sql
CREATE TABLE table_name ( field_name data_type constraints )
```

- The [data type](https://www.sqlite.org/datatype3.html) will affect the behavior of the data in that field. For example, whether the data itself is treated as text or a number.

- The [constraints](http://www.tutorialspoint.com/sqlite/sqlite_constraints.htm) will affect the behavior of that field. For example, a field with a `NOT NULL` constraint means that each record must have some data in this field.

2. Create a new file and call it "buildtable.py". Add these lines to connect to the database, as before.

```python
# import sqlite library
import sqlite3

"""create a database and make a connection. This command will create a new database if it doesn't already exist."""
conn = sqlite3.connect("firstdb.db")

# create a cursor
cursor = conn.cursor()
```

Notice that this time we also created a "cursor" object for the database. This allows us to traverse the database records, to search through and change them.

3. Create a table to store data about academic programs. Name the table "programs" and give it two fields (aka, columns): one for "id", the other for "program_name".

First let's write the SQL we need:

```sql
CREATE TABLE programs  (
	id INTEGER PRIMARY KEY,
	program_name VARCHAR
);
```

Now we include that statement in a Python function:

```python
conn.execute("""CREATE TABLE programs  (
    id INTEGER PRIMARY KEY,
    program_name VARCHAR
)""")
```

And we add that function to our "buildtable.py" file, so now our script looks like this:

```python
# import sqlite library
import sqlite3

"""create a database and make a connection. This command will create a new database if it doesn't already exist."""
conn = sqlite3.connect("firstdb.db")
cursor = conn.cursor()

# create a table inside our database
cursor.execute("""CREATE TABLE programs  (
    id INTEGER PRIMARY KEY,
    program_name VARCHAR
)""")
conn.commit()
```

So now WHAT??????


[<<< Back](1-builddb.md) - [Next >>>](3-insertdata.md)
