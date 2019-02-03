# csv-to-sql-extractor

*A script that extracts a csv file into an sqlite database*

## Installing

Plain and simple: Clone the repository to your machine.

This project is based on Python's standard library, i.e., it does not use any external package (_batteries included!_). It was mainly developed using a Python3.7 virtual environment, even though it was eventually tested using Python 2.7, and worked on both versions.

## Running

```
usage: extractor.py [-h] csv_file
```

The script will export the csv entries into an sqlite database that is named after <i>csv\_file</i>. For example, `extractor.py samples/valid_input.csv` will gerenate a `valid_input.csv.db` file.

Sample csv files are available in the samples/ directory.

## Decisions and assumptions

* I am using Python's argparser library in order to parse and validate the command line arguments
* In order to process the csv file, I started doing it manually via generator/list comprehensions. However, I decided replacing it by Python's own csv module, which might be more versatile and adaptative to other csv formats
* The csv format is fixed and matches a table that is pre-created via the script itself (`create table if not exists person ( time timestamp, name varchar, age integer)`)
* The database unique key is the timestamp
* Database insertions are made via `insert or ignore`, which means the script is idempotent: running it twice will neither raise errors nor generate new insertions
