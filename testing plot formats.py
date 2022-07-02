# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 20:28:09 2022

@author: tyson.fuller
"""
from collections import deque
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['savefig.facecolor'] = "0.8"


def example_plot(ax, fontsize=12):
    ax.plot([1, 2])

    ax.locator_params(nbins=3)
    ax.set_xlabel('x-label', fontsize=fontsize)
    ax.set_ylabel('y-label', fontsize=fontsize)
    ax.set_title('Title', fontsize=fontsize)

plt.close()
fig, ax = plt.subplots()
example_plot(ax, fontsize=24)
plt.tight_layout(pad=5)
plt.savefig('image5.png', bbox_inches='tight')

coolers = = deque([f'chr{x}' for x in [1,17,9,22,11,7,16,8,15,2,14,10,5,13,4,12,3,18,21,19,6,20,21,23]])

llist = [243, 17]
cutoff = int(len(llist) * 0.5)
print(cutoff)
print(llist[cutoff])
