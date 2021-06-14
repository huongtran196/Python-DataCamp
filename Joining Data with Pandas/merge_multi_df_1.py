import pandas as pd

cal = pd.read_csv('calendar.csv')
ridership = pd.read_csv('ridership.csv')
stations = pd.read_csv('stations.csv')

ridership_cal = ridership.merge(cal, on=['year', 'month', 'day'])
print(ridership_cal)

ridership_cal_stations = ridership.merge(cal, on=['year', 'month', 'day']) \
                                .merge(stations, on='station_id')
print(ridership_cal_stations)

# Create filter criteria
filter_criteria = (ridership_cal_stations['station_name'] == 'Wilson')
                    & (ridership_cal_stations['day_type'] == 'Weekday')
                    & (ridership_cal_stations['month'] == 7)

# Filter rows with the previous condition and sum the ride column
print(ridership_cal_stations.loc[filter_criteria, 'ride'].sum())