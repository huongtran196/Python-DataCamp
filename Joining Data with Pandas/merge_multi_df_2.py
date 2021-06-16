import pandas as pd

land_use = pd.read_csv('land_use.csv')
census = pd.read_csv('census.csv')
licenses = pd.read_csv('licenses.csv')

land_cen_lic = land_use.merge(census, on='ward') \
                    .merge(licenses, on='ward', suffixes=('_cen', '_lic'))
pop_vac_lic = land_cen_lic.groupby(['ward', 'pop_2010', 'vacant'], 
                                   as_index=False).agg({'account':'count'})
sorted_pop_vac_lic = pop_vac_lic.sort_values(['vacant', 'account', 'pop_2010'], 
                                             ascending=[False, True, True])
print(sorted_pop_vac_lic.head())