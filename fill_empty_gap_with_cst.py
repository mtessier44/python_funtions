import pandas as pd
import math

df = pd.read_csv('Temperature_making.csv')

print(df.head())
Temp_list = df['Temperature']

s=0
New_Temp_list = []
for t in Temp_list:
    if math.isnan(t):
        New_Temp_list+=[s]
    else:
        s = t
        New_Temp_list += [s]

df['Temperature'] = New_Temp_list
df.to_csv('Temperature-hourly-Sim.csv')