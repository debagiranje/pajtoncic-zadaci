# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 13:14:47 2022

@author: angie

Zadatak 5

Napisati funkciju ParseInt koja kao ulazni parametar uzima jednu nisku. Nisku konvertuje u
cijeli broj ukoliko je to moguce, u suprotnom vraca None.

"""

string = "123456"
string2 = "123456sadsad"

def ParseInt(string):
    try:
        return int(string)
    except:
        print("ne moze se konvertovati u int")
    
print(ParseInt(string))
print(ParseInt(string2))
