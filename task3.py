import pandas as pd

print("--- Task 3: Python Functionalities on Series ---")
marks = pd.Series([78, 85, 90, 66, 72])
print("Maximum marks:", marks.max())
print("Minimum marks:", marks.min())
print("Sum of marks:", marks.sum())
print("Mean marks:", marks.mean(), "
")

passed = marks.apply(lambda x: x >= 70)
print("Passed students (True/False):
", passed.to_string(), "
")
print("Number of students passed:", passed.sum())
