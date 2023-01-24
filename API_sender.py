import pandas as pd
from requests import put, get
import threading
import time
import ast



# I got the data locally from a CSV file
df = pd.read_csv(r'C:\Users\micka\Dropbox\Cobalt Water\Development\API\API_short.csv')

# Dataframe convert to dictionary
dic_df = df.to_dict(orient='records')
# Format of each line:
# dic_example = {"time" : "2018-06-08T00:15:00.000Z", "DO" : 2.2, "NH4" : 3.1, "N2O" : 0.1, "NO3" : 4.2}

output = pd.DataFrame()

for d_s in dic_df:

    # Data sent every 2 secs in this case
    time.sleep(2)
    # Reformat dictionary
    d_s = str(d_s).replace("'",'"')
    # Check locally what is sent
    print("Data sent:")
    print(d_s)
    # Data sent to the API
    put('https://n2orisk-dev.eba-eknsupnb.us-east-1.elasticbeanstalk.com/api/v1/asset/test', data={'data': d_s})

    # Data received, we let 2 sec to apply the models
    time.sleep(2)
    m = get('https://n2orisk-dev.eba-eknsupnb.us-east-1.elasticbeanstalk.com/api/v1/asset/test')
    # Format data received
    d_r = m.text
    d_r = d_r.replace("\\", "")
    d_r = d_r.replace(r'{"test": "', "")
    d_r = d_r[:-3]
    d_r = ast.literal_eval(d_r)
    # Check locally what is received
    print("Data received:")
    print(d_r)
    # Save data received in the output dataframe
    output = output.append(d_r, ignore_index=True)

print(output)
output.to_csv(r'C:\Users\micka\Desktop\API_output.csv', index=False, sep=';')

