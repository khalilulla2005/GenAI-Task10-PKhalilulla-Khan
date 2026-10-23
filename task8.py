import pandas as pd
import matplotlib
matplotlib.use('Agg') # Prevents GUI freezing
import matplotlib.pyplot as plt

print("--- Task 8: Pandas Plotting (Simple Graphs) ---")
df = pd.DataFrame({
    'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
    'Marks': [78, 85, 90, 66, 72]
})

# 1. Bar graph
df.plot(x='Name', y='Marks', kind='bar', title='Student Names vs Marks', color='skyblue')
plt.savefig('bar_graph.png')
plt.close()
print("1. Bar graph generated and saved as 'bar_graph.png'")

# 2. Line graph
df['Marks'].plot(kind='line', title='Marks Line Graph', marker='o')
plt.savefig('line_graph.png')
plt.close()
print("2. Line graph generated and saved as 'line_graph.png'")

# 3. Histogram
df['Marks'].plot(kind='hist', title='Marks Histogram', bins=5, edgecolor='black')
plt.savefig('histogram.png')
plt.close()
print("3. Histogram generated and saved as 'histogram.png'")
