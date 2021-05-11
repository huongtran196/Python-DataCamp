#Loading & inspecting a DataFrame

import pandas as pd
credit_records = pd.read_csv(credit_records.csv)
print(credit_records.head(5))
print(credit_records.info())