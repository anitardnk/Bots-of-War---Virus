class InterfejsKarty:
    def __init__(self, kolor, funkcja):
        pass


from posrednik import PosrednikGraczPlansza


class InterfejsPosrednikGraczPlansza:
    def sprawdz_czy_ruch_legalny(self, gracz_id):
        pass
    @staticmethod
    def wymien_karte(karta, gracz_id):
        pass
    @staticmethod
    def wyloz_karte(karta, gracz_id): 
        pass

class InterfejsPlanszy:

    def __init__(self, talia):
        pass

    def rozdaj_karty(self, ilosc_graczy):
        pass

    def daj_karty_graczowi(self, ilosc_kart, gracz_id):
       pass

    def poloz_karte(self, indeks_karty, gracz_id):
       pass

class InterfejsGracz:
    def __init__(self, gracz_id, nazwa):
        pass

    def wymien_karte(self, gracz_id):
        pass

    def wyloz_karte(self, gracz_id):
        pass

