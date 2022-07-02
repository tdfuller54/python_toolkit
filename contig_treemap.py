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
from cycler import cycler
import plotly.express as px
import kaleido

data = defaultdict(list)


with open('C:/Users/tyson.fuller/OneDrive - USDA/Desktop/Vvillosa.fa.fai', "r") as input:
    for l in input:
        s = l.rstrip().split()
        data['ctg'].append(s[0])
        data['len'].append(int(s[1]))
        
print(data)

df = pd.DataFrame(data)
df.head(10)
df = df.sort_values(by='len', ascending=False)
df.tail()
largestctg = df['len'].max()
largestctg
smallestctg = df['len'].min()
smallestctg
SN50 = 174244450
df.reset_index(inplace=True, drop=True)

#Get labels to add to datframe for plot
labels=[]

for i in range(0, len(df)):
    i += 1
    label= f'Linkage_{i}'
    labels.append(label)

len(labels)
labels[0:10]
df = df.assign(labels = labels)




asmsize = sum(df.len)
asmsize
chlen = sum(df.len[:7])
chlen

(chlen/asmsize)*100

NGX = list()
temp = []
nlength = 0
nlist = []
for i in range(0,len(df)):
    ngx = (nlength + df.iat[i, 1]) / asmsize * 100
    temp.append(ngx)
    nlength = nlength + df.iat[i, 1]
    nlist.append(nlength)
NGX.extend(temp)

df = df.assign(NGX = NGX)
df = df.assign(nlength = nlist)
df
asmsize
LNGX = df['NGX'].max()
SNGX = df['NGX'].min()

###Getting percentage of assembly length from smaller contigs
test = list(df.len[:7])
test2 = list(df.len[:9])
test2
((asmsize-sum(test))/asmsize) * 100
((asmsize-sum(test2))/asmsize) * 100

#Get color scheme for treemap
#norm = matplotlib.colors.Normalize(vmin=smallestctg, vmax=largestctg)
#colors = [matplotlib.cm.Blues(norm(value)) for value in df.len]
#len(colors)

##Generate list of colors that can be put into squarify. Squarify will
##recycle through these as necessary
colormap=matplotlib.cm.get_cmap('Blues', 5)
colorlist = []
for i in range(colormap.N):
    rgba = colormap(i)
    # rgb2hex accepts rgb or rgba
    colorlist.append(matplotlib.colors.rgb2hex(rgba))
colorlist
del colorlist[0]
#Changed RC params but squarify didn't use these
#matplotlib.rcParams['axes.prop_cycle'] = cycler(color=colorlist)
#matplotlib.rcParams['axes.prop_cycle']
#Generate plot

squarify.plot(sizes=df.len, label=df['labels'][:7], 
               alpha=0.8, color=colorlist, text_kwargs={'fontsize':7})
plt.title("Assembly Scaffold TreeMap",fontsize=11,fontweight="bold")

plt.axis('off')
plt.tight_layout()
plt.savefig('C:/Users/tyson.fuller/OneDrive - USDA/Desktop/TreeMap_labeled.pdf', bbox_inches='tight')
plt.close()





