from abc import ABC, abstractmethod
from datetime import datetime


# Szoba absztrakt osztály
class Szoba(ABC):
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

    @abstractmethod
    def __str__(self):
        pass

# EgyagyasSzoba osztály
class EgyagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam):
        super().__init__(ar, szobaszam)

    def __str__(self):
        return f"Egyágyas szoba (Szám: {self.szobaszam}, Ár: {self.ar} Ft/éj)"

# KétagyasSzoba osztály
class KetagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam):
        super().__init__(ar, szobaszam)

    def __str__(self):
        return f"Kétágyas szoba (Szám: {self.szobaszam}, Ár: {self.ar} Ft/éj)"

# Szalloda osztály
class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def hozzaad_szoba(self, szoba):
        self.szobak.append(szoba)

    def listaz_szobak(self):
        for szoba in self.szobak:
            print(szoba)

# Foglalás osztály
class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

    def __str__(self):
        return f"Foglalás - Szoba: {self.szoba.szobaszam}, Dátum: {self.datum}, Ár: {self.szoba.ar} Ft"

# Rendszer a foglalások kezelésére
class FoglalasiRendszer:
    def __init__(self):
        self.szalloda = Szalloda("Teszt Szálloda")
        self.foglalasok = []

    def szoba_foglalas(self, szobaszam, datum):
        datum = datetime.strptime(datum, "%Y-%m-%d")
        if datum < datetime.now():
            print("Hiba: A foglalás dátuma a jövőben kell legyen!")
            return

        for foglalas in self.foglalasok:
            if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                print("Hiba: A szoba már foglalt erre a dátumra!")
                return

        for szoba in self.szalloda.szobak:
            if szoba.szobaszam == szobaszam:
                uj_foglalas = Foglalas(szoba, datum)
                self.foglalasok.append(uj_foglalas)
                print("Foglalás sikeres:", uj_foglalas)
                return
        print("Hiba: Nincs ilyen szobaszám a szállodában!")

    def foglalas_lemondas(self, szobaszam, datum):
        datum = datetime.strptime(datum, "%Y-%m-%d")
        for foglalas in self.foglalasok:
            if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                self.foglalasok.remove(foglalas)
                print("Foglalás lemondva:", foglalas)
                return
        print("Hiba: Nincs ilyen foglalás!")

    def listaz_foglalasok(self):
        if not self.foglalasok:
            print("Nincs foglalás.")
        else:
            for foglalas in self.foglalasok:
                print(foglalas)

# Rendszer inicializálása tesztadatokkal
rendszer = FoglalasiRendszer()
rendszer.szalloda.hozzaad_szoba(EgyagyasSzoba(10000, 101))
rendszer.szalloda.hozzaad_szoba(EgyagyasSzoba(12000, 102))
rendszer.szalloda.hozzaad_szoba(KetagyasSzoba(15000, 201))

# Teszt foglalások
rendszer.szoba_foglalas(101, "2024-06-01")
rendszer.szoba_foglalas(102, "2024-06-02")
rendszer.szoba_foglalas(201, "2024-06-03")
rendszer.szoba_foglalas(101, "2024-06-04")
rendszer.szoba_foglalas(102, "2024-06-05")

# Felhasználói interfész
while True:
    print("\nFoglalási Rendszer")
    print("1. Szoba foglalása")
    print("2. Foglalás lemondása")
    print("3. Foglalások listázása")
    print("4. Kilépés")
    valasztas = input("Válasszon egy műveletet (1-4): ")

    if valasztas == "1":
        szobaszam = int(input("Adja meg a szobaszámot: "))
        datum = input("Adja meg a dátumot (YYYY-MM-DD): ")
        rendszer.szoba_foglalas(szobaszam, datum)
    elif valasztas == "2":
        szobaszam = int(input("Adja meg a szobaszámot: "))
        datum = input("Adja meg a dátumot (YYYY-MM-DD): ")
        rendszer.foglalas_lemondas(szobaszam, datum)
    elif valasztas == "3":
        rendszer.listaz_foglalasok()
    elif valasztas == "4":
        break
    else:
        print("Érvénytelen választás, próbálja újra.")
