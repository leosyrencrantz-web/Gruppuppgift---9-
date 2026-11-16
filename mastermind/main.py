print("Datorn kommer att slumpa fram en kod på fyra siffror mellan 1 och 6\n Du ska försöka gissa denna kods siffror på max 12 drag\nEfter respektive gissning så kommer du få en respons:\nFör varje korrekt gissad siffra på korrekt plats i koden:\nFör varje korrekt gissad siffra på fel plats i koden:\nför dem siffror som inte finns med i koden ges ingen markering")

print("\n\nDu får välja mellan två svårighetsnivåer:\nLättare nivå: Alla siffror är garanterat olika\nSvårare nivå: Det kan finnas en upprepning av en eller flera siffror")

while True:
    nivå = int(input("Ange önskad nivå: lättare (1), svårare (2) ->"))
    if nivå == 1 or nivå == 2 :
        break
    else :
        None


if nivå = 1 :
    print("WEAK")
elif nivå = 2 :
    print("UR GONNA REGRET THIS :3")


antal_omgångar = 12
antal_omgångar_körda = 0
while antal_omgångar_körda  < antal_omgångar :
    while True :
        gissning = input("Ange gissning som följd av fyra siffror ->")
        if len(gissning) == 4 and gissning.isdigit() :
            break
        else :
            print("kom ihåg endast 4")
            None
    
    print(gissning)

    i = 0 
    while i < 4:
        print(gissning[i])
        i = i + 1


    antal_omgångar_körda  = antal_omgångar_körda  + 1
