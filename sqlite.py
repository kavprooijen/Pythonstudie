import sqlite3
from collections import namedtuple


class Persoon():
    def __init__(self, achternaam, leeftijd, voornamen):
        self.achternaam = achternaam
        self.leeftijd = leeftijd
        self.voornamen = voornamen
       
        
        
persoon1 = Persoon('van Prooijen - Zegveld', 36, 'Karin Anne')
print(persoon1.achternaam, persoon1.leeftijd, persoon1.voornamen)


def persoontabel(achternaam, leeftijd, voornamen):
    achternaam = str(achternaam)
    leeftijd = int(leeftijd)
    voornamen = str(voornamen)
    conn = sqlite3.connect('persoondb.db')
    curs = conn.cursor()
    try:
        curs.execute('''DROP TABLE persoon''')
    except:
        pass
    if leeftijd in range(1,199):
        curs.execute('''CREATE TABLE persoon (achternaam TEXT, leeftijd INT, voornamen TEXT)''')
        toevoeg = 'INSERT INTO persoon (achternaam, leeftijd, voornamen) VALUES(?, ?, ?)'
        curs.execute(toevoeg, (achternaam, leeftijd, voornamen))
        conn.commit()
    else:
        print('Geen geldige leeftijd')
    try:
        curs.execute('SELECT * FROM persoon')
        rows = curs.fetchall()
        print(rows)
    except:
        print('Geen tabel aanwezig')
    curs.close()
    conn.close()

persoontabel('van Prooijen - Zegveld', 36, 'Karin Anne')

Persoon = namedtuple('Persoon', 'achternaam leeftijd voornamen')
karin = Persoon('van Prooijen-Zegveld', 36, 'Karin Anne')
print(karin)



