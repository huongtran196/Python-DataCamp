import pandas as pd
taxi_owners = pd.read_csv('taxi_owners.csv')
taxi_veh = pd.read_csv('taxi_veh.csv')

# Merge two tables taxi_owners and taxi_veh
taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid', suffixes=('_own', '_veh'))
print(taxi_own_veh)

# Find the most common fuel_type
print(taxi_own_veh['fuel_type'].value_counts())

wards = pd.read_csv('wards.csv')
census = pd.read_csv('census.csv')
wards_altered = pd.read_csv('wards_altered')
census_altered = pd.read_csv('census_altered.csv')

# Merge the first two tables
wards_census = wards.merge(census, on='ward')
print(wards_census)

print(wards_altered[['ward']].head())
wards_altered_census = wards_altered.merge(census, on='ward')
print('The table shape is ', wards_altered_census.shape)

print(census_altered[['ward']].head())
wards_census_altered = wards.merge(census_altered, on='ward')
print('This table shape is ', wards_census_altered.shape)
