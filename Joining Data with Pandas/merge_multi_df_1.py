import pandas as pd

cal = pd.read_csv('calendar.csv')
ridership = pd.read_csv('ridership.csv')
stations = pd.read_csv('stations.csv')

ridership_cal = ridership.merge(cal, on=['year', 'month', 'day'])
print(ridership_cal)

ridership_cal_stations = ridership.merge(cal, on=['year', 'month', 'day']) \
                                .merge(stations, on='station_id')
print(ridership_cal_stations)