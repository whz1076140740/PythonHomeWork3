import pandas as pd
def upload_csvfile(path):
    data=pd.read_csv(path)
    return data