
from interfejsy import InterfejsUI

class ui(InterfejsUI):

    def __init__(self, Plansza):
        self.Plansza = Plansza


    def pokaz_wylozone_karty(self):

        for gracz in self.Plansza.gracze:
            for i in self.Plansza.karty_polozone[gracz.gracz_id ]:
                print('\t' + i.kolor, i.funkcja, end="\t")


    def pokaz_karty_na_reku(self, gracz_id):
        for i in self.Plansza.karty_na_reku[gracz_id]:
            print('\t'+i.kolor, i.funkcja, end="\t")

    def pokaz_karty_wylozone_gracza(self, gracz_id):

        for i in self.Plansza.karty_polozone[gracz_id]:
            print('\t' + i.kolor, i.funkcja, end="\t")

