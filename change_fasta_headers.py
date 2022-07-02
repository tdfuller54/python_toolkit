# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 12:14:18 2022

@author: tyson.fuller
"""
test = []
i = 1
with open('C:/Users/tyson.fuller/OneDrive - USDA/Desktop/LG7_probe.fa', "r") as text:
    for l in text:
        l = l.strip()
        #print(l)
        if l.startswith('>'):
            l = f'>LG7.{i}'
            print(l)
            test.append(l)
            i += 1
        else:
            test.append(l)
  
    
print(test)
fasta = "\n".join(test)
print(fasta)
#type(fasta)

with open('C:/Users/tyson.fuller/OneDrive - USDA/Desktop/LG_probes.fa', "w") as text2:
    text2.write(fasta)
    
