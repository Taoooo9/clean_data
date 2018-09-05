import re


file_path = './phones_result2.txt'
data = []
data1 = []
with open(file_path, encoding = 'utf-8') as f:
    p = re.compile(r"&[a-zA-Z]+;")
    p1 = re.compile(r'&#[0-9]+;')
    for line in f.readlines():
        #print('p:', p.findall(line))
       # print('\np1:', p1.findall(line))
        if p.findall(line):
            data.append(p.findall(line))
        if p1.findall(line):
            data.append(p1.findall(line))
    for i in data:
        for j in i:
            data1.append(j)
    data2 = set(data1)
    print(data2, '\n', len(data2))
