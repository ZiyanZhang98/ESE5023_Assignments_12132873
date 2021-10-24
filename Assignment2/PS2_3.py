import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel('总降水量.xlsx', sheet_name='鼎湖山')
df['year'] = df['年']
df['month'] = df['月']
df['day'] = df['日']
df['hour'] = df['时']
df['minute'] = df['分']
df = df[['year', 'month', 'day', 'hour', 'minute', '降水量']]
df = df[df['降水量'] > -1]
time = pd.to_datetime(df[['year', 'month', 'day', 'hour', 'minute']])
df['time'] = time
df = df[['time', '降水量']]
print(df.head())

print('max rainfall per minute:', end='\n')
print(df.sort_values('降水量', ascending=False).head(1))


month = time.dt.to_period('M')
df['time'] = month
df_subset = df.groupby('time').sum()['降水量'].sort_values(ascending=False)
print(df_subset.head())
print(df_subset.head(1))


day = time.dt.to_period('D')
df['time'] = day
df_subset = df.groupby('time').mean()['降水量']
print(df_subset.head())
print(df_subset.head(1))
df_subset.plot()
plt.show()