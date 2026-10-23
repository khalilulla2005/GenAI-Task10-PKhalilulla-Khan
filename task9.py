import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

print("--- Task 9: Mini Use Case: Sales Data Analysis ---")
sales = pd.DataFrame({
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    'Revenue': [1200, 1500, 900, 2000, 1800]
})
print("Sales Data:
", sales.to_string(), "
")

print("1. Total revenue:", sales['Revenue'].sum())
avg_rev = sales['Revenue'].mean()
print(f"2. Average daily revenue: {avg_rev:.2f}")

max_day = sales.loc[sales['Revenue'].idxmax(), 'Day']
print("3. Day with highest revenue:", max_day)

above_avg = sales[sales['Revenue'] > avg_rev]
print("4. Days where revenue > average:
", above_avg.to_string())

sales.plot(x='Day', y='Revenue', kind='line', marker='o', title='Revenue vs Day', color='green')
plt.savefig('revenue_plot.png')
plt.close()
print("
5. Revenue vs Day plot generated and saved as 'revenue_plot.png'")
