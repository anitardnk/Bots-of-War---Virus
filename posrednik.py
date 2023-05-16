from interfejsy import InterfejsPosrednikGraczPlansza


class PosrednikGraczPlansza(InterfejsPosrednikGraczPlansza):

    def __init__(self, Plansza, gracz_id):
        self.__Plansza = Plansza
        self.__gracz_id = gracz_id

    #nie wiem czy te metody nie powinny byc statyczne
    def sprawdz_czy_ruch_legalny(self, gracz_id):
        pass

    def wymien_karte(self, indeks_karty, gracz_id):
        karta = self.__Plansza.karty_na_reku[gracz_id][indeks_karty]
        if karta in self.__Plansza.karty_na_reku[gracz_id]:
            self.__Plansza.wymien_karte(indeks_karty, gracz_id)
            self.__Plansza.daj_karty_graczowi(1, gracz_id)
            delta = {'akcja': 'wymien', 'indeks_karty': indeks_karty}
            self.__Plansza.poinformuj_graczy_o_ruchu(delta, gracz_id)
            return True
        else:
            return False
        
    def wyloz_karte(self, indeks_karty, gracz_id):
        karta = self.__Plansza.karty_na_reku[gracz_id][indeks_karty]
        if self.__Plansza.sprawdz_czy_ruch_legalny(karta, gracz_id):
            #poprawnosc ruchu
            self.__Plansza.poloz_karte(indeks_karty, gracz_id)
            self.__Plansza.daj_karty_graczowi(1, gracz_id)
            #delta = {'akcja' : akcja, 'indeks_karty': indeks_karty}
            #delta = "wyloz "+str(indeks_karty)
            delta = {'akcja': 'wyloz', 'indeks_karty': indeks_karty}
            self.__Plansza.poinformuj_graczy_o_ruchu(delta, gracz_id)
            
            return True
        else:
            return False