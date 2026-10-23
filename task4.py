import pandas as pd
print("--- Task 4: Create a DataFrame ---")
students = {'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'], 'Marks': [78, 85, 90, 66, 72], 'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']}
df = pd.DataFrame(students)
print("First 3 rows:\n", df.head(3).to_string())
print("Last 2 rows:\n", df.tail(2).to_string())
print("Shape:", df.shape)
print("Columns:", list(df.columns))