# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 09:17:28 2022

@author: wokta

Zadatak 3

Sa tastature se unosi trenutna pozicija konja na sahovskoj ploci 
(npr. F4, A3 itd.).
Ispisati sve moguce poteze konja koji mogu da se odigraju sa trenutne pozicije.

"""


slova = ["A", "B", "C", "D", "E", "F", "G", "H"]
brojevi = ["1", "2", "3", "4", "5", "6", "7", "8"]



curr = input("unesite polje na kojem se nalazi konjic...")



y0 = slova.index(curr[0])
x0 = brojevi.index(curr[1])


def konj(y,x):
    list3 = [(i,j) for i in [x-1, x+1] for j in [y-2, y+2]]
    list4 = [(i,j) for i in [x-2, x+2] for j in [y-1, y+1]]
    moves = list3 + list4
    moves = [(x,y) for x,y in moves if x >= 0 and y >= 0 and x < 8 and y < 8]
    return moves

lista = konj(x0, y0)

nova = []
for i in lista:
    nova.append(slova[i[0]] + brojevi[i[1]])

print("broj mogucih koraka je", len(lista), "a to su:")
print(nova)