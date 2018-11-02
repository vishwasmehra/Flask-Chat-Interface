# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 17:25:09 2018

@author: Heller
"""
import os
inde="1"
inde=int(inde)
flag=0
for f in os.listdir("notes/"):
    flag=flag+1
    if(flag==inde):
        file="notes/"+f
        with open(file) as fa:
            content = fa.readlines()
content=[x.strip() for x in content] 
rep=""
for i in content:
    rep=rep+i+"<br>"
    
print(rep)