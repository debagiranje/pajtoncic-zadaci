# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 18:30:35 2022

@author: angie

Zadatak 10
Sa tastature se unosi neparan prirodan broj iz intervala (3, 13). 
Naci najmanji prirodan broj koji je potrebno dodati generisanom broju da bi se dobio potpuni kub.
Npr. Ako je generisani broj 5, trazeni broj je 3 jer je 5 + 3 = 8 = 2**3

"""

import random

broj = random.randint(3, 14)

#pkub = [x**3 for x in range(2,14)]
print(broj)

if broj <= 8:
    print(8-broj)
else:
    print(27-broj)