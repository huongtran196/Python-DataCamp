# Finding missing value
import pandas as pd
import matplotlib.pyplot as plt

avocados = pd.read_csv('avocados_sales.csv')
avocados_2016 = avocados[avocados['year'] == '2016']
# Check individual values for missing values
print(avocados_2016.isna())

# Check each column for missing values
print(avocados_2016.isna().any())

# Bar plot of missing values by variable
avocados_2016.isna().sum().plot(kind='bar')

# Show plot
plt.show()

# Removing missing values
avocados_complete = avocados_2016.dropna()

# Check if any columns contain missing values
print(avocados_complete.isna().any())