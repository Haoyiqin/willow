# -*- coding: utf-8 -*-
"""
Created on Sun May 13 23:47:37 2018

@author: Administrator
"""

import keyword
s=keyword.kwlist
n=input("输入一个文件名:")
f=open(n,"r").readlines()
ls=[]
for i in f:
    i=i.split()
    ls.append(i)
fo=open(n,"w+")
for i in range(len(ls)):
    if f[i].isspace():
       fo.write(" "+"\n")
    for j in range(len(ls[i])):
        x= ls[i][j]
        if x not in s:
            x=x.upper()
        else:
            x=x.lower()
        if x==ls[i][len(ls[i])-1]:
            fo.write(x+"\n")
        else:
            fo.write(x+" ")
