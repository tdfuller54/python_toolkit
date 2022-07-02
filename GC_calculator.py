# -*- coding: utf-8 -*-
"""
Created on Wed May  4 13:34:51 2022

@author: tyson.fuller
"""

from Bio import SeqIO
from Bio.SeqUtils import GC
import pandas as pd

filepath = 'C:/Users/tyson.fuller/OneDrive - USDA/Desktop/Vvillosa.fa'

assembly = []
i = 0
with open(filepath, "r") as text:
    for l in text:
        l = l.strip()
        #print(l)
        if l.startswith('>'):
            i += 1
        else:
            assembly.append(l)
            
asmstring = "".join(assembly)
assembly[0]
assembly[2]
print(i)
asmstring[:160]
assembly
len(asmstring)

c_count = asmstring.count("C")
g_count = asmstring.count("G")
t_count = asmstring.count("T")
a_count = asmstring.count("A")
n_count = asmstring.count("n")
c_count + g_count + t_count + a_count + n_count

gc_percent = ((c_count + g_count)/len(asmstring)) * 100
gc_percent = round(gc_percent, 2)
gc_percent


outfile='C:/Users/tyson.fuller/OneDrive - USDA/Desktop/Vvillosa_GC.txt'

with open(outfile, "w") as out:
    out.write("GC Content (%)\n")
    out.write(f'{gc_percent}\n')