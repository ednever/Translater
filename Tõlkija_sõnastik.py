from Module import*
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
    6. Välja minna""")
    vastus = input("-> ")
    if vastus == "1":
        print(ang)
        print(rus)
        continue
    elif vastus == "2":
        slovo = input("Kirjuta sõna mis tahad tõlkida -> ")
        if slovo not in ang and slovo not in rus:
            print(f"Sõna {slovo} veel pole meie sõnastikus aga te võite teda lisada")
            continue
        else:
            if slovo in ang:
                indeks = ang.index(slovo)
                print(f"{slovo} - {rus[indeks]}")
            elif slovo in rus:
                indeks = rus.index(slovo)
                print(f"{slovo} - {est[indeks]}")
                
    elif vastus == "3":
        print()
    elif vastus == "4":
        print()
    elif vastus == "5":
        print()
    elif vastus == "6":
        break
    else:
        print("Vale andmetüüp!")
#slovoAng = ang[0]
#slovoRus = rus[0]
#if slovoAng in ang and slovoRus in rus:
#    if ang.index(slovoAng) == rus.index(slovoRus):
#        print("Nice")

