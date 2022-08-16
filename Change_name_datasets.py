import pandas as pd
import numpy as np
from os import listdir
from os.path import isfile, join

path_datasets = r'C:\Users\micka\Desktop\Nash\Nash Data\DO september 2021'

list_datasets = [f for f in listdir(path_datasets) if isfile(join(path_datasets, f))]

print(list_datasets)

dic = {'1E87391.csv': 'L3-DO2',
       '1E87392.csv': 'L4-DO1',
       '1E87393.csv': 'L4-DO2',
       '1E87394.csv': 'L5-DO1',
       '1E87395.csv': 'L5-DO2',
       '1E87396.csv': 'L6-DO1',
       '1E87397.csv': 'L6-DO2',
       '1E87398.csv': 'L7-DO1',
       '1E87399.csv': 'L7-DO2',
       '1E87400.csv': 'L8-DO1',
       '1E87401.csv': 'L8-DO2',
       '1E87402.csv': 'L9-DO1',
       '1E87403.csv': 'L9-DO2'}

for t in dic:
    df_read = pd.read_csv(path_datasets + '/' + t, sep=',', low_memory=False)
    print(dic[t])
    df_read.to_csv(path_datasets + '/' + dic[t] + '-0921.csv', index=False)