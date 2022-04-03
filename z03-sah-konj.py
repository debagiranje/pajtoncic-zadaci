# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 09:17:28 2022

@author: wokta

Zadatak 3

Sa tastature se unosi trenutna pozicija konja na sahovskoj ploci 
(npr. F4, A3 itd.).
Ispisati sve moguce poteze konja koji mogu da se odigraju sa trenutne pozicije.

"""
from itertools import product

slova = ["A", "B", "C", "D", "E", "F", "G", "H"]
brojevi = ["1", "2", "3", "4", "5", "6", "7", "8"]



curr = input("unesite polje na kojem se nalazi konjic...")



y0 = slova.index(curr[0])
x0 = brojevi.index(curr[1])



def knight_moves(y,x):
    moves = list(product([x-1, x+1],[y-2, y+2])) + list(product([x-2,x+2],[y-1,y+1]))
    moves = [(x,y) for x,y in moves if x >= 0 and y >= 0 and x < 8 and y < 8]
    return moves

lista = knight_moves(x0, y0)

rezultat = []
for i in lista:
    trazeni = i
    rezultat.append((slova[trazeni[0]]+brojevi[trazeni[1]]))

print("broj mogucih koraka je", len(rezultat), "a to su:")
print(rezultat)