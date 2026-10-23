import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
print("--- Task 8: Plotting ---")
df = pd.DataFrame({'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'], 'Marks': [78, 85, 90, 66, 72]})
df.plot(x='Name', y='Marks', kind='bar').get_figure().savefig('bar_graph.png')
plt.close()
print("1. Bar graph saved as 'bar_graph.png'")
df['Marks'].plot(kind='line').get_figure().savefig('line_graph.png')
plt.close()
print("2. Line graph saved as 'line_graph.png'")
df['Marks'].plot(kind='hist').get_figure().savefig('histogram.png')
plt.close()
print("3. Histogram saved as 'histogram.png'")