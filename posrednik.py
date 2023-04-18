from interfejsy import InterfejsPosrednikGraczPlansza


class PosrednikGraczPlansza(InterfejsPosrednikGraczPlansza):

    def __init__(self, Plansza):
        self.Plansza = Plansza

    #nie wiem czy te metody nie powinny byc statyczne
    def sprawdz_czy_ruch_legalny(self, gracz_id):
        pass

    def wymien_karte(self, indeks_karty, gracz_id):
        karta = self.Plansza.karty_na_reku[gracz_id][indeks_karty]
        if karta in self.Plansza.karty_na_reku[gracz_id]:
            self.Plansza.karty_na_reku[gracz_id].remove(karta)
            self.Plansza.daj_karty_graczowi(1, gracz_id)
            return True
        else:
            return False
        
    def wyloz_karte(self, indeks_karty, gracz_id):
        karta = self.Plansza.karty_na_reku[gracz_id][indeks_karty]
        if karta in self.Plansza.karty_na_reku[gracz_id]:
            self.Plansza.poloz_karte(indeks_karty, gracz_id)
            self.Plansza.daj_karty_graczowi(1, gracz_id)
            return True
        else:
            return False