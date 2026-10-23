import pandas as pd
print("--- Task 1: Pandas Series Basics ---")
marks = pd.Series([78, 85, 90, 66, 72])
print("Values:
", marks.values)
print("Index:
", marks.index)
print("Data Type:", marks.dtype)
print("
First element:", marks.iloc[0])
print("Last two elements:
", marks.iloc[-2:].to_string())
