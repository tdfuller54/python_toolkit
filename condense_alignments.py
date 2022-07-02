# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 20:24:39 2022

@author: tyson.fuller
"""

import pandas as pd


df = pd.read_csv(r'C:/Users/tyson.fuller/OneDrive - USDA/Desktop/LG1_alignments.txt',
                   sep='\t', header=None)
print(df)
type(df)

df[['scaffold','coords']] = df[0].str.split(":",expand=True)
df[['start','end']] = df.coords.str.split("-",expand=True)

print(df[['start','end']])
type(df['start'][0])
df['start'] = df['start'].astype(int)
df['end'] = df['end'].astype(int)
df.dtypes
df = df.drop(df.columns[0:6], 1)
df = df[df.scaffold != 'PGA_scaffold1']
df = df[df.scaffold != 'PGA_scaffold2']
df = df[df.scaffold != 'PGA_scaffold4']
df = df[df.scaffold != 'PGA_scaffold5']
df = df[df.scaffold != 'PGA_scaffold6']
df.scaffold.unique()
df.reset_index(inplace=True, drop=True)

##shift values down 1 into new column to look for matching scaffolds and
##higher or lower values


print(df)

df['group'] = df['scaffold'].ne(df['scaffold'].shift()).cumsum()
df1 = df[df.group == 1]
df2 = df[df.group == 2]
df3 = df[df.group == 3]
df4 = df[df.group == 4]
df5 = df[df.group == 5]
df6 = df[df.group == 6]
print(df1)
print(df2)
print(df3)
print(df4)
print(df5)
print(df6)
text = []
df1['st_shift'] = df1["start"].shift(1)
df1['sc_shift'] = df1["scaffold"].shift(1)
df1['end_shift'] = df1["end"].shift(1)


for index, row in df1.iloc[1:].iterrows():
    if row.st_shift < row.start:
        orient = '+'
        df1.at[index,'orient'] = orient
    else:
        orient = '-'
        df1.at[index,'orient'] = orient
df1['orient'][0] = "-"
df1['group2'] = df1['orient'].ne(df1['orient'].shift()).cumsum()



for group, df_group in df1.groupby('group2'):
    start = df_group['start'].min()
    end = df_group['end'].max()
    scaff = df_group.scaffold.unique()
    scaff2 = "".join(scaff)
    o = df_group.orient.unique()
    o2 = "".join(o)
    l = f'{scaff2}\t{start}\t{end}\t{o2}'
    text.append(l)
len(text)

print(df2)
df2['st_shift'] = df2["start"].shift(1)
df2['sc_shift'] = df2["scaffold"].shift(1)
df2['end_shift'] = df2["end"].shift(1)


for index, row in df2.iloc[1:].iterrows():
    if row.st_shift < row.start:
        orient = '+'
        df2.at[index,'orient'] = orient
    else:
        orient = '-'
        df2.at[index,'orient'] = orient
df2['orient'][959] = "+"
df2['group2'] = df2['orient'].ne(df2['orient'].shift()).cumsum()



for group, df_group in df2.groupby('group2'):
    start = df_group['start'].min()
    end = df_group['end'].max()
    scaff = df_group.scaffold.unique()
    scaff2 = "".join(scaff)
    o = df_group.orient.unique()
    o2 = "".join(o)
    l = f'{scaff2}\t{start}\t{end}\t{o2}'
    text.append(l)
len(text)


print(df3)
o = "+"
scaff = "PGA_scaffold3"
start = df3["start"].min()
end = df3["end"].max()
l = f'{scaff}\t{start}\t{end}\t{o}'
print(l)
text.append(l)
len(text)


print(df4)
len(df4)
df4['st_shift'] = df4["start"].shift(1)
df4['sc_shift'] = df4["scaffold"].shift(1)
df4['end_shift'] = df4["end"].shift(1)


for index, row in df4.iloc[1:].iterrows():
    if row.st_shift < row.start:
        orient = '+'
        df4.at[index,'orient'] = orient
    else:
        orient = '-'
        df4.at[index,'orient'] = orient
df4['orient'][1166] = "+"
df4['group2'] = df4['orient'].ne(df4['orient'].shift()).cumsum()



for group, df_group in df4.groupby('group2'):
    start = df_group['start'].min()
    end = df_group['end'].max()
    scaff = df_group.scaffold.unique()
    scaff2 = "".join(scaff)
    o = df_group.orient.unique()
    o2 = "".join(o)
    l = f'{scaff2}\t{start}\t{end}\t{o2}'
    text.append(l)
len(text)


print(df5)
o = "+"
scaff = "PGA_scaffold3"
start = df5["start"].min()
end = df5["end"].max()
l = f'{scaff}\t{start}\t{end}\t{o}'
print(l)
text.append(l)
len(text)

print(df6)
len(df6)
df6['st_shift'] = df6["start"].shift(1)
df6['sc_shift'] = df6["scaffold"].shift(1)
df6['end_shift'] = df6["end"].shift(1)


for index, row in df6.iloc[1:].iterrows():
    if row.st_shift < row.start:
        orient = '+'
        df6.at[index,'orient'] = orient
    else:
        orient = '-'
        df6.at[index,'orient'] = orient
df6['orient'][1200] = "+"
df6['group2'] = df6['orient'].ne(df6['orient'].shift()).cumsum()



for group, df_group in df6.groupby('group2'):
    start = df_group['start'].min()
    end = df_group['end'].max()
    scaff = df_group.scaffold.unique()
    scaff2 = "".join(scaff)
    o = df_group.orient.unique()
    o2 = "".join(o)
    l = f'{scaff2}\t{start}\t{end}\t{o2}'
    text.append(l)
len(text)




tab = "\n".join(text)
print(tab)

with open('C:/Users/tyson.fuller/OneDrive - USDA/Desktop/LG1_condensed.tab', "w") as text2:
    text2.write(tab)   
         