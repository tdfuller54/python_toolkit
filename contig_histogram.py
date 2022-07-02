# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 16:43:03 2022

@author: tyson.fuller
"""

import matplotlib
from matplotlib import pyplot as plt
matplotlib.use('Agg')
from matplotlib.collections import BrokenBarHCollection
from itertools import cycle
from collections import defaultdict
import pandas as pd
import numpy as np
import squarify

data = defaultdict(list)


with open('C:/Users/tyson.fuller/OneDrive - USDA/Desktop/Vvillosa.fa.fai', "r") as input:
    for l in input:
        s = l.rstrip().split()
        data['ctg'].append(s[0])
        data['len'].append(int(s[1]))
        
print(data)

df = pd.DataFrame(data)
df.head()
df = df.sort_values(by='len', ascending=False)
df.tail()
largestctg = df['len'].max()
largestctg
smallestctg = df['len'].min()
smallestctg
SN50 = 174244450
df.reset_index(drop=True)

#Get color scheme for treemap
norm = matplotlib.colors.Normalize(vmin=smallestctg, vmax=largestctg)
colors = [matplotlib.cm.hsv(norm(value)) for value in df.len]
len(colors)
#Generate plot
plt.hist(x=df.len)
plt.title("Assembly Scaffold TreeMap",fontsize=14,fontweight="bold")
plt.axis('off')
plt.tight_layout()
plt.savefig('scaffold_hist.pdf', bbox_inches='tight')
plt.close()
