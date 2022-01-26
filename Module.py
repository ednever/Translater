from random import*
#import os
#from gtts import gTTS
def failist_lugemine(f:str,l:list)->list:
    """Info failist f listisse l
    :param str f: fail infoga
    :param list l: loend kuhu lisatakse infot
    :rtype: list
    """
    fail = open(f,"r",encoding="utf-8-sig")
    for rida in fail:
        l.append(rida.strip())
    fail.close()
    return l

def new_word(f:str,slovo:str,l:list)->list:
    """Lisatakse uut sõna failisse ja loendisse
    :param str f: Faili nimetus
    :param str slovo: Lisatav sõna
    :param list l: sõnade loetelu
    :rtype: list
    """
    with open(f,"a",encoding="utf-8-sig") as fail:
        fail.write(slovo + "\n")
    l.append(slovo)
    return l

#def heli(text:str,keel:str):
#    """
#    :param str text: sõna mis tahad rääkida
#    :param str keel: millises keeles tahad rääkida
#    obj = gTTS(text = text,lang = keel, slow = False).save("heli.mp3")
#    os.system("heli.mp3")

def correction(slovo:str,l:list):
    """Asendame vana sõna uue sõnaga
    :param str slovo: sõna mis tahad parandada
    :param list l: loend kus parandatakse
    """
    for i in range(len(l)):
        if l[i] == slovo:
            uus_slovo = slovo.replace(slovo,input("Uus sõna >>> "))
            l.insert(i,uus_slovo)
            l.remove(slovo)
            print(f"Vana sõna {slovo} on asendatud sõnaga {uus_slovo}!")


def test(result:int,l:list,l2:list)->int:
    """Juhuslikult valitakse sõna loendist, ning pärast kontrollitakse
    :param int result: Punktide arv
    :param list l: Vene keele sõnastik
    :param list l2: Inglise keele sõnastik
    :rtype: int
    """
    slovo = choice(l)
    otvet = input(f"{slovo} >>> ")
    if otvet in l2: 
        if l2.index(otvet) == l.index(slovo):
            result += 1
            print("Õige")
    else:
        print("Vale")
    return result