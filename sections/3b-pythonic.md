[<<< Back](3-insertdata.md) - [Next >>>](4-updatefield.md)

# A more readable approach
We've been using pure SQL in our scripts so far. Ah, but there's a more pythonic way of accomplishing our goal. Consider the script below:

```python
# import sqlite library
import sqlite3

# create a database and make a connection.
conn = sqlite3.connect("first.db")
cursor = conn.cursor()

sql = """CREATE TABLE boardgames (
    boardgame VARCHAR,
    length_in_hours INTEGER,
    players INTEGER
)"""

cursor.execute(sql)

conn.commit()

# insert multiple records using the "?" method
boardgames = [('Settlers of Catan', 3, 5),
          ('Settlers of Catan', 3, 5),
          ('Carcasonne', 1, 10),
          ('Diplomacy', 2, 4),
          ]

cursor.executemany("INSERT INTO boardgames VALUES (?,?,?)", boardgames)
conn.commit()
```

What might be the advantage of such an approach? It is cleaner, and after a bit of practice with Python, easier to read. Being more compact, it is easier to take in with one glance.

[<<< Back](3-insertdata.md) - [Next >>>](4-updatefield.md)
