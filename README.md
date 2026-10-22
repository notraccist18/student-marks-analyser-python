# Student Marks Analyser (Python)

I made this project to practise working with CSV files in Python. It reads the marks of students from `marks.csv` and makes a simple report.

## What it does
- Reads Name, Maths, Physics and English marks from a CSV file
- Calculates total, average and grade for every student
- Finds the class topper and the class average
- Saves a report in `report.txt`

## Concepts I used
- CSV file reading with `DictReader`
- Lists of dictionaries
- Functions — I made a separate function for grade calculation
- Basic statistics (total and average)

## How to run
First check that `marks.csv` is in the same folder, then:
```
python marks_analyser.py
```
You can change the names and marks in `marks.csv` and run it again with your own class data.

## What I want to add later
- Subject-wise topper
- A bar chart of averages
