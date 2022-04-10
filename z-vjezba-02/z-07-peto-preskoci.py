"""
Zadatak 7

Napisati program koji od korisnika zahtijeva da sa tastature unese ime
datoteke. Takođe, sadržaj datoteke se unosi sa tastature - primjer sa vježbi.
Napisati program koji čita sadržaj fajla red po red i ispisuje ga na ekranu.
Svako peto slovo u redu ne treba da bude ispisano.

ime = input("unesi ime...")
ime += ".txt"

with open(ime, "w") as f:
    print("unesite nesto u datoteku...")
    while True:
        unos = input("nesto: ")
        if not unos:
            break
        f.writelines(unos+'\n')


"""


ime = "nesto.txt"

with open(ime, "r") as f:
    lines = f.readlines()
    mylist = []
    
    for line in lines:
        mylist.append(line.strip().split('\t'))
    
   # for i in mylist:
        #TODO finish this poop
    
    print(mylist)
