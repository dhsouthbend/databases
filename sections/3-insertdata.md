[<<< Back](2-buildtable.md) - [Next >>>](4-updatefield.md)

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

# A note about mistakes

Mistakes happen! Constantly, in fact. In Python, fixing your mistake usually is a matter of correcting something in your script and running it again. One of the difficulties of learning SQL is that your mistake may end up entered into the database, and reversing that error is more difficult.

There are processes to remove mistakes in SQL. In a simple table like the one above, if we want to delete a row, we can do this:
```sql
DELETE FROM programs WHERE id = 1;
```
This would delete "Anthropology" from our table. If we want to edit our table instead, we would type:
```sql
UPDATE programs SET program_name = 'Physics' WHERE id = 3;
```
And now we have "Physics" in place of "Linguistics".

As we go through this tutorial, keep these `delete` and `update` commands in mind. But if you find your database has reached a state of complete confusion, don't be afraid of starting over! 

[<<< Back](2-buildtable.md) - [Next >>>](4-updatefield.md)
