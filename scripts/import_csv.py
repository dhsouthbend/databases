import pandas
import sqlite3
cnx = sqlite3.connect('db.sqlite')
df = pandas.read_csv('nypl_items.csv', low_memory=False)
df.to_sql('nypl_items', cnx)
print (pandas.read_sql_query("SELECT * FROM nypl_items", cnx))
