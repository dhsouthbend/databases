[<<< Back](2-buildtable.md) - [Next >>>](3b-pythonic.md)

# Inserting data into an SQL table

Now that we have a table structure, we can insert some data. Let's make a table of departments in a school.

The syntax for inserting multiple records is:

```sql
INSERT INTO table_name (field_name) VALUES (record1), (record2), (record3);
```

Insert `Anthropology`, `Biology`, and `Linguistics` into the table we just created. Here is the SQL we need:

```sql
INSERT INTO programs (program_name) VALUES
("Anthropology"),
("Biology"),
("Linguistics");
```

Execute that code in the SQLite REPL. Now you have a database table with data in it! But it's all rather abstract without visible evidence, isn't it? In order to visualize our data, we need to change some settings in the SQLite program:
```sql
 .mode column
 .headers on
```
Now add this code:
```sql
select * from programs;
```
Here is the shape of our table:

```
id          program_name
----------  ------------
1           Anthropology
2           Biology
3           Linguistics
```
If you see the programs we added to the database, it worked! 

[<<< Back](2-buildtable.md) - [Next >>>](3-updatefield.md)
