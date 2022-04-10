# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 12:05:53 2022

@author: angie

Zadatak 1

Ucitati cetiri cijela broja, s1; s2; s3 i s4, kao i cio broj z.
Ispisati sve kombinacije sabiraka (s1, s2, s3 i s4) za koje je suma manja
od z, uz uslov da se sabirci u sumi ne ponavljaju.

"""

from functools import reduce

def kombinacija(lista, n):
     
    if n == 0:
        return [[]]
     
    l =[]
    
    for i in range(len(lista)):
         
        t = lista[i]
        ostatak = lista[i + 1:]
         
        for j in kombinacija(ostatak, n-1):
            l.append([t]+j)
             
    
    return l


if __name__ == "__main__":
    
    s1 = int(input("unesite s1..."))
    s2 = int(input("unesite s2..."))
    s3 = int(input("unesite s4..."))
    s4 = int(input("unesite s5..."))
    
    z = int(input("unesite zeljeni broj..."))
    
    arr = [s1, s2, s3, s4]
    s = []
    suma = 0

   
    for i in range(2, len(arr)+1):
            k = (kombinacija(arr, i))
            for j in k:
                suma = (reduce(lambda x,y: x+y, j))
                if suma < z:
                    s.append(j)
                    
    
    print("\nlista sabiraka: ", s)
  
   