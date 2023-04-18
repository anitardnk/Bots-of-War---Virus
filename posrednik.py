from interfejsy import InterfejsPosrednikGraczPlansza

class PosrednikGraczPlansza(InterfejsPosrednikGraczPlansza):

    #nie wiem czy te metody nie powinny byc statyczne
    def sprawdz_czy_ruch_legalny(self, gracz_id):
        pass
    @staticmethod
    def wymien_karte(karta, gracz_id):
        if karta in Plansza.karty_na_reku[gracz_id]:
            Plansza.karty_na_reku[gracz_id].remove(karta)
            Plansza.daj_karty_graczowi(1, gracz_id)
            return True
        else:
            return False
    @staticmethod
    def wyloz_karte(karta, gracz_id):
        if karta in Plansza.karty_na_reku[gracz_id]:
            Plansza.poloz_karte(karta, gracz_id)
            return True
        else:
            return False