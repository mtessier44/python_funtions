import datetime
import dateutil.parser as parser

#text = '1/2/2021 00:00'
text = 'Mon Mar 07 2022 11:30:22 GMT+0000'
#date = parser.parse(text)
date = parser.parse(text, dayfirst=True)

#Addition of one day
date += datetime.timedelta(seconds=1)
print(date.isoformat())

import pandas as pd
from os import listdir
from os.path import isfile, join

path_datasets = r'C:\Users\micka\Desktop\Laighpark WWTW data transfer'
path_export = r'C:\Users\micka\Desktop\Laighpark WWTW data transfer\export'
list_datasets = [f for f in listdir(path_datasets) if isfile(join(path_datasets, f))]

print(list_datasets)

for t in list_datasets:
    with open(path_datasets + '/' + t,'r') as f:
        with open(path_export + '/' + t,'w') as f1:
            next(f) # skip header line
            for line in f:
                f1.write(line)

    df = pd.read_csv(path_export + '/' + t)
    df['Timestamp'] = df['Timestamp'].str.replace(' (Greenwich Mean Time)', '', regex=False)
    df['Timestamp'] = df['Timestamp'].str.replace(' (British Summer Time)', '', regex=False)
    df = df.rename(columns={"Timestamp": "Time"})
    df['Time'] = df['Time'].apply(parser.parse)
    df.to_csv(path_export + '/' + t)
#df['Time'] = df['Time'].apply(parser.parse)
#df.to_csv('Chicago-Temp-Modified.csv')