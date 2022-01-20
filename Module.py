import os
from gtts import gTTS
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

def failisse_salvestamine(f:str,l:list):
    """Loetele salvestame failisse
    :param str f: fail kuhu salvestame
    :param list l: loend kuhu lisatakse infot
    """
    fail = open(f,"w")
    for el in l:
        fail.write(el + "\n")
    fail.close()

def rida_salvestamine(f:str,rida:str):
    """Üks sõna või lause(rida) salvestamine failisse
    :param str f: fail kuhu salvestame
    :param str rida: sõna, mis vajab salvestada failisse
    """
    fail = open(f,"a")
    fail.write(rida + "\n")
    fail.close()

def new_word(f:str,rida:str,l:list)->list:
    """
    :param str f: Faili nimetus
    :param str rida: Lisatav sõna
    :param list l: sõnade loetelu
    :rtype: list
    """
    l = []
    with open(f,"a",encoding="utf-8-sig") as fail:
        fail.write(rida + "\n")
    l = failist_lugemine(f)
    return l

def translate(slovo:str)->str:
    """
    :param str slovo:
    :rtype:
    """

def heli(text:str,keel:str):
    obj = gTTS(text = text,lang = keel, slow = False).save("heli.mp3")
    os.system("heli.mp3")

def correction(sona:str,l:list):
    """
    :param str text: sõna mis tahad rääkida
    :param str keel: millises keeles tahad rääkida
    """
    for i in range(len(l)):
        if l[i] = sona:
            uus_sona = sona.replace(sona,input("Uus sõna -> "))
            l.insert(i,uus_sona)
            l.remove(sona)