# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 13:06:53 2022

@author: wokta

Zadatak 2

Sa tastature se unosi rezultat teniskog meca u obliku stringa (u formi x:x x:x x:x). Ispravna forma je "7:6 6:3" ==> sto znaci da je igrac 1 pobijedio;
"3:6 6:4 2:6" ==> igrac 2 je pobijedio 2:1 u setovima.

Nakon ispisanog rezultata, ispisati poruku koji od igraca je pobijedio i kojim rezultatom (u setovima).
Provjeriti prije obrade unosa njegovu validnost i ispisati poruku ako unos nije validan.


"""

import re 

pattern = "[6-7]+\:+[0-6]|[0-6]+\:+[6-7]"


st = "3:6 6:3 2:6"

a = re.findall(pattern , st)

provjera = st.split(" ")

if a == provjera:
    pass
else:
    print("unos nije okej!")

prvi = []
drugi = []

for gem in a:
    prvi.append(gem.split(":")[0])
    drugi.append(gem.split(":")[1])


print(prvi)
print(drugi)

pb = 0
db = 0

for svaki in range(len(prvi)):
    if prvi[svaki] > drugi[svaki]:
        pb += 1
    else:
        db += 1
        
if pb > db:
    print("pobijedio je prvi igrac, sa {} : {} u setovima".format(pb, db))
else:
    print("pobijedio je drugi igrac, sa {} : {} u setovima".format(db, pb))