import pandas as pd

print("--- Task 6: Filtering & Conditional Selection ---")
students = {
    'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
    'Marks': [78, 85, 90, 66, 72],
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']
}
df = pd.DataFrame(students)

print("1. Students > 75 marks:
", df[df['Marks'] > 75].to_string(), "
")
print("2. Subject = Math:
", df[df['Subject'] == 'Math'].to_string(), "
")

avg = df['Marks'].mean()
print(f"3. Students > Average ({avg:.2f}):
", df[df['Marks'] > avg].to_string(), "
")
print("4. Failed students (< 70):
", df[df['Marks'] < 70].to_string())
