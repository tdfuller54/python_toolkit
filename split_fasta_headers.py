# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 12:14:18 2022

@author: tyson.fuller
"""
test = []
with open('C:/Users/tyson.fuller/OneDrive - USDA/Desktop/test.txt', "r") as text:
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
    
