import random
print("Nu ska vi spela Sten, Sax eller Påse!")
print("Jag är pytohn 311")

spelarnamn = input("Ange ditt spelarnamn ->")
antal_omgångar = int(input("Ange antal omgångar som vi ska spela ->"))

i = 0
val = None
print("waht")
while i < antal_omgångar :
    print(f"Spelomgång {i}")
    val = input("Välj Sten Sax eller Påse ->")
    ai = random.randint(1,3)
    print(ai)

    
    



