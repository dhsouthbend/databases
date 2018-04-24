[<<< Back](8-innerjoin.md) - [Next >>>](10-usefulqueries.md)

# Import data into table

Let's create a database table from an [existing csv file](https://github.com/GCDigitalFellows/nypl_data/blob/master/nypl_items.csv).

We're going to cheat a bit by using the Pandas library to import our data.

```python
import pandas
import sqlite3

# make the connection
conn = sqlite3.connect('db.sqlite')

# have Pandas read our CSV
df = pandas.read_csv('nypl_items.csv', low_memory=False)

# convert our data into a SQlite table called 'nypl_items'
df.to_sql('nypl_items', conn)

# print a list of every record in  the table
print (pandas.read_sql_query("SELECT * FROM nypl_items", conn))
```

[<<< Back](8-innerjoin.md) - [Next >>>](10-usefulqueries.md)
