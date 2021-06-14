# One-to-many merge
import pandas as pd
licenses = pd.read_csv('licenses.csv')
biz_owners = pd.read_csv('biz_owners.csv')

licenses_owners = licenses.merge(biz_owners, on='account')
counted_df = licenses_owners.groupby('title').agg({'account':'count'})
sorted_df = counted_df.sort_values('account', ascending=False)
print(sorted_df.head())
