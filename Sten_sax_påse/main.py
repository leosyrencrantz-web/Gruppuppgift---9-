import random
print("Nu ska vi spela Sten, Sax eller Påse!")
print("Jag är pytohn 311")

spelarnamn = input("Ange ditt spelarnamn ->")
antal_omgångar = int(input("Ange antal omgångar som vi ska spela ->"))

i = 0
val = None
while i < antal_omgångar :
    print(f"Spelomgång {i}")
    val = input("Välj Sten Sax eller Påse ->")
    ai = random.randint(1,3)
#   1 = Sten
#   2 = Sax
#   3 = Påse
    
    if val.lower == "sten" :
        print("magistern spelar: Sten")

    elif val.lower == "sax" :
        print("magistern spelar: Sax")
    elif val.lower == "påse" :
        print("magistern spelar: Påse")

    else :
        print("what the sigma")
    
    print(ai)
    i = i + 1

    
    



