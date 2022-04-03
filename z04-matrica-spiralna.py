# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 16:30:22 2022

@author: wokta

Zadatak 4

Sa standardnog ulaza učitava se dimenzija kvadratne matrice n,
a zatim i elementi matrice.

Izlaz: Na standardni izlaz ispisati niz elemenata matrice koji se 
dobijaju spiralnim obilaskom.

primjer

Ulaz
5
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25

Излаз
1 2 3 4 5 10 15 20 25 24 23 22 21 16 11 6 7 8 9 14 19 18 17 12 13

"""

def spiralPrint(m, n, a):
    k = 0
    l = 0
 
    ''' k - starting row index
        m - ending row index
        l - starting column index
        n - ending column index
        i - iterator '''
 
    while (k < m and l < n):
 
        # Print the first row from
        # the remaining rows
        for i in range(l, n):
            print(a[k][i], end=" ")
 
        k += 1
 
        # Print the last column from
        # the remaining columns
        for i in range(k, m):
            print(a[i][n - 1], end=" ")
 
        n -= 1
 
        # Print the last row from
        # the remaining rows
        if (k < m):
 
            for i in range(n - 1, (l - 1), -1):
                print(a[m - 1][i], end=" ")
 
            m -= 1
 
        # Print the first column from
        # the remaining columns
        if (l < n):
            for i in range(m - 1, k - 1, -1):
                print(a[i][l], end=" ")
 
            l += 1
 
 
# Driver Code
a = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
 
n = 4
 
# Function Call
spiralPrint(R, C, a)
 