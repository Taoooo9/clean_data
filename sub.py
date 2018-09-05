import re

error_path = './error.txt'
symbol = './symbol'
data = []
data1 = []
data2 = {}

with open(error_path, encoding = 'utf-8') as f:
    for error in f:
        data.append(error)
        print('string' + '=' + 're.sub(' + error + ',' + '""' + ',' + 'string)', '\n')
    print(data)

with open(symbol, encoding = 'utf-8') as f:
    for symbol in f:
        data1.append(symbol)
    print(data1)



