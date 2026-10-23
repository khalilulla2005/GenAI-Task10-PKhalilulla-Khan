import pandas as pd
print("--- Task 2: Mathematical Operations ---")
marks = pd.Series([78, 85, 90, 66, 72])
print("Original:\n", marks.to_string())
print("Add 5:\n", (marks + 5).to_string())
print("Subtract 2:\n", (marks - 2).to_string())
print("Multiply by 1.05:\n", (marks * 1.05).to_string())
print("Divide by 2:\n", (marks / 2).to_string())