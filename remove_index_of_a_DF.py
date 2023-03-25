# Remove index of a DF

import pandas as pd

df=pd.read_csv('BTC-USD.csv')
print(df) #Works

new_df = pd.DataFrame()
new_df['Date'] = df['Date']
new_df['Open'] = df['Open']

print(new_df)

#remove index

new_df.to_csv('new_df.csv',index = False)
#open file from explorer
