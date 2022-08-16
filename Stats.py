import pandas as pd

df = pd.read_csv('NDAn-prepared.csv')

print(df.head())

t=pd.unique(df['DO'])

t.sort()

print(t)