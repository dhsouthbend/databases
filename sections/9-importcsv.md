[<<< Back](8-innerjoin.md) - [Next >>>](9b-datasets.md)

# Import data into table

Now we are moving back into the world of Python! Let's create a new file in the `database-practice` directory.

Our goal is to create a database table from an [existing csv file](https://github.com/GCDigitalFellows/nypl_data/blob/master/nypl_items.csv). Click the link, then right-click the `Download` button on that page, and click `save link as` to get the csv we want. Move the csv file to your `database-practice` directory.

We're going to use the Pandas library to import our data.

```python
import pandas
import sqlite3

# make the connection
conn = sqlite3.connect('nypldb.db')

# have Pandas read our CSV
df = pandas.read_csv('nypl_items.csv', low_memory=False)

# convert our data into a SQlite table called 'nypl_items'
df.to_sql('nypl_items', conn)

# print a list of every record in  the table
print (pandas.read_sql_query("SELECT * FROM nypl_items", conn))
```

[<<< Back](8-innerjoin.md) - [Next >>>](9b-datasets.md)
