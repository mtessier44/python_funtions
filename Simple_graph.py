import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\micka\PycharmProjects\pythonProject\SwanseaN2O_30mar_11apr_prepared.csv', sep=',',
                 low_memory=False)

print(df)

plt.plot(df['Time'], df['N2O'])
plt.show()