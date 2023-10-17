def binary(data,columns,value_for_1,value_for_0):
    data[columns]=data[columns].map({value_for_1:1,value_for_0:0})
    return data

