def failist_lugemine(f:str,l:list)->list:
    """Info failist f listisse l
    :param str f: fail infoga
    :param list l: loend kuhu lisatakse infot
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
    : str rida: sõna, mis vajab salvestada failisse
    """
    fail = open(f,"a")
    fail.write(rida + "\n")
    fail.close()

def uus_sona(f:str,rida:str)->list:
    """
    ::
    ::
    """
    l = []
    with open(f,"a",encoding="utf-8-sig") as fail:
        fail.write(rida + "\n")
    l = failist_lugemine(f)
    return l

def translate