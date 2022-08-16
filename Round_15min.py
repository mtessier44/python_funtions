import pandas as pd
import datetime

df = pd.read_csv('Lane_2_NH4_prepared_joined_prepared.csv')


l = []
for t in df['Time']:
    start = t[0:11]
    end = t[16:]
    hour = t[11:13]
    minute = t[14:16]

    if int(minute) > 7 and int(minute) <= 23:
        l += [start + hour +':15' + end]
    elif int(minute) > 23 and int(minute) <= 37:
        l += [start + hour +':30' + end]
    elif int(minute) > 37 and int(minute) <= 53:
        l += [start + hour + ':45' + end]
    else:

        if int(minute) <= 7:
            l += [start + hour + ':00' + end]
        else:
            hour = int(hour)
            hour += 1
            if hour == 24:
                hour = '00'
            elif hour < 10:
                hour = '0' + str(hour)
            else:
                hour = str(hour)

            l += [start + hour + ':00' + end]

print(l)
df['Time'] = l
df.to_csv('output.csv', index=False)
