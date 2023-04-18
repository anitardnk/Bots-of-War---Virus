from posrednik import PosrednikGraczPlansza
from interfejsy import InterfejsGracz
class Gracz(InterfejsGracz):
    def __init__(self, gracz_id, nazwa):
        self.gracz_id = gracz_id
        self.nazwa = nazwa
        self.PosrednikGraczPlansza = PosrednikGraczPlansza()

    def wymien_karte(self, gracz_id):
        karta = input("Wybierz karte do wymiany: ")
        return self.PosrednikGraczPlansza.wymien_karte(karta, gracz_id)

    def wyloz_karte(self, gracz_id):
        karta = input("Wybierz karte do wylozenia: ")
        return self.PosrednikGraczPlansza.wyloz_karte(karta, gracz_id)
