import pandas as pd
from os import listdir
from os.path import isfile, join

path_datasets = r'C:\Users\micka\Desktop\Nash 120722\Convertor_folder'
path_export = r'C:\Users\micka\Desktop\Nash 120722\Export_folder'
Target = '1E87382'

list_datasets = [f for f in listdir(path_datasets) if isfile(join(path_datasets, f))]

for t in list_datasets:

    xls = pd.ExcelFile(path_datasets + '/' + t)
    print(xls.sheet_names)
    df_read = pd.read_excel(xls, Target)
    df_read.to_csv(path_export + '/' + t[:-4] + '_' + Target + '.csv', index=False)


