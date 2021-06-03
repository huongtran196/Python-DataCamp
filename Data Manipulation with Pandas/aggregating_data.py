# Summary statistics
import pandas as pd
import numpy as np

sales = pd.read_csv('sales.csv')

# Explore new Dataframe
print(sales.head())
print(sales.info())
print(sales['weekly_sales'].mean())
print(sales['weekly_sales'].median())

# Summarizing date
print(sales['date'].min())
print(sales['date'].max())

# Using .agg() method
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)

print(sales['temperature_c'].agg(iqr))
print(sales[['temperature_c', 'fuel_price_usd_per_l', 'unemployment']].agg(iqr))
print(sales[['temperature_c', 'fuel_price_usd_per_l', 'unemployment']].agg([iqr, np.median]))

# Cumulative statistics
sales_1_1 = pd.read_csv('sales_1_1')
sales_1_1 = sales_1_1.sort_values('date', ascending=True)
sales_1_1['cum_weekly_sales'] = sales_1_1['weekly_sales'].cumsum()
sales_1_1['cum_max_sales'] = sales_1_1['weekly_sales'].cummax()
print(sales_1_1[['date', 'weekly_sales', 'cum_weekly_sales', 'cum_max_sales']])

# Dropping duplicates
store_types = sales.drop_duplicates(subset=['store', 'type'])
print(store_types.head())

store_depts = sales.drop_duplicates(subset=['store', 'department'])
print(store_depts.head())

holiday_dates = sales[sales['is_holiday'] == True].drop_duplicates(subset='date')
print(holiday_dates['date'])

# Counting categorical variables
# Count the number of stores of each type
store_counts = store_types['type'].value_counts()
print(store_counts)

# Get the proportion of stores of each type
store_props = store_types['type'].value_counts(normalize = True)
print(store_props)

# Count the number of each department number and sort
dept_counts_sorted = store_depts['department'].value_counts(sort = True)
print(dept_counts_sorted)

# Get the proportion of departments of each number and sort
dept_props_sorted = store_depts['department'].value_counts(sort= True, normalize= True)
print(dept_props_sorted)

# What percent of sales occurred at each store type?
sales_all = sales["weekly_sales"].sum()

# Subset for type A, B, C stores, calc total weekly sales
sales_A = sales[sales["type"] == "A"]["weekly_sales"].sum()
sales_B = sales[sales['type'] == 'B']['weekly_sales'].sum()
sales_C = sales[sales['type'] == 'C']['weekly_sales'].sum()

# Get proportion for each type
sales_propn_by_type = [sales_A, sales_B, sales_C] / sales_all
print(sales_propn_by_type)

# Calculation with .groupby()
# Group by type; calc total weekly sales
sales_by_type = sales.groupby("type")["weekly_sales"].sum()
print(sales_by_type)

# Get proportion for each type
sales_propn_by_type = sales_by_type / sum(sales_by_type)
print(sales_propn_by_type)

# Group by type and is_holiday; calc total weekly sales
sales_by_type_is_holiday = sales.groupby(['type', 'is_holiday'])['weekly_sales'].sum()
print(sales_by_type_is_holiday)

# Multiple grouped summaries
# For each store type, aggregate weekly_sales: get min, max, mean, and median
sales_stats = sales.groupby('type')['weekly_sales'].agg([np.min, np.max, np.mean, np.median])

# Print sales_stats
print(sales_stats)

# For each store type, aggregate unemployment and fuel_price_usd_per_l: get min, max, mean, and median
unemp_fuel_stats = sales.groupby('type')[['unemployment', 'fuel_price_usd_per_l']].agg([np.min, np.max, np.mean, np.median])

# Print unemp_fuel_stats
print(unemp_fuel_stats)
