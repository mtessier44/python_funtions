import pandas as pd
from requests import put, get
import threading
import time



# I got the data locally from a CSV file
df = pd.read_csv(r'C:\Users\micka\Dropbox\Cobalt Water\Development\API\API.csv')

# Dataframe convert to dictionnary
dic_df = df.to_dict(orient='records')
# Format of each line:
# dic_example = {"time" : "2018-06-08T00:15:00.000Z", "DO" : 2.2, "NH4" : 3.1, "N2O" : 0.1, "NO3" : 4.2}

for d_s in dic_df:

    # Data sent every 5 secs in this case
    time.sleep(5)
    # Reformat dictionary
    d_s = str(d_s).replace("'",'"')
    # Check locally what is sent
    print(d_s)
    # Data sent to the API
    put('https://n2orisk-dev.eba-eknsupnb.us-east-1.elasticbeanstalk.com/api/v1/asset/test', data={'data': d_s})

    # Data received, we let 5 sec to apply the models
    time.sleep(5)
    m = get('https://n2orisk-dev.eba-eknsupnb.us-east-1.elasticbeanstalk.com/api/v1/asset/test')
    # Format data received
    d_r = m.text
    d_r = d_r.replace("\\", "")
    d_r = d_r.replace(r'{"test": "', "")
    # Check locally what is received
    print(d_r)
