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

import random

def matrica(n):
    a = []
    for i in range(n):
        for j in range(n):
            a.append(random.randint(0, 1))
    return a


def kretko(x,y):
    lista = [[i,j] for i in [x+1, x, x-1] for j in [y-1, y, y+1]]
    nova = [[x,y] for x,y in lista if x < 0 and y < 0 and x < 3 and y < 3]
    return nova
    

n = 3
a = matrica(3)
x =  1
y = 1

kopija = [0 for i in a]


lista = [[i,j] for i in [x+1, x, x-1] for j in [y-1, y, y+1]]
nova = [[x,y] for x,y in lista if x >= 0 and y >= 0 and x < 3 and y < 3]
nova.remove([x,y])

for i in range(lista):
    for j in range(lista[0]):
        if nova[i][j]    

print(a)
print(nova)
print(kopija)