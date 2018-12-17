[<<< Back](1-builddb.md) - [Next >>>](3-insertdata.md)

# Building tables

The next step is to create tables to hold your data. From here on, we are going to be using SQL to execute database queries.

The syntax for creating a table in SQLite is:

```sql
CREATE TABLE table_name ( field_name data_type constraints );
```

- The field name describes some aspect of the record, such as `name`, `id`, or `last_updated_on`.
- The [data type](https://www.sqlite.org/datatype3.html) will affect the behavior of the data in that field. For example, whether the data itself is treated as text or a number. 
- The [constraints](http://www.tutorialspoint.com/sqlite/sqlite_constraints.htm) will affect the behavior of that field. For example, a field with a `NOT NULL` constraint means that each record must have some data in this field.


Let's create a table to store data about academic programs. Name the table "programs" and give it two fields (aka, columns): one for `id`, the other for `program_name`.

Here's the SQL we need:

```sql
CREATE TABLE programs  (
	id INTEGER PRIMARY KEY,
	program_name VARCHAR
);
```
Remember, you can press `enter` at any time to start a new line, without executing the code. A `;` is necessary to finish a line of SQL. SQLite is not case-sensitive. Press `enter` after the `;` to create this table in your SQLite database.

A table is most useful when it represents a category of object you are tracking. A record in a table is one instance of that category, i.e. a book in a collection of books, or a person in a list of people. Each field is an aspect of that record, like the author of a book, or the age of a person. This will become clearer as we continue.

[<<< Back](1-builddb.md) - [Next >>>](3-insertdata.md)
