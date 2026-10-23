import pandas as pd
print("--- Task 7: Grouping ---")
students = {'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'], 'Marks': [78, 85, 90, 66, 72], 'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']}
df = pd.DataFrame(students)
print("Average per subject:\n", df.groupby('Subject')['Marks'].mean().to_string())
print("Count per subject:\n", df.groupby('Subject')['Name'].count().to_string())
print("Max per subject:\n", df.groupby('Subject')['Marks'].max().to_string())