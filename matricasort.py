# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 09:12:19 2022

@author: angie

datu matricu transponovati te nakon toga sortirati njene elemente
potrebno ih je sortirati od najmanje do najvece na osnovu sume
elem u matrici
"""

mat = [[1,4,2],
       [9,2,1],
       [1,1,1],
       [2,3,7]]

def trans(mat):
    nova = []
    j = 0
    while j < len(mat[0]):
        nova.append([])
        for i in mat:
            nova[j].append(i[j])
        j+=1
    
    return nova

def sumica(nova):
    suma = 0
    suma_L = 0
    for i in nova:
        for j in i:
            suma += j
        suma_L.append(suma)
    return suma_L

def merge(nova):
    

n = trans(mat)
print(n)