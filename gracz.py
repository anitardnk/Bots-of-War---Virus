from posrednik import PosrednikGraczPlansza
from interfejsy import InterfejsGracz


class Gracz(InterfejsGracz):
    def __init__(self, gracz_id, nazwa, ilosc_graczy, posrednik):
        self.gracz_id = gracz_id
        self.nazwa = nazwa
        self.karty_polozone = {}
        for gracz_id in range(1, ilosc_graczy + 1):
            self.karty_polozone[gracz_id] = []
        self.karty_uzyte = []
        self.ilosc_graczy = ilosc_graczy
        self.PosrednikGraczPlansza = posrednik

    def wymien_karte(self, gracz_id):
        karta = input("Wybierz karte do wymiany: ")
        return self.PosrednikGraczPlansza.wymien_karte(karta, gracz_id)

    def wyloz_karte(self, gracz_id):
        karta = input("Wybierz karte do wylozenia: ")
        return self.PosrednikGraczPlansza.wyloz_karte(karta, gracz_id, gracz_id_wyloz)

    def aktualizacja_planszy_po_ruchu_wyloz(self, delta, karta):
        self.karty_polozone[delta['gracz_id_wyloz']].append(karta)
    
    def aktualizacja_planszy_po_ruchu_wymien(self, delta, karta):
        self.karty_uzyte.append(karta)
