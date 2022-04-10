# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 17:07:19 2022

@author: angie

Zadatak 7

Napisati funckiju koja kao argument uzima string koji se sastoji od jednocifrenih brojeva i znakova + i *. 
Izmedju svagog znaka se nalazi jednocifren broj. Funkcija treba da izracuna vrijednost unesenog stringa.
Npr. "4+2*2+7*1+3*2*2+8+1" -> 36
"""

st = "4+2*2+7*1+3*2*2+8+1" 
stoo = []
for i in range(len(st)):
    stoo.append(st[i])

rez = 0

p2 = st.split("*")
p = st.split("+")

print(st)
print(p)

pr = 1
sm = 0
nova = []
s = 0 

for i in p:
    br = 0
    for j in i:
        if j in "*" and br < 1:
            nova.append(i)
            br+=1
            
print(nova)

for i in nova:
    pr = 1
    for j in i:
        if j == "*":
            pass
        else:
            pr*=int(j)
    sm += pr
    
for i in p:
        if len(i) == 1:
            s+= int(i)
            
    
print(sm+s)

