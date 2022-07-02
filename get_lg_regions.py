# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 12:14:18 2022

@author: tyson.fuller
"""
import pandas as pd


data = pd.read_excel(r'C:/Users/tyson.fuller/OneDrive - USDA/Desktop/LG_marker_list.xlsx')
print(data)
type(data)

for col in data.columns:
    df = pd.DataFrame(data[col].dropna())
    print(df)
    l = list(df[col].values)
    print(l)
    print(type(l))
    text = []
    for v in l:
        print(v)
        d = v.split('_')
        print(d)
        d.append(int(d[2])-50)
        d.append(int(d[2])+50)
        t = d[0].replace("*S", "PGA_scaffold")
        line = f'{t}:{d[3]}-{d[4]}'
        text.append(line)
    group = "\n".join(text)
    with open(f'C:/Users/tyson.fuller/OneDrive - USDA/Desktop/{col}.txt', 'w') as file:
        file.write(group)

        

for i in lg1:
    print(i)
    d = i.split('_')
    print(d)

test = []
with open('C:/Users/tyson.fuller/OneDrive - USDA/Desktop/LG_marker_list.xlsx', "r") as text:
    for l in text:
        l = l.strip()
        #print(l)
        if l.startswith('>'):
            l = "_".join(l.split("_", 2)[:2])
            test.append(l)
        else:
            test.append(l)
    
    
#print(test)
fasta = "\n".join(test)
#print(fasta)
#type(fasta)

with open('C:/Users/tyson.fuller/OneDrive - USDA/Desktop/test2.txt', "w") as text2:
    text2.write(fasta)
    