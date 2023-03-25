# Find minum and maximum values in a DF

import pandas as pd

df = pd.read_csv('BTC-USD.csv')
print(df)

max_value=df['High'].max()
print(max_value)
# 68789.625

min_value = df['Low'].min()
print(min_value)
# 171.509995
