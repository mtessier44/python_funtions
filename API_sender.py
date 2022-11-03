import pandas as pd
from requests import put
import threading
import time

#dic = {"time" : "2018-06-08T00:15:00.000Z", "DO" : 2.2, "NH4" : 3.1, "N2O" : 0.1, "NO3" : 4.2}

df = pd.read_csv(r'C:\Users\micka\Desktop\API.csv')
#df = df.append(dic, ignore_index=True)

#def hello_world():
#    threading.Timer(10.0, hello_world).start() # called every minute
#    print("Hello, World!")
#hello_world()

dic_df = df.to_dict(orient='records')

for t in dic_df:
    time.sleep(5)

    t = str(t).replace("'",'"')
    print(t)
    put('https://n2orisk-dev.eba-eknsupnb.us-east-1.elasticbeanstalk.com/api/v1/asset/test', data={'data': t})