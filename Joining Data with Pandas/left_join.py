import pandas as pd

movies = pd.read_csv('movies.csv')
financials = pd.read_csv('financials')

movies_financials = movies.merge(financials, on='id', how='left')
missing_value = movies_financials['budget'].isna().sum()