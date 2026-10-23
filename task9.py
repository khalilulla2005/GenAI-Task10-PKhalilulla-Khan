import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
print("--- Task 9: Sales Analysis ---")
sales = pd.DataFrame({'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'], 'Revenue': [1200, 1500, 900, 2000, 1800]})
print(sales.to_string())
print("Total revenue:", sales['Revenue'].sum())
avg_rev = sales['Revenue'].mean()
print(f"Average revenue: {avg_rev:.2f}")
print("Highest day:", sales.loc[sales['Revenue'].idxmax(), 'Day'])
print("Days > average:\n", sales[sales['Revenue'] > avg_rev].to_string())
sales.plot(x='Day', y='Revenue', kind='line').get_figure().savefig('revenue_plot.png')
plt.close()
print("Plot saved as 'revenue_plot.png'")