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

data = defaultdict(list)


with open('C:/Users/tyson.fuller/OneDrive - USDA/Desktop/Vvillosa.fa.fai', "r") as input:
    for l in input:
        s = l.rstrip().split()
        data['asm'].append("Vvillosa")
        data['len'].append(int(s[1]))

with open('C:/Users/tyson.fuller/OneDrive - USDA/Desktop/CowPea.fa.fai', "r") as input:
    for l in input:
        s = l.rstrip().split()
        data['asm'].append("CowPea")
        data['len'].append(int(s[1]))
        
print(data)

df = pd.DataFrame(data)
df.head()
df = df.sort_values(by=['asm', 'len'], ascending=(True, False))
df.tail()
largestctg = df['len'].max()
largestctg
smallestctg = df['len'].min()
smallestctg
df.reset_index(drop=True, inplace=True)

colors = [ '#bd2309', '#bbb12d', '#1480fa', '#14fa2f', '#000000',
          '#faf214', '#2edfea', '#ea2ec4', '#ea2e40', '#cdcdcd',
          '#577a4d', '#2e46c0', '#f59422', '#219774', '#8086d9' ]

asmsize = 0
Nx = list()
nlist = []
asm = []
for k, g in df.groupby(['asm'], sort=False):
    asmsize = g['len'].sum()
    name = g['asm'].unique()
    print(f'{name} asm is {asmsize}bp')
    temp = []
    nlength = 0
    for i in range(0,len(g)):
        ngx = (nlength + g.iat[i, 1]) / asmsize * 100
        temp.append(ngx)
        nlength = nlength + g.iat[i, 1]
        nlist.append(nlength)
        asm.append(asmsize)
    Nx.extend(temp)

df = df.assign(Nx = Nx)
df = df.assign(nlength = nlist)
df = df.assign(asmsize = asm)
df[0:10]
df = df.sort_values(by=['asm', 'len'], ascending=(False, False))
df[0:10]










asmsize
fig, ax = plt.subplots()
i = 0
for k, g in df.groupby(['asm']):
    #ax = g.plot(ax=ax, kind='line', x='NGX', y='len', c=colors[i], label=k)
    ax = g.plot(ax=ax, marker='', x='Nx', y='len', c=colors[i], linewidth=1, label=k)
    i += 1

ax.vlines(x=50.0, ymin=0, ymax=largestctg, linestyles='dashed')
plt.title("Nx")
plt.xlabel("x")
plt.ylabel("Scaffold Length (bp)")
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('C:/Users/tyson.fuller/OneDrive - USDA/Desktop/Nx_Line.pdf', bbox_inches='tight')
plt.close()
