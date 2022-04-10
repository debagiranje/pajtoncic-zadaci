# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 13:21:55 2022

@author: angie
Zadatak 6

Napisati program koji zahtjeva unos brojeva sa tastature dok se ne unese 0. 
Ispisati brojeve redom i medju njima izdvojiti onaj sa najvise prostih faktora. 
Ukoliko ima vise takvih brojeva treba izdvojiti onaj sa vecom vrijednoscu.

"""

def prost(br):
    for i in range(2, br):
        if br % i == 0:
            return False
    return True

def prostiFaktori(br):
    
    brojac = 0
    
    for i in range(2, br):
        if prost(i) == True and br % i == 0:
            brojac += 1
    
    return brojac
    


br = []

while True:
    unos = int(input("unesite broj..."))
    if unos == 0:
        break
    else:
        br.append(unos)
        
najveci = prostiFaktori(br[0])

for i in br:
    if prostiFaktori(i) > najveci:
        najveci = i

for i in br:
    print(i)
    
print("naaajveci broj je... : ", najveci)   
print(prostiFaktori(36))

        