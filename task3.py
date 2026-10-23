import pandas as pd
print("--- Task 3: Python Functionalities ---")
marks = pd.Series([78, 85, 90, 66, 72])
print("Max:", marks.max(), "| Min:", marks.min(), "| Sum:", marks.sum(), "| Mean:", marks.mean())
passed = marks.apply(lambda x: x >= 70)
print("Passed (True/False):\n", passed.to_string())
print("Number of students passed:", passed.sum())