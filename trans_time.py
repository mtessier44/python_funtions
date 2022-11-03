import datetime
import dateutil.parser as parser
import pandas as pd


df = pd.read_csv('T5-P3-NO3-to-modify.csv')

df['Time'] = pd.to_datetime(df['Time'].astype(str)) + pd.DateOffset(minutes=1)

print(df['Time'])
df.to_csv('NO3-modified.csv')