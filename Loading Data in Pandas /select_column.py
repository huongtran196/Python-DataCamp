# Selecting columns

import pandas as pd
credit_records = pd.read_csv('credit_records.csv')
item = credit_records['item']
item = credit_records.item
print(item)
location = credit_records['location']
print(location)

# Correcting column selection errors

mpr = pd.read_csv('mpr')
print(mpr.info())
dog_name = mpr['Dog Name']
missing = mpr['Missing?']
print(dog_name)
print(missing)