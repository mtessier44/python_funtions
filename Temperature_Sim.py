import pandas as pd

df = pd.read_csv('Month_All.csv')

print(df.head())

Temp_list = []

for t in df['Month']:
    if t == 1:
        T = 11.0
    elif t == 2:
        T = 11.0
    elif t == 3:
        T = 11.6
    elif t == 4:
        T = 14.3
    elif t == 5:
        T = 17.1
    elif t == 6:
        T = 19.8
    elif t == 7:
        T = 21.5
    elif t == 8:
        T = 21.5
    elif t == 9:
        T = 19.8
    elif t == 10:
        T = 17.1
    elif t == 11:
        T = 13.1
    elif t == 12:
        T = 12.1
    Temp_list += [T]

df['Temperature'] = Temp_list
print(df.head())

df.to_csv('Sim-Tempeature-2022_Cog-Moors.csv')