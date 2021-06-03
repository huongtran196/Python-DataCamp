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

