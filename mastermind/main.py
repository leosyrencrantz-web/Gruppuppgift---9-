print("Datorn kommer att slumpa fram en kod på fyra siffror mellan 1 och 6\n Du ska försöka gissa denna kods siffror på max 12 drag\nEfter respektive gissning så kommer du få en respons:\nFör varje korrekt gissad siffra på korrekt plats i koden:\nFör varje korrekt gissad siffra på fel plats i koden:\nför dem siffror som inte finns med i koden ges ingen markering")

print("\n\nDu får välja mellan två svårighetsnivåer:\nLättare nivå: Alla siffror är garanterat olika\nSvårare nivå: Det kan finnas en upprepning av en eller flera siffror")

while True:
    nivå = int(input("Ange önskad nivå: lättare (1), svårare (2) ->"))
    if nivå == 1 or nivå == 2 :
        break
    else :
        None

print(nivå)
