[<<< Back](0-dbintro.md) - [Next >>>](2-buildtable.md)

# Building a database

To get started, we're going to use the `sqlite` library to create the database file we will be using during this session.

In these sesssions, we've been placing files in a `projects` folder on our desktop. Let's create a folder for this session on databases. These commands will also create the `projects` folder if you don't already have it.

Open your command line and enter these commands:

```bash
mkdir -p ~/Desktop/projects/database-practice
cd ~/Desktop/projects/database-practice
```

This will create a new folder for this session and also move into it using the `cd` command.

Now that you're in the correct folder, begin creating a new Python file with this command:

```bash
code createdb.py
```

In your editor, type this code:

```python
# import sqlite library
import sqlite3

# Connect to a database. 
# This command will create a new database if it doesn't already exist.

conn = sqlite3.connect("first.db")
```

Save the file with `Control-s` on Windows or `⌘-s` on Mac. Let's call it  `createdb.py`.

Back on the command line, enter this command to run the script:

```bash
python createdb.py
```

Now check your directory with the `ls` command to see whether "firstdb.db" has been created.

Congratulations! You've successfully created and accessed your database using a Python script. This is an excellent first step toward performing data analysis on large data sets or creating your own applications!

[<<< Back](0-dbintro.md) - [Next >>>](2-buildtable.md)
