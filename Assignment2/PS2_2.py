import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('2281305.csv', low_memory=False)[['DATE', "WND"]]
date = pd.to_datetime(df['DATE'])
month = date.dt.to_period('M')
df['DATE'] = month
wind = df['WND'].str.split(",")
data = []
for item in wind.values:
    data.append((float(item[3])/10))
speed = pd.Series(data, copy=False)
df['WND'] = speed
df_subset = df[['DATE', 'WND']].groupby('DATE').mean()['WND']
df_subset.plot(kind='bar')
plt.show()

