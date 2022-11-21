from random import randint 
import csv

#Functia principala
def main():
    numere_castigatoare=get_numere()
    print(f"Numerele castigatoare sunt: {numere_castigatoare}")
    numere_extrase=get_extrageri()
    print(f"Numerele extrase sunt: {numere_extrase}")

    #Afisam daca am nimerit vre-un numar
    numere_comune=[]
    for i in numere_castigatoare:
        if i in numere_extrase:
            numere_comune.append(i)
    print(f"Numere comune: {len(numere_comune)}")
    
    #Stocam numerele extrase intr-un fisier .csv
    with open("rezultate.csv", "w", newline="") as csvfile:
        write=csv.writer(csvfile, delimiter=",")
        write.writerow(numere_castigatoare)
        write.writerow(numere_extrase)



#Functie pentru a introduce numerele castigatoare
def get_numere():
    #numere=["11", "45", "23", "7", "36", "1"]
    numere=[] 
    print("Introduceti 6 numere. Numerele trebuie sa fie de la 1 la 49:")
    for _ in range(6):
        while True:
            try:
                numar=int(input())
                if numar in numere:
                    print("Numarul deja exista. Introduceti alt numar")
                elif numar <1 or numar >49:
                    print("Numarul trebuie sa fie intre 1 si 49!")
                else: 
                    break     
            except ValueError:
                print("Introduceti numere intregi!")
        numere.append(numar) 
    return numere
    


#Functie pentru a genera numere aleatorii
def get_extrageri():
    numere=[] 
    for _ in range(6):
        numar=randint(1,49) #generam un numar intre 1 si 15
        while numar in numere: #daca numarul este in lista
            numar=randint(1,49) #generam alt numar
        numere.append(numar) #adaugam nr in lista
    return numere #lista goala unde urmeaza asa adaugam numere



if __name__ =="__main__":
    main()
