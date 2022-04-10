# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 13:06:40 2022

@author: angie

Zadatak 4
Napisati program koji zahtijeva unos stringa koji se sastoji od malih i velikih slova,
kao rezultat vraca uneseni tekst formatiran tako da mu rijeci pocinju velikim slovom,
dok su sva ostala slova mala. Npr. "DaNaS jE uToraK" -> "Danas Je Utorak".

"""

string = "DaNaS jE uToraK"

string = string.lower()
string = string.split(" ")

novi = []
for i in string:
    novi.append(i[0].upper() + i[1:])
    
print(" ".join(novi))