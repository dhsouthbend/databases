[<<< Back](0-dbintro.md) - [Next >>>](2-buildtable.md)

# Building a Database

To get started, we're going to use the sqlite library to create the database file we will be using during this session.

First, create a new file, called "createdb.py". Import the sqlite3 library, and connect to the database.

```python
# import sqlite library
import sqlite3

# Connect to a database. 
# This command will create a new database if it doesn't already exist.

conn = sqlite3.connect("first.db")
```

Run the program. First, open the command line, cd to the directory containing your "createdb.py" file. Then type

```Python
python createdb.py
```

and hit Enter. Now check your directory to see whether "first.db" has been created.

Congratulations! You've successfully created and accessed your database using a Python script. This is an excellent first step in performing data analysis on large data sets or creating your own applications!

[<<< Back](0-dbintro.md) - [Next >>>](2-buildtable.md)
