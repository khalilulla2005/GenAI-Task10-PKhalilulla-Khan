import pandas as pd

print("--- Task 2: Mathematical Operations on Series ---")
marks = pd.Series([78, 85, 90, 66, 72])
print("Original Marks:
", marks.to_string(), "
")

print("1. Add 5:
", (marks + 5).to_string(), "
")
print("2. Subtract 2:
", (marks - 2).to_string(), "
")
print("3. Multiply by 1.05:
", (marks * 1.05).to_string(), "
")
print("4. Divide by 2:
", (marks / 2).to_string())
