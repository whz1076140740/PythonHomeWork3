def input_mean(data,columns):
    data[columns]=data[columns].fillna(data[columns].mean())
    return data