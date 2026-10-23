import pandas as pd
print("--- Task 5: DataFrame Functions ---")
students = {'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'], 'Marks': [78, 85, 90, 66, 72], 'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']}
df = pd.DataFrame(students)
print("--- describe() ---")
print(df.describe().to_string())
sorted_df = df.sort_values(by='Marks', ascending=False)
print("Sorted by Marks:\n", sorted_df.to_string())
print("Reset Index:\n", sorted_df.reset_index(drop=True).to_string())