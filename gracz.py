from posrednik import PosrednikGraczPlansza
from interfejsy import InterfejsGracz


class Gracz(InterfejsGracz):
    def __init__(self, gracz_id, nazwa, ilosc_graczy, Plansza):
        self.gracz_id = gracz_id
        self.nazwa = nazwa
        self.karty_polozone = {}
        for gracz_id in range(1, ilosc_graczy + 1):
            self.karty_polozone[gracz_id] = []
        self.karty_uzyte = []
        self.PosrednikGraczPlansza = PosrednikGraczPlansza(Plansza)

    def wymien_karte(self, gracz_id):
        karta = input("Wybierz karte do wymiany: ")
        return self.PosrednikGraczPlansza.wymien_karte(karta, gracz_id)

    def wyloz_karte(self, gracz_id):
        karta = input("Wybierz karte do wylozenia: ")
        return self.PosrednikGraczPlansza.wyloz_karte(karta, gracz_id)

    def aktualizacja_planszy_po_ruchu_wyloz(self, delta, gracz_id, karta):
        self.karty_polozone[gracz_id].append(karta)
    
    def aktualizacja_planszy_po_ruchu_wymien(self, delta, gracz_id, karta):
        self.karty_uzyte.append(karta)
