import pandas as pd 

def remove_nan_rows(data, columns):
     return data.dropna(subset=columns)
