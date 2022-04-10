# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 08:15:56 2022

@author: Angie


if __name__ == "__main__":
    
    with open("ulaz.txt", "w") as f:
        
        while True:
            unos = input("unesite timove i rezultate: ")
            f.write(unos+"\n")
            if unos.strip() in "":
                break
            
    f.close()
    

"""
from functools import reduce



def pobjedica(timovi, rez):
    
    pobjede = dict()
    
    i = 0
    while i < len(timovi)-1:
        
        ime1 = timovi[i]
        ime2 = timovi[i+1]
        
        if rez[i] > rez[i+1]:
            try:
                pobjede[ime1] += 1
            except KeyError:
                pobjede[ime1] = 1
        elif rez[i] < rez[i+1]:
            try:
                pobjede[ime2] += 1
            except KeyError:
                pobjede[ime2] = 1
        
        i+=2
    
    return pobjede
    

def gubicici(timovi, rez):
    
    gubici = dict()
        
    i = 0

    while i < len(timovi)-1:
        
        ime1 = timovi[i]
        ime2 = timovi[i+1]
        
        if rez[i] < rez[i+1]:
            try:
                gubici[ime1] += 1
            except KeyError:
                gubici[ime1] = 1
        elif rez[i] > rez[i+1]:
            try:
                gubici[ime2] += 1
            except KeyError:
                gubici[ime2] = 1
        
        i+=2
        
    return gubici
    
def nerijeseno(timovi, rez):
    
    ner = dict()
    
    i = 0

    while i < len(timovi)-1:
        
        ime1 = timovi[i]
        ime2 = timovi[i+1]
        
        if rez[i] == rez[i+1]:
            try:
                ner[ime1] += 1
                ner[ime2] += 1
            except KeyError:
                ner[ime1] = 1
                ner[ime2] = 1
        
        i+=2

    return ner


    
    with open("ulaz.txt", "r") as f:
        rezultati = f.readlines()
        
    f.close()
    
    
    novi = list(map(lambda svaki: svaki.strip(), rezultati))
    novi = [i for i in novi if i]
    timovi = list(map(lambda svaki: svaki.split(" ")[0], novi))
    rez = list(map(lambda svaki: svaki.split(" ")[1], novi))
    
    timovi = list(map(lambda svaki: svaki.split(":"), timovi))
    timovi = reduce(lambda x,y:x+y,timovi)
    
    DTim = dict()
    
    for tim in timovi:
        if tim not in DTim.keys():
            DTim[tim] = 0
        
    
    rez = list(map(lambda svaki: svaki.split(":"), rez))
    rez = reduce(lambda x,y:x+y, rez)
    
    
    
    pob = pobjedica(timovi, rez)
    gub = gubicici(timovi, rez) 
    nerr = nerijeseno(timovi, rez)
    

    
    for key in DTim:
        if key not in  pob.keys():
            pob[key] = 0
        if key not in  gub.keys():
            gub[key] = 0
        if key not in  nerr.keys():
            nerr[key] = 0
 
            
    with open("izlaz.txt", "w") as f:
        for key in DTim:
            lajna = "tim: {} \n\tpobjeda: {} \n\tgubitaka: {} \n\tnerijesenih: {} \n"
            f.writelines(lajna.format(key, pob[key], gub[key], nerr[key]))
        
