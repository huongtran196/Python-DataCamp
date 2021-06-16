import pandas as pd

iron_1_actors = pd.read_csv('Iron_Man_1.csv')
iron_2_actors = pd.read_csv('Iron_Man_2.csv')

iron_1_and_2 = iron_1_actors.merge(iron_2_actors,
                                     on='id',
                                     how='outer',
                                     suffixes=('_1', '_2'))
m = ((iron_1_and_2['name_1'].isnull()) | 
     (iron_1_and_2['name_2'].isnull()))
     
print(iron_1_and_2[m].head())