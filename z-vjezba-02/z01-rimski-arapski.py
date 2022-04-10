# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 18:15:47 2022

@author: wokta

Zadatak 1

Napisati program koji konvertuje rimske u arapske brojeve.

"""


def rom(num):
    rimski = {"I": 1, "II":2, "III":3, "IV":4, "V":5, "VI":6, "VII":7, "VIII":8, "IX":9, "X":10, "L":50, "C":100, "D":500, "M":1000}
    result = 0
    for i,c in enumerate(num):
        if (i+1) == len(num) or rimski[c] >= rimski[num[i+1]]:
            result += rimski[c]
        else:
            result -= rimski[c]
    return result


print(rom("MCDXVIII"))