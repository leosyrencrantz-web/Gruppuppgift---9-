import random





print("Nu ska vi spela Sten, Sax eller Påse!")
name_of_ai = "python311"
print(f"Jag är {name_of_ai}")

spelarnamn = input("Ange ditt spelarnamn ->")
antal_omgångar = int(input("Ange antal omgångar som vi ska spela ->"))

result = {

spelarnamn : 0,
name_of_ai : 0,

}




i = 0
val = None
while i < antal_omgångar :
    print(f"Spelomgång {i}")
    val = input("Välj Sten Sax eller Påse ->")
    if val.lower() == "sten" :
        print("magistern spelar: Sten")

    elif val.lower() == "sax" :
        print("magistern spelar: Sax")
    elif val.lower() == "påse" :
        print("magistern spelar: Påse")

    else :
        print("what the sigma")
    
    ai_list = ["Sten","Sax","Påse"]
    ai_val = ai_list[random.randint(0,2)]
    
    print(f"{name_of_ai} spelar: {ai_val}")
    
    if val.lower() == ai_val.lower() :
        print("Womp Womp ni gissade på samma ")
    elif val.lower() == "sten" and ai_val.lower() == "påse" :
        print(f"vinnare i spelomgång {i}: {name_of_ai}")
    elif val.lower() == "sten" and ai_val.lower() == "sax" :
        print(f"vinnare i spelomgång {i}: {spelarnamn}")

 
    elif val.lower() == "påse" and ai_val.lower() == "sax" :
        print(f"vinnare i spelomgång {i}: {name_of_ai}")
    elif val.lower() == "påse" and ai_val.lower() == "sten" :
        print(f"vinnare i spelomgång {i}: {spelarnamn}")

    
    
    elif val.lower() == "sax" and ai_val.lower() == "sten" :
        print(f"vinnare i spelomgång {i}: {name_of_ai}")
    elif val.lower() == "sax" and ai_val.lower() == "påse" :
        print(f"vinnare i spelomgång {i}: {spelarnamn}")



    print(result)
    i = i + 1

    
    



