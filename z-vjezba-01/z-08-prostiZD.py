# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 18:20:35 2022

@author: angie

Zadatak 8
Napisati program koji od korisnika zahtijeva unos dva prirodna broja, a kao rezultat ispisuje
proizvod svih prostih zajednickih djelilaca unesenih brojeva.
 
"""
from functools import reduce

p = int(input("unesi prvi broj..."))
d = int(input("unesi drugi broj..."))

def prost(br):
    for i in range(2, br):
        if br % i == 0:
            return False
    return True 

def pzd(p, d):
    lista = []
    maxi = p
    if d < p:
        maxi = d
    for i in range(2, maxi+1):
        if prost(i) == True and p % i == 0 and d % i == 0:
            lista.append(i)
    
    return reduce(lambda x,y:x*y, lista)

print(pzd(p,d))