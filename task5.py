import pandas as pd

print("--- Task 5: Important DataFrame Functions ---")
students = {
    'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
    'Marks': [78, 85, 90, 66, 72],
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']
}
df = pd.DataFrame(students)

print("--- info() ---")
df.info()

print("
--- describe() ---")
print(df.describe().to_string())

print("
--- head() ---")
print(df.head().to_string())

print("
--- tail() ---")
print(df.tail().to_string())

sorted_df = df.sort_values(by='Marks', ascending=False)
print("
Sorted by Marks (Descending):
", sorted_df.to_string())

reset_df = sorted_df.reset_index(drop=True)
print("
After Resetting Index:
", reset_df.to_string())
