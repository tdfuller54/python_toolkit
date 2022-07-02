# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from collections import defaultdict
asms = ("OAR4", "Rambouillet2")
ecol = 1
ccol = 1
dcol = 10
esep = '-' * (ecol - 1)
csep = '-' * (ccol - 1)
dsep = '-' * (dcol - 1)
print(csep)

#.join takes whats inside so csep (---------) + : so (---------:) creates one of those strings
#for each value of asms and prints them combining them with the | before the .join
# so this says print | + ----:|----: + | because two values in asm are being combined by the
# | and the two outer | surround it. |---------:|---------:|
csepfull = "|" + "|".join([csep + ":" for x in asms]) + "|"
print(csepfull)


#.format says value of i goes where 0 is. Then the : >{ccol} actually tells .format
#to return string "i" with a total of ccol spaces and to align the string to the right
# so if i="cat" then this returns "       cat". if it was :*>{ccol} it would
#return "*******cat" total spaces need to be length of ccol which is 10 and the
#character before ">" says what to fill in the extra with. Note that the returned
#value can also be greater so if : >{2} then it would still return "cat"
def formatVarWidth(tlist, ccol):
    rstr = ""
    for i in tlist:
        rstr += "|{0: >{ccol}}".format(i, ccol=ccol)
    return rstr + "|"


d = defaultdict(list)
d2 = defaultdict(list)
a=[('ace',100),('b',2),('c',3)]
b=[('ac','tree'),('b',2),('c',3)]
c=[('ac','purples'),('b',190000000),('c',3)]
for i, j in a:
    d[i].append(j)
    
for i, j in c:
    d2[i].append(j)


for k, v in d2.items():
    ecol = len(str(k)) if len(str(k)) > ecol else ecol
    print(k)
    print(v)
    for j in v:
        ccol = len(str(j)) if len(str(j)) > ccol else ccol
print(ecol)
print(ccol)
print(d)
print(d2)
