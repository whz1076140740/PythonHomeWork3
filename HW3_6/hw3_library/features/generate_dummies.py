import pandas as pd 

def generate_dummies(data,columns):
    dummies=pd.get_dummies(data[columns], prefix=columns)
    data = pd.concat([data,dummies],axis=1)
    data.drop(columns,axis=1)
    return data