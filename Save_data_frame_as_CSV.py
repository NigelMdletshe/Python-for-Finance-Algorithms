# How to save a dataframe as CSV

import pandas as pd

# Data 

d = [['Sara',34],['Mike',32],['Zara',55]]

df = pd.DataFrame(d,columns=['Name','Age'])

print(df)

df.to_csv('Df.csv')