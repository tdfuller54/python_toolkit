# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 17:27:20 2022

@author: tyson.fuller
"""
#Modified from themis script written by Derek Bickhart
#Really only seems to be of value to compare plots from different assemblies

import matplotlib
from matplotlib import pyplot as plt
matplotlib.use('Agg')
from matplotlib import cm
from itertools import cycle
from collections import defaultdict
import pandas
import numpy as np

#Get assembly short name
asms = ["Vvillosa"]
print(asms)

#Get FRC data for input
alist = ["C:/Users/tyson.fuller/OneDrive - USDA/Desktop/v_merged_frc.txt_FRC.txt"]
print(alist)

colors = [ '#bd2309', '#bbb12d', '#1480fa', '#14fa2f', '#000000',
          '#faf214', '#2edfea', '#ea2ec4', '#ea2e40', '#cdcdcd',
          '#577a4d', '#2e46c0', '#f59422', '#219774', '#8086d9' ]

# Start loading assemblies into dataframe
data = defaultdict(list)
for i, v in enumerate(alist):
    atext = asms[i]
    print(atext)
    print(v)
    with open(v, 'r') as input:
        for l in input:
            s = l.rstrip().split()
            data['asm'].append(atext)
            data['x'].append(float(s[0]))
            data['y'].append(float(s[1]))

df = pandas.DataFrame(data)
df
# Plot the FRC data
fig, ax = plt.subplots()
i = 0
for k, g in df.groupby(['asm']):
    #ax = g.plot(ax=ax, kind='line', x='x', y='y', c=colors[i], label=k)
    ax = g.plot(ax=ax, marker='', x='x', y='y', c=colors[i], linewidth=1, label=k)
    i += 1
plt.title("Feature Space")
plt.xlabel("Cumulative Errors")
plt.ylabel("Coverage (%)")
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('C:/Users/tyson.fuller/OneDrive - USDA/Desktop/v_frc.pdf', bbox_inches='tight')
plt.close()
