import pandas as pd

dic = {"time" : "2018-06-08T00:15:00.000Z", "DO" : 2.2, "NH4" : 3.1, "N2O" : 0.1, "NO3" : 4.2}

df = pd.read_csv(r'C:\Users\micka\Desktop\Real-Time.csv')


print(df)

df = df.append(dic, ignore_index=True)
print(df)