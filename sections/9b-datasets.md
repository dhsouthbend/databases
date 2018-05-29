[<<< Back](9-datasets.md) - [Next >>>](10-usefulqueries.md)

# What makes a good dataset / cleaning data

Given a dataset that we want to use, how do we know that we can trust it to tell us what we want to learn? Of course, we have to ask the right questions--those that are possible for the dataset to answer. But we also have to test the integrity and consistency of the dataset. We have to make sure that the dataset is not incomplete, or messy, or liable to mislead us when we attempt to analyze it. Indeed, data scientists and engineers often spend the lion’s share of their time on various forms of “data cleaning” and much less on the “fun” part of the job.

There are many different levels to this kind of work and ways to prepare data for analysis, from checking for outliers in your data, to parsing dates, to determining the correct values in missing data.

# Cleansing data

At one level, cleaning data means ensuring accuracy and consistency of individual entries--each cell in a row of a table.

This can take the form of:
- ensuring consistent nomenclature
- identifying and addressing missing values
- removing duplicate entries
- correcting typos and removing additional spaces
- for text-based data, ensuring capitalization is consistent
- parsing dates and numbers
- correcting character encodings (for international data)

It is possible to use Python (and Pandas) to do these things, but programs like Excel will also have tools for each of these (Find & Replace, Remove Duplicates, etc.).

Performing basic descriptive statistics on a dataset can also help to flag extreme outliers that may be incorrect (negative values in a set of ages, for example). In Excel specifically, it helps to get comfortable using formulas like COUNT, MIN, MAX, and AVERAGE for numerical data, COUNTIF for text entries, or COUNTBLANK for empty cells.


It is essential to create unique numerical identifiers for a dataset (eg, using column A of a spreadsheet for consecutive ID numbers), so that, after sorting and re-sorting, the dataset can be restored to its original order with ease and certainty.

# Tidying data

In addition to “cleansing” a dataset of typos, inconsistencies, etc., a process called “tidying” is employed to correct its formatting. This is more involved and complicated than it might at first appear.

A “tidy” data structure has been defined by [Hadley Wickham](http://vita.had.co.nz/papers/tidy-data.html) as having the following qualities:
- Variables are arranged in columns: each variable forms a column and contains values
- Observations are arranged in rows: each observation forms a row
- Each type of observational unit forms a table

Thus, messy datasets may have issues such as:
- Columns without headers (or headers that are values, rather than the names of variables)
- More than one variable within a single column
- Variables stored in both rows and columns
- Several types of observational units in a single table
- A single observational unit stored across multiple tables

Most of these “messiness” issues can be solved with the following tools:
- Melting
- String splitting
- Casting

[<<< Back](9-datasets.md) - [Next >>>](10-usefulqueries.md)

