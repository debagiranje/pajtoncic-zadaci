# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 10:35:20 2022

@author: angie

umjesto elem koji se ponavljuju vise od jednom staviti nule


"""

mat = [[1,2,6], [7,1,6], [5,1,2]]

def broj_poj(l,e): #Broj pojavljivanja broja e u listi l
    br = 0
    for i in l:
        if i==e:
            br+=1
    return br

def mat_u_lisu(mat): #Matrica u listu
    lista = []
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            lista.append(mat[i][j])

    return lista

def dupli(lista): #lista duplikata
    for i in lista:
        if broj_poj(lista,i)==1:
            lista.remove(i)

def nula_umjesto_originala(mat): 
    lista = mat_u_lisu(mat)
    dupli(lista)

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] in lista:
                mat[i][j] = 0


nula_umjesto_originala(mat)
print (mat)