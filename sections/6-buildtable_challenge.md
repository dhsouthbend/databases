[<<< Back](5-foreignkeys.md) - [Next >>>](7-commonqueries.md)  

# Challenge: build a table for GPA!

Now we have a student table that looks something like this:

```
id          student     id_program
----------  ----------  ----------
1           Josefina    3
2           Cecilia     2
3           Nico        2
4           Sarah       1
```

Let's imagine that we want to connect each student to their GPA. How can we do this?

Things to consider:

- Where will we put the GPAs?
- What kind of data type will they be?
- How will we connect each GPA to the correct student?

## Solution 

### Create a New Table For GPAs

```sql
CREATE TABLE gpas (
	id INTEGER PRIMARY KEY,
	gpa FLOAT,
	id_student INTEGER,
	FOREIGN KEY (id_student) REFERENCES students(id)
);
```

You may notice a new term in the above example. `FLOAT` is just a number that can have a decimal point.

### Populate the GPA Table with GPA Score and Foreign Key

```sql
INSERT INTO gpas (gpa, id_student) VALUES
	(2.67, 2),
	(3.9, 1),
	(1.23, 3),
	(4.0, 4);
```

And thus our table for GPAS looks like:
```
id          gpa         id_student
----------  ----------  ----------
1           2.67        2
2           3.9         1
3           1.23        3
4           4.0         4
```

[<<< Back](5-foreignkeys.md) - [Next >>>](7-commonqueries.md)  
