import pandas as pd
import csv
df=pd.read_csv('digital_behaviour.csv')
print(f'{df.head(5)}\n')
print(f'{df.tail(5)}\n')
print(f'{df.info()}\n')
print(f'{df.columns}\n')
print(f'{df['Instagram_Minutes']}\n')
print(f'{df[['Date','Instagram_Minutes']]}\n')
print(f'{df['Instagram_Minutes'].sum()}')
print(f'{df['Instagram_Minutes'].mean()}')
print(f'{df['Instagram_Minutes'].max()}')

