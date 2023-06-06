from interfejsy import InterfejsPosrednikGraczPlansza


class PosrednikGraczPlansza(InterfejsPosrednikGraczPlansza):

    def __init__(self, Plansza, gracz_id):
        self.__Plansza = Plansza
        self.__gracz_id = gracz_id

    #nie wiem czy te metody nie powinny byc statyczne
    def sprawdz_czy_ruch_legalny(self, gracz_id):
        pass

    def wymien_karte(self, indeks_karty):
        karta = self.__Plansza.karty_na_reku[self.__gracz_id][indeks_karty]
        if karta in self.__Plansza.karty_na_reku[self.__gracz_id]:
            self.__Plansza.wymien_karte(indeks_karty, self.__gracz_id)
            self.__Plansza.daj_karty_graczowi(1, self.__gracz_id)
            #delta = {'akcja': wyloz/wymien, 'indeks_karty': indeks wykladanej/wymienianej karty}
            delta = {'akcja': 'wymien', 'indeks_karty': indeks_karty}
            self.__Plansza.poinformuj_graczy_o_ruchu(delta)
            return True
        else:
            return False
        
    def wyloz_karte(self, indeks_karty, gracz_id_wyloz):
        karta = self.__Plansza.karty_na_reku[self.__gracz_id][indeks_karty]
        if self.__Plansza.sprawdz_czy_ruch_legalny(karta, self.__gracz_id, gracz_id_wyloz):
            #poprawnosc ruchu
            self.__Plansza.poloz_karte(indeks_karty, self.__gracz_id, gracz_id_wyloz)
            self.__Plansza.sprawdz_skutki_ruchu(karta, gracz_id_wyloz)
            self.__Plansza.daj_karty_graczowi(1, self.__gracz_id)
            #delta = {'akcja' : wyloz/wymien, 'indeks_karty': indeks wykladanej/wymienianej karty}
            #delta = {'akcja': wyloz/wyien, 'indeks_karty': indeks_karty wykladanej/wymienianej, 'gracz_id' : gracz_id osoby wykonujacej ruch,
            #  'gracz_id_wyloz': gracz_id u kogo sie wyklada karte }
            delta = {'akcja': 'wyloz', 'indeks_karty': indeks_karty, 'gracz_id' : self.__gracz_id, 'gracz_id_wyloz': gracz_id_wyloz}
            self.__Plansza.poinformuj_graczy_o_ruchu(delta)
            
            return True
        else:
            return False
    
    def karty_gracza(self):
        karty = self.__Plansza.karty_na_reku[self.__gracz_id]
        karty_opisane = [i.kolor + " " +i.funkcja for i in karty]
        return karty_opisane
        
    def karty_gracza_obiekt(self):
        karty = self.__Plansza.karty_na_reku[self.__gracz_id]
        return karty
