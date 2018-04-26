[<<< Back](5-foreignkeys.md) - [Next >>>](7-commonqueries.md)  

# Challenge: Build a table for GPA!

Let's imagine that we want to connect each student to their GPA. How can we do this?

Things to consider:

- Where will we put the GPAs?
- What kind data type will they be?
- How will we connect each GPA to the correct student?

## Solution 

### Create a New Table For GPAs

```sql
CREATE TABLE gpas (
	id INTEGER PRIMARY KEY,
	gpa DOUBLE PRECISION,
	id_student INTEGER,
	FOREIGN KEY (id_student) REFERENCES students(id)
);
```  

### Populate the GPA Table with GPA Score and Foreign Key

```sql
INSERT INTO gpas (gpa, id_student) VALUES
	(2.67, 2),
	(3.9, 1),
	(1.23, 3),
	(4.0, 4);
```

[<<< Back](5-foreignkeys.md) - [Next >>>](7-commonqueries.md)  
