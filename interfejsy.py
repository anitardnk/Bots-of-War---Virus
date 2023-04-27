

class InterfejsKarty:
    def __init__(self, kolor, funkcja):
        pass


class InterfejsPosrednikGraczPlansza:
    def sprawdz_czy_ruch_legalny(self, gracz_id):
        pass
    
    def wymien_karte(self, karta):
        pass
    
    #if gracz_id None -> wykladam u siebie karte
    def wyloz_karte(self, karta, gracz_id=None): 
        pass

    def pokaz_zuzyte_karty(self):
        pass

    def pokaz_karty_gracza(self):
        pass

    def pokaz_karty_gracza_na_reku(self):
        pass

    def pokaz_karty_gracza_wylozone(self):
        pass

    def pokaz_wylozone_karty(self):
        pass
    
    #lista id wystarczy
    def pokaz_liste_graczy(self):
        pass


class InterfejsPlanszy:

    def __init__(self, talia):
        pass

    def daj_karty_graczowi(self, ilosc_kart, gracz_id):
       pass

    def poloz_karte(self, indeks_karty, gracz_id):
       pass

    def sprawdz_czy_ruch_legalny(self, gracz_id):
        pass
    
    def wymien_karte(self, karta):
        pass
    
    #if gracz_id None -> wykladam u siebie karte
    def wyloz_karte(self, karta, gracz_id_wykladajacego, gracz_id_docelowego=None): 
        pass

    def pokaz_zuzyte_karty(self, gracz_id):
        pass

    def pokaz_karty_gracza(self, gracz_id):
        pass

    def pokaz_karty_gracza_na_reku(self, gracz_id):
        pass

    def pokaz_karty_gracza_wylozone(self, gracz_id):
        pass

    def pokaz_wylozone_karty(self, gracz_id):
        pass
    
    #lista id wystarczy
    def pokaz_liste_graczy(self):
        pass

    def poinformuj_graczy_o_ruchu(self, delta, gracz_id):
        pass


class InterfejsGracz:
    def __init__(self, gracz_id, nazwa):
        pass

    def wykonaj_ruch(self, nr_kolejki):
        pass
    
    #gracz_id - kto wykonal ruch
    #delta - jedna z trzech informacji o ruchu - 1) wylozylem karte u siebie
    #2) u kogos 3) wymienilem swoja karte 4) czy ktos wygral i kto - wtedy gracz powinien
    #przygotowac sie do nowej rozgrywki
    #wywolywane po ruchu KAZDEGO gracza - nawet po swoim ruchu
    def aktualizacja_planszy_po_ruchu(self, gracz_id, delta):
        pass

    def aktualizacja_planszy_po_ruchu_wymien(self, delta, gracz_id, karta):
        pass

    def aktualizacja_planszy_po_ruchu_wyloz(self, delta, gracz_id,  karta):
        pass


class InterfejsUI:

    def __init__(self, Plansza):
        pass

    def pokaz_wylozone_karty(self):
        pass

    def pokaz_karty_na_reku(self, gracz_id):
        pass

    def pokaz_karty_wylozone_gracza(self, gracz_id):
        pass

    def pokaz_karty_gracza(self, gracz_id):
        pass



    #pobiera z planszy stan gry
    def aktualizacja_planszy_po_ruchu(self, gracz_id, delta):
        pass

    #zwraca jaki ruch, index karty, ewentualnie gracz_id drugiego gracza
    def pobierz_ruch_gracza(self, gracz_id):
        pass
