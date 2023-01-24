import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\micka\Desktop\API_output.csv', sep=';', low_memory=False)

print(df)

plt.plot(df['time'], df['N2O'], df['time'], df['N2O pred.'])
plt.show()