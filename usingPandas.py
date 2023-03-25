import pandas as pd
# turn csv into a data frame 
df = pd.read_csv('BTC-USD.csv')
print(df)

#------drop a column in pandas
#df = df.drop('Adj Close',1)
#print(df)

#-----How to rename a column in pandas
#df.rename(columns= {'Volume':'Vol','Date':'Time'}, inplace = True)
#print(df)

#-------- How to change the index in pandas?
df = df.set_index('Date')
print(df)

# How to reset the index in pandas?
df = df.reset_index()
print(df)

# How to make a dataframe from scratch
df2 = pd.DataFrame({
    'name':['Jon','Jon','Sara','Mindy','Mindy'],
    'thing':['food','food','food','chair','chair'],
    'rating':[5,5,6,22,7] 
})

print(df2)

#----How to drop duplicates in pandas
df2 = df2.drop_duplicates()
print(df2)
print('')
print('----')

# Drop duplicates based on columns
df2 = df2.drop_duplicates(subset = ['name'])
print(df2)
print('*====*')


#How to group in pandas
df = pd.DataFrame({'food':['chicken','chicken','bacon','ranch'],
                    'cals':[500.,390.,600.,52.]})
print(df)

print(" ")
print('*====*')

df = df.groupby(['food']).mean()
print(df) 

print(" ")
print('*====*')
#How to filter in python
#Use operators for numbers.
df2 = df2[df2.High > 4500]
print(df2)

#use multiple operators 
df1 = df2[(df2.High > 6500) | (df2.Volume ==  21056800) ]
print(df1) # returns empty data frame
print(" ")
print('*====*')

#Filter with a list
highs = [468.174011,427.834991,456.859985,423.295990,412.425995]
df = df2[df2.High.isin(highs)]
print(df) # messed up the dfs somewhere


#watch video again

# soetimes w ewant the largets and smallest

print(df)
#read on Pandas

# how to sort in Pandas

# Read in an XLSL excel
#df = pd.read_excel('name+extension',index_col = 0)
#print(pd)

# you will get an error, you need to pip install in terminal
# pip instal openpyxl
