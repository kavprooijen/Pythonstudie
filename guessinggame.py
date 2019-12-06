import random
#importeren van random generator

#functie om raadspel te maken
def raden_maar(top=10):
    antwoord = random.randint(1,top)
    #randomgenerator
    while True:
    #zolang functie loopt (en dus fout antwoord geeft) vraagt ie om een nummer. zodra goed breakt ie uit de functie    

        try:
            gokgetal = int(input('Raad het getal tussen 1 en {bla} '.format(bla=top)))
        
            if (gokgetal > top or gokgetal < 1):
                print("Wel binnen 1 en ",top," raden")

            elif gokgetal < antwoord:
                print("Hoger")
                
            elif gokgetal > antwoord:
                print("Lager")
                        
            else:
                print("Goed!")
                break
        except:
            print("Geen juist getal ingevoerd")
        

raden_maar()
