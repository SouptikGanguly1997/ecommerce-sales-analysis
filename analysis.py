import pandas as pd
import numpy as np

data = {
    "name": ["Rahul", "Priya", "Ankit", "Sneha", "Vikram", "Aman"],
    "amount": [55000, 2500, 67000, 52000, 3000, 45000],
    "city": ["Kolkata", "Delhi", "Mumbai", "Kolkata", "Delhi", "Mumbai"]
}

df = pd.DataFrame(data)

# Export to CSV
df.to_csv("sales_data.csv", index=False)


## 1. Total Revenue
total_revenue = df['amount'].sum()
print(f"Total Revenue: {total_revenue}\n")


## 2. Top Customer
# Sorting or filtering works, but idxmax is very efficient for single top records
top_customer = df.loc[[df['amount'].idxmax()], ['name', 'amount']]
print("Top Customer:")
print(top_customer.to_string(index=False), "\n")


## 3. City with Highest Revenue
# Grouping once and reusing the result is better for performance
city_totals = df.groupby('city')['amount'].sum()
top_city = city_totals.idxmax()
print(f"City with most revenue: {top_city}\n")


## 4. Customer Segmentation
conditions = [
    (df['amount'] >= 60000),
    (df['amount'] >= 30000), # Simple logic: if it fails the first, it checks this
    (df['amount'] < 30000)
]
choices = ['VIP', 'Regular', 'Low']

df['category'] = np.select(conditions, choices, default='Other')
print("Customer Segmentation:")
print(df.to_string(index=False), "\n")


## 5. Revenue Distribution by City
# Calculating percentage directly on the grouped object
city_dist = city_totals.reset_index()
city_dist['percentage'] = (city_dist['amount'] / total_revenue * 100).round(2)
city_dist = city_dist.sort_values(by='amount', ascending=False)

print("Revenue Distribution by City:")
print(city_dist.to_string(index=False))