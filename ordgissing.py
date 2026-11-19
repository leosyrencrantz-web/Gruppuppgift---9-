import random

# Ordlista med 10 olika ord
ordlista = [
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

spela_igen = "j"

while spela_igen == "j":
    ordet = random.choice(ordlista)
    fel_kvar = 10
    alla_gissningar = ""
    felgissingar = ""
    
    print(f"du ska gissa ett ord, bokstav för bokstav, på {len(ordet)} bokstäver")
    
    while True:
        gissing = input("ange en gissing -> ").strip()
        if len(gissing) != 1:
            print("Ogiltig gissing")
        elif not gissing.isalpha():
            print("ogiltigt tecken")
        elif gissing.upper() in alla_gissingar:
            print("denna bokstav har du redan gissat på")
        else:
            gissing = gissing.upper()
            alla_gissingar += gissing
            
            if gissing not in ordet:
                fel_kvar -= 1
                felgissningar += gissing
                
