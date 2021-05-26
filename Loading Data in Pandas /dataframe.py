#Loading & inspecting a DataFrame

import pandas as pd
credit_records = pd.read_csv(credit_records.csv)
print(credit_records.head(5))
print(credit_records.info())

# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = { 'country': names, 'drives_right': dr, 'cars_per_cap': cpc}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)
print(cars)
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels
print(cars)