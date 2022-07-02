# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 15:45:15 2022

@author: tyson.fuller
"""

file = "C:/Users/tyson.fuller/OneDrive - USDA/Desktop/gaps.bed"

#calculate number of gaps in full assembly
count = 0
with open("C:/Users/tyson.fuller/OneDrive - USDA/Desktop/gaps.bed", "r") as f:
    for line in f:
        count+=1
print("Line count is: ", count)

#This gives the returns of gaps per assembly
asmlen = 0
nlen = 0
with open("C:/Users/tyson.fuller/OneDrive - USDA/Desktop/gaps.stats", "r") as stats:
    next(stats)
    for l in stats:
        s = l.rstrip().split()
        print(s)
        asmlen += int(s[1])
        nlen += int(s[2])
        print(asmlen)
        print(nlen)
        
print("asm length is: ", asmlen)
print("n length is: ", nlen)
gapper = (nlen/asmlen)*100
print(gapper)
rounded = "{:0.4f}".format(gapper)
print(rounded)
with open("C:/Users/tyson.fuller/OneDrive - USDA/Desktop/gapstats.tab", "w") as out:
    out.write("NumGaps\tpercentChrLenN\n")
    out.write(f'{count}\t{gapper}\n')

test = float('1.437864')
round = "{:0.4f}".format(test)
print(round)
print(test)
