# Assignment 10: Pandas

This assignment demonstrates data manipulation, filtering, grouping, and basic plotting using the Pandas library.

## Folder Structure
GenAI-Task10-PKhalilulla-Khan/
├── task1.py
├── task2.py
├── task3.py
├── task4.py
├── task5.py
├── task6.py
├── task7.py
├── task8.py
├── task9.py
└── README.md

## Code Execution Output

### Task 1
```text
--- Task 1: Pandas Series Basics ---
Series Values:
 [78 85 90 66 72]
Index:
 RangeIndex(start=0, stop=5, step=1)
Data Type: int64
First element: 78
Last two elements:
 3    66
4    72
```

### Task 2
```text
--- Task 2: Mathematical Operations ---
Original:
 0    78
1    85
2    90
3    66
4    72
Add 5:
 0    83
1    90
2    95
3    71
4    77
Subtract 2:
 0    76
1    83
2    88
3    64
4    70
Multiply by 1.05:
 0    81.90
1    89.25
2    94.50
3    69.30
4    75.60
Divide by 2:
 0    39.0
1    42.5
2    45.0
3    33.0
4    36.0
```

### Task 3
```text
--- Task 3: Python Functionalities ---
Max: 90 | Min: 66 | Sum: 391 | Mean: 78.2
Passed (True/False):
 0     True
1     True
2     True
3    False
4     True
Number of students passed: 4
```

### Task 4
```text
--- Task 4: Create a DataFrame ---
First 3 rows:
     Name  Marks  Subject
0   Amit     78     Math
1   Neha     85     Math
2  Rahul     90  Science
Last 2 rows:
     Name  Marks  Subject
3  Sneha     66  Science
4  Pooja     72     Math
Shape: (5, 3)
Columns: ['Name', 'Marks', 'Subject']
```

### Task 5
```text
--- Task 5: DataFrame Functions ---
--- describe() ---
           Marks
count   5.000000
mean   78.200000
std     9.654015
min    66.000000
25%    72.000000
50%    78.000000
75%    85.000000
max    90.000000
Sorted by Marks:
     Name  Marks  Subject
2  Rahul     90  Science
1   Neha     85     Math
0   Amit     78     Math
4  Pooja     72     Math
3  Sneha     66  Science
Reset Index:
     Name  Marks  Subject
0  Rahul     90  Science
1   Neha     85     Math
2   Amit     78     Math
3  Pooja     72     Math
4  Sneha     66  Science
```

### Task 6
```text
--- Task 6: Filtering ---
Marks > 75:
     Name  Marks  Subject
0   Amit     78     Math
1   Neha     85     Math
2  Rahul     90  Science
Subject Math:
     Name  Marks Subject
0   Amit     78    Math
1   Neha     85    Math
4  Pooja     72    Math
Marks > Average (78.20):
     Name  Marks  Subject
1   Neha     85     Math
2  Rahul     90  Science
Failed (< 70):
     Name  Marks  Subject
3  Sneha     66  Science
```

### Task 7
```text
--- Task 7: Grouping ---
Average per subject:
 Subject
Math       78.333333
Science    78.000000
Count per subject:
 Subject
Math       3
Science    2
Max per subject:
 Subject
Math       85
Science    90
```

### Task 8
```text
--- Task 8: Plotting ---
1. Bar graph saved as 'bar_graph.png'
2. Line graph saved as 'line_graph.png'
3. Histogram saved as 'histogram.png'
```

### Task 9
```text
--- Task 9: Sales Analysis ---
   Day  Revenue
0  Mon     1200
1  Tue     1500
2  Wed      900
3  Thu     2000
4  Fri     1800
Total revenue: 7400
Average revenue: 1480.00
Highest day: Thu
Days > average:
    Day  Revenue
1  Tue     1500
3  Thu     2000
4  Fri     1800
Plot saved as 'revenue_plot.png'
```

