from Module import*
from random import*
ang = []
rus = []
failist_lugemine("ang.txt",ang)
failist_lugemine("rus.txt",rus)
vastus = True
while vastus:
    print("""
    1. Kõik sõnad
    2. Tõlkida
    3. Uus sõna
    4. Viga parandamine
    5. Test
    6. Rääkimine
    7. Välja minna""")
    vastus = input(" >>> ")
    if vastus == "1":
        for i in range(len(ang)):
            print(rus[i]+"-"+ang[i])
        continue
    elif vastus == "2":
        slovo = input("Kirjuta sõna mis tahad tõlkida >>> ")
        if slovo not in ang and slovo not in rus:
            print(f"Sõna {slovo} veel pole meie sõnastikus aga te võite teda lisada")
            continue
        else:
            if slovo in ang:
                indeks = ang.index(slovo)
                print(f"{slovo} - {rus[indeks]}")
            elif slovo in rus:
                indeks = rus.index(slovo)
                print(f"{slovo} - {ang[indeks]}")                
    elif vastus == "3":
        slovo = input("Kirjutage sõna mis tahade lisada inglise keele sõnastiku >>> ")
        if slovo in ang:
            print("Selline sõna on juba olemas")
        else:
            new_word("ang.txt",slovo,ang)
        slovo = input("Kirjutage sõna mis tahade lisada vene keele sõnastiku >>> ")
        if slovo in rus:
            print("Selline sõna on juba olemas")
        else:
            new_word("rus.txt",slovo,rus)
    elif vastus == "4":
        vastus = input("Millises sõnastikus on viga ang/rus? >>> ")
        if vastus == "ang":
            slovo = input("Kirjutage sõna veoga inglise keele sõnastikust >>> ")
            correction(slovo,ang)
        elif vastus == "rus":
            slovo = input("Kirjutage sõna veoga vene keele sõnastikust >>> ")
            correction(slovo,rus)
        else:
            print("Vale andmetüüp!")
    elif vastus == "5":
        print("""
        Praegu hakkavad ilmuma sõnad, ning te peate kirjutama nende õiget tõlkimist""")
        result = 0
        for i in range(len(rus)):
            number = randint(1,2)
            if number == 1:
                result = test(result,rus,ang)
            else:
                result = test(result,ang,rus)
        hind = result * 100 / len(rus)
        print(f"Sul on {result}/{len(rus)} punkti ")
        if hind >= 90:
            print("Tubli, saad 5!")
        elif hind >= 75 and hind <= 90:
            print("Tubli, saad 4!")
        elif hind >= 50 and hind <= 75:
            print("Tubli, saad 3!")
        else:
            print("Pole viga, saad 2!")
    elif vastus == "6":
        print()
        #text=input("->")
        #keel=input("->")
        #heli(text,keel)
    elif vastus == "7":
        break
    else:
        print("Vale andmetüüp!")