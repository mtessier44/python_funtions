import pandas as pd
import joblib

row_dic = {'DO': 0.2, 'NH4': 0.3, 'NO3': 0.7}

X = pd.DataFrame([row_dic], columns=row_dic.keys())
print(X)