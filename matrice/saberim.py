# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 10:26:23 2022

@author: angie

sabira elem iznad dijagonale 

"""
mat = [[1,4,2,5],
       [9,2,1,6],
       [1,1,1,7],
       [2,3,7,8]]

def saberi_iznad(mat):
    suma = 0
    
    for i in mat:
        for j in i:
            if i < j:
                suma += j
    
    return suma 



        