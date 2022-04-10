# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 12:58:35 2022

@author: angie

Zadatak 3

Napisati program koji zahtijeva unos prirodnog broja sa tastature, kao rezultat ispisuje
listu nula i jedinica koji predstavljaju zapis unesenog broja u binarnom brojnom sistemu.

"""

br = int(input("unesite prirodan broj..."))

rez = []

while br != 0:
    ostatak = br % 2  
    br = br // 2
    rez.append(ostatak)

print("decimalno u binarno: ", rez)