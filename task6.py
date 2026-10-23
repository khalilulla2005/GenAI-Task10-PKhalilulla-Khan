import pandas as pd
print("--- Task 6: Filtering ---")
students = {'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'], 'Marks': [78, 85, 90, 66, 72], 'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']}
df = pd.DataFrame(students)
print("Marks > 75:\n", df[df['Marks'] > 75].to_string())
print("Subject Math:\n", df[df['Subject'] == 'Math'].to_string())
avg = df['Marks'].mean()
print(f"Marks > Average ({avg:.2f}):\n", df[df['Marks'] > avg].to_string())
print("Failed (< 70):\n", df[df['Marks'] < 70].to_string())