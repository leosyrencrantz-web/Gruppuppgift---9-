import random

# Ordlista med 10 olika ord
ORD_LISTA = [
    "SLÄKTNING",
    "SKIDÅKNING",
    "PROGRAMMERING",
    "DATORSKÄRM",
    "CYKELSTÄLL",
    "HÖSTLOV",
    "JORDGUBBE",
    "CHOKLAD",
    "PANNKAKA",
    "SOMMARLOV"]


def spela_omgang():
    ordet = random.choice(ORD_LISTA).upper()
    gissade_bokstaver = set()
    felgissningar = []
    fel_kvar = 9

    print(f"Du ska gissa ett ord, bokstav för bokstav, på {len(ordet)} bokstäver")

    while True:
        gissning = input("Ange en gissning -> ").strip()
        
        if len(gissning) != 1:
            print("Ogiltig gissning")
            continue
        if not gissning.isalpha():
            print("Ogiltigt tecken")
            continue
            
        gissning = gissning.upper()
        
        if gissning in gissade_bokstaver:
            print("Denna bokstav har du redan gissat på")
            continue