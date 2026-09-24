import pandas as pd
import csv
df=pd.read_csv('digital_behaviour.csv')
df.head(5)
df.tail(5)
df.info()
df.columns
df['Instagram_Minutes']
df[['Date','Instagram_Minutes']]
df['Instagram_Minutes'].sum()
df['Instagram_Minutes'].mean()
df['Instagram_Minutes'].max()

