# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 18:54:57 2022

@author: wokta

Zadatak 5

Napraviti funkciju koja za agrument uzima matricu sastavljenu
od 0 i 1.
Kao rezultat funkcija treba da vrati marticu u kojoj su
nule zamijenjene 
brojem koji govori koliko se oko nule nalazi jedinica, a jedinice
zamijenjene nulama.


popravi ovo

"""
from itertools import product
import random

def matrica(n):
    a = []
    
    for i in range(n):
        for j in range(n):
            a.append(random.randint(0, 1))
    return a

def jelKec(poz):
    if poz == 1:
        return True
    else:
        return False

def kretko(y,x):
    moves = list(product([x-1, x+1],[y-1, y+1])) 
    moves = [(x,y) for x,y in moves if x >= 0 and y >= 0 and x < n and y < n]
    return moves

n = 3
a = matrica(3)

for i in range(n):
    for j in range(n):
        if a[j] == 0:
            a[j] = kretko(i,j)
        

print(kretko(i,j))
print(a)