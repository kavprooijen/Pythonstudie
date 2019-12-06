# H6_inzend_04.py
"""Klassen-hiërarchie 'onderste tak' van (wieler)wedstrijd"""             
import datetime

class Wedstrijd(object):
    # Hier uw  uitwerking van (04a, b, c, d)
    def __init__(self, plaats, datum, vertrekpunt, vertrektijd, deelnemers = None):
        self.plaats = plaats
        self.datum = datetime.datetime.strptime(datum, '%Y-%m-%d')
        self.vertrekpunt = vertrekpunt
        self.vertrektijd = datetime.datetime.strptime(vertrektijd, '%H:%M')
        self.deelnemers = deelnemers

        if self.deelnemers is None:
            self.deelnemers = []
        

    def inschrijving(self, deelnemers):
        self.deelnemers.append(deelnemers)

    def uitslag(self, goud, zilver, brons):
        self.goud = goud
        self.zilver = zilver
        self.brons = brons

        
        #goud check
        if self.goud not in self.deelnemers:
           print('Niet in deelnemerlijst: {naam}'.format(naam = str(self.goud)))
           self.goud = ""
          
        elif self.zilver not in self.deelnemers:
           print('Niet in deelnemerlijst: {naam}'.format(naam = str(self.zilver)))
           self.zilver = ""
        elif self.brons not in self.deelnemers:
           print('Niet in deelnemerlijst: {naam}'.format(naam = str(self.brons)))
           self.brons = ""
        else:
            self.winnaars = (self.goud, self.zilver, self.brons)
            print(self.winnaars)
        

    def toon(self):
        for attr, value in self.__dict__.items():
            print(attr, value)
        
        
        
            
        

# ...
# Andere klassen (Weg, ..., Baan, ...) bewust weggelaten
# ...

class Cross(Wedstrijd):
    # of: CrossWedstrijd(Wedstrijd)
    pass

class Veldrijden(Cross):
    pass

class ATB(Cross):
    # All-Terrain Bike  / MTB (Mountain bike) 
     pass	


if __name__ == '__main__':
    wedstrijd1 = ATB('eindhoven', '2019-10-12', 'kerk', '11:00')
    wedstrijd1.inschrijving('Jan Janssen')
    wedstrijd1.inschrijving('Karel Karels')
    wedstrijd1.inschrijving('Henk Henkies')
    wedstrijd1.uitslag('Jan Janssen', 'Michel', 'Henk Henkies')
    wedstrijd1.toon()

   
    



