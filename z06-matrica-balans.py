# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 09:36:34 2022

@author: wokta
"""

import random as ra
from functools import reduce as rr

def matrica(n):
    
    mat = []
    
    for i in range(n):
        mat.append([])
        for j in range(n):
            mat[i].append(ra.randint(0, 1))
    
    return mat

def Red(mat):
    
    sumaReda = []
    
    for i in range(n):
        mm = mat[i]
        sumaReda.append(rr(lambda x,y: x+y, mm))
    
    return sumaReda
    
def Kolona(mat):
    
    sumaKolone = []
    mm = []
    
    for j in range(n):
        mm.append([])
        for i in range(n):
            mm[j].append(mat[i][j])
    
    
    for i in range(n):
        m = mm[i]
        sumaKolone.append(rr(lambda x,y: x+y, m))
    
    
    return sumaKolone


def isBalansirana(r, k):
    for i in range(n-1):
        if r[i] != r[i+1]:
            return False
        elif k[i]!=k[i+1]:
            return False
        elif r[i]!=k[i+1]:
            return False
    
    return True

n = ra.randint(3,5)

for i in range(100):
    m = matrica(n)
    r = Red(m)
    k = Kolona(m)
    if isBalansirana(r, k) == True:
        print(m)
        print(r)
        print(k)
        print("da li je balansirana?", isBalansirana(r, k))
        print("redni br: ", i)
        