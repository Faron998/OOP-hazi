from abc import ABC
from datetime import datetime

class Szoba(ABC):
    
    def __init__(self, ar, szobaszam):
        self._ar = ar
        self._szobaszam = szobaszam
    
    def __str__(self):
        return f"Szobaszam: {self._szobaszam} Ar: {self._ar} Ft"
    
    @property
    def ar(self):
        return self._ar
    @ar.setter
    def ar(self, ertek):
        if(ertek < 0):
            print("Az ar nem lehet negativ!")
        else:
            self._ar = ertek
    @property
    def szobaszam(self):
        return self._szobaszam
    @szobaszam.setter
    def szobaszam(self, ertek):
        if(ertek < 0):
            print("A szobaszam nem lehet negativ!")
        else:
            self._ar = ertek

class EgyagyasSzoba(Szoba):
    alap = 10000
    def __init__(self, ar, szobaszam, dekoralt):
        self._dekoralt = dekoralt
        super().__init__(ar + self.alap, szobaszam)
    
    def invert_dekoralt(self):
        self._dekoralt = not self._dekoralt
    
    @property
    def dekoralt(self):
        return self._dekoralt
    @dekoralt.setter
    def dekoralt(self, ertek):
        self._dekoralt = ertek

class KetagyasSzoba(Szoba):
    alap = 15000
    tajolasok = ["north", "south", "east", "west"]
    
    def __init__(self, ar, szobaszam, tajolas):
        self._tajolas = tajolas
        super().__init__(ar + self.alap, szobaszam)
    
    @property
    def tajolas(self):
        return self._tajolas
    @tajolas.setter
    def tajolas(self, ertek):
        if(ertek in self.tajolasok):
            self._tajolas = ertek
        else:
            print("Ervenytelen tajolas!")

class Szalloda():
    def __init__(self, nev, csillagok):
        self._nev = nev
        self._csillagok = csillagok
        self._szobak = []
    
    def uj_szoba(self, szoba):
        self._szobak.append(szoba)
    
    @property
    def nev(self):
        return self._nev
    @nev.setter
    def nev(self, ertek):
        self._nev = ertek
    @property
    def csillagok(self):
        return self._csillagok
    @csillagok.setter
    def csillagok(self, ertek):
        if(ertek in range(1,6)):
            self._csillagok = ertek
        else:
            print("Ervenytelen ertek!")  
    @property
    def szobak(self):
        return self._szobak
    @szobak.setter
    def szobak(self, ertek):
        self._szobak = ertek

class Szallodak(ABC):
    szall = []
    
    # def listazas()

class Foglalas():
    def __init__(self, datum, szalloda_neve, szobaszam):
        self._datum = datum
        self._szalloda_neve = szalloda_neve
        self._szobaszam = szobaszam
    
    def __str__(self):
        return f"{self._datum}, {self._szalloda_neve}, {self._szobaszam}"
    
    def kiir_datum(self):
        return f"{self._datum['y']}. {self._datum['m']}. {self._datum['d']}."
    
    @property
    def datum(self):
        return self._datum
    @datum.setter
    def datum(self, ertek):
        self._datum = ertek
    @property
    def szalloda_neve(self):
        return self._szalloda_neve
    @szalloda_neve.setter
    def szalloda_neve(self, ertek):
        self._szalloda_neve = ertek
    @property
    def szobaszam(self):
        return self._szobaszam
    @szobaszam.setter
    def szobaszam(self, ertek):
        self._szobaszam = ertek

class Foglalasok(ABC):
    fog = []
    
    def egyezo_datum(dict, lis):
        if(dict['y'] == lis[0] and
           dict['m'] == lis[1] and
           dict['d'] == lis[2]):
            return True
        return False
    def uj_foglalas():
        # All rooms
        szall = []
        szoba = []
        for sz in Szallodak.szall:
            szall.append(sz.nev)
            g = []
            for szo in sz.szobak:
                g.append(szo.szobaszam)
            szoba.append(g)
        
        current = datetime.now()
        # Input
        be = input("Adj meg egy datumot! (Csak szamok spacekkel elvalasztva.) ")
        lines = be.split(' ')
        num_lines = []
        for l in lines:
            num_lines.append(int(l))
        # Exception
        now = current.year * 10000 + current.month * 100 + current.day
        test = num_lines[0] * 10000 + num_lines[1] * 100 + num_lines[2]
        if(now >= test):
            print("Nem jovobeli datum!")
            raise Exception
        # Kill Bad Rooms
        for i in range(len(Foglalasok.fog)):
            if(Foglalasok.egyezo_datum(Foglalasok.fog[i].datum, num_lines)):
                for j in range(len(szall)):
                    if(Foglalasok.fog[i].szalloda_neve == szall[j]):
                        szoba[j].remove(Foglalasok.fog[i].szobaszam)
        
        # List avalaible
        print("\n==============\nElerhetoek:\n=============\n")
        for i in range(len(szall)):
            print(i, ".|\t", szall[i], ": ", sep='', end='')
            for j in szoba[i]:
                print("  ", j, sep='', end='')
        be = int(input("\n-----------\nValassz szallast! (csak index)\n"))
        for i in range(len(szoba[be])):
            print(i, ".|\t", szoba[be][i], sep='')
        be2 = int(input("\n-----------\nValassz szobat! (csak index)\n"))
        
        Foglalasok.fog.append(Foglalas({'y': num_lines[0], 'm': num_lines[1], 'd': num_lines[2]}, szall[be], szoba[be][be2]))
        print("Uj foglalas sikeresen hozzaadva!\n\n")
        
        
    def listazas():
        print("==============")
        for i in range(len(Foglalasok.fog)):
            print(i, ".|\t",Foglalasok.fog[i].kiir_datum(), ':  ', Foglalasok.fog[i].szalloda_neve, "  - ", Foglalasok.fog[i].szobaszam, sep='')
    def listazas_ls(ls):
        for i in ls:
            print(i, ".|\t",Foglalasok.fog[i].kiir_datum(), ':  ', Foglalasok.fog[i].szalloda_neve, "  - ", Foglalasok.fog[i].szobaszam, sep='')
    def lemond():
        Foglalasok.listazas()
        be = int(input("\nHanyas indexu foglalast szeretned lemondani? "))
        try:
            del Foglalasok.fog[be]
        except IndexError:
            print("Nem letezo foglalas!")

def hipi_szupi_menu():
    muveletek = ["foglalas", "lemondas", "listazas", "kilepes"]
    while True:
        print("Mit szeretnel tenni? (Indexet irj)")
        for i in range(len(muveletek)):
            print(i, ".|\t", muveletek[i], sep = '')
        
        be = int(input("\n"))
        if(be == 0): Foglalasok.uj_foglalas()
        elif(be == 1): Foglalasok.lemond()
        elif(be == 2): Foglalasok.listazas()
        elif(be == 3): break
        else: print("Ervenytelen muvelet")

Szallodak.szall.append(Szalloda("Bukkos Szallas", 3))
Szallodak.szall[0].uj_szoba(EgyagyasSzoba(5000, 12, False))
Szallodak.szall[0].uj_szoba(KetagyasSzoba(5000, 13, "South"))
Szallodak.szall[0].uj_szoba(EgyagyasSzoba(9000, 15, True))

Foglalasok.fog.append(Foglalas({'y': 2024, 'm': 7, 'd': 18}, "Bukkos Szallas", 12))
Foglalasok.fog.append(Foglalas({'y': 2024, 'm': 7, 'd': 19}, "Bukkos Szallas", 12))
Foglalasok.fog.append(Foglalas({'y': 2024, 'm': 7, 'd': 20}, "Bukkos Szallas", 12))
Foglalasok.fog.append(Foglalas({'y': 2024, 'm': 6, 'd': 1}, "Bukkos Szallas", 13))
Foglalasok.fog.append(Foglalas({'y': 2024, 'm': 6, 'd': 28}, "Bukkos Szallas", 15))

hipi_szupi_menu()