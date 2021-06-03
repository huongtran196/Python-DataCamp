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

