#create data-frames in python
import pandas as pd

school_data = [['John',16],['Bob',18],['Sherry',17]]

df = pd.DataFrame(school_data, columns = ['Name','Age'])
print(df)


