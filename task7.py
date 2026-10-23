import pandas as pd

print("--- Task 7: Grouping & Basic Analysis ---")
students = {
    'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
    'Marks': [78, 85, 90, 66, 72],
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']
}
df = pd.DataFrame(students)

print("1. Average marks per subject:
", df.groupby('Subject')['Marks'].mean().to_string(), "
")
print("2. Count of students per subject:
", df.groupby('Subject')['Name'].count().to_string(), "
")
print("3. Maximum marks per subject:
", df.groupby('Subject')['Marks'].max().to_string())
