[<<< Back](0-dbintro.md) - [Next >>>](2-buildtable.md)

# Building a database

To get started, we're going to use the sqlite library to create the database file we will be using during this session. (We will also use the same file in a later session on web frameworks.)

1. Create a new file, called "createdb.py". Write some pseudocode that describes what our code will do once it's finished:

```Python
# import sqlite3 library

# create and connect to the database
```

2. Import the sqlite3 library, connect to the database, and create a cursor object. (Don't worry about this last part!)

```Python
# import sqlite library
import sqlite3

"""create a database and make a connection. This command will create a new database if it doesn't already exist."""
conn = sqlite3.connect("firstdb.db")
```

3. Run the program. First, open the command line, cd to the directory containing your "createdb.py" file and "firstdb.db" database. Then type

```Python
python createdb.py
```
and hit Enter. Now check your directory to see whether "firstdb.db" has been created.

Congratulations! You've successfully created and accessed your database using a Python script. This is an excellent first step in performing data analysis on large data sets or creating your own applications!

[<<< Back](0-dbintro.md) - [Next >>>](2-buildtable.md)
