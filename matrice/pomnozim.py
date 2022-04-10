# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 10:47:57 2022

@author: angie
"""

def mnozi(a,b):
    
    c = [[0 for i in range(len(a))] for j in range(len(a))]
    
    
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                c[i][j] += a[i][k] * b[k][j]
    
    return  c
        
        

a = [[1,0,1,1,1],[1,1,0,0,0],[0,0,1,0,1]]
b = [[1,0,0],[1,1,0],[0,1,0],[1,1,1],[0,0,1]]


print(mnozi(a,b))