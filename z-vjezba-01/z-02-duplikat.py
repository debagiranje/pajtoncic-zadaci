# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 12:47:47 2022

@author: angie

Zadatak 2

Napisati funkciju koja brise duplikate iz liste

"""

lista = [1,2,3,3,4,3,2,4,5,3]

nova = []

for i in lista:
    if i not in nova:
        nova.append(i)
    
print(nova)