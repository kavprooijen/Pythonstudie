def boom(teken, grootte):
    blad = ""
    for i in range(grootte):
        if len(blad) < grootte:
            blad += teken
        print(blad)

    for i in range(grootte):
        if len(blad) > 0:
            blad = blad[:-1]
        print(blad)

boom('*', 8)
