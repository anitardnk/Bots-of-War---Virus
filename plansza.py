import random
from interfejsy import InterfejsPlanszy
from time import sleep


class Plansza(InterfejsPlanszy):

    def __init__(self, talia):
        self.talia = talia  # lista objektow klasy Karta
        self.karty_pozostale = self.talia[:]
        self.karty_uzyte = []

        self.karty_polozone = {}
        self.karty_na_reku = {}

    def rozdaj_karty(self, ilosc_graczy):
        for gracz_id in range(1, ilosc_graczy + 1):
            self.karty_polozone[gracz_id] = []
            self.karty_na_reku[gracz_id] = []
            self.daj_karty_graczowi(3, gracz_id)

    def daj_karty_graczowi(self, ilosc_kart, gracz_id):
        rozdane_karty = 0
        while rozdane_karty != ilosc_kart:
            karta = random.choice(self.karty_pozostale)
            self.karty_na_reku[gracz_id].append(karta)
            self.karty_pozostale.remove(karta)
            rozdane_karty += 1

    def poloz_karte(self, indeks_karty, gracz_id):
        karta = self.karty_na_reku[gracz_id][indeks_karty]
        self.karty_polozone[gracz_id].append(karta)
        self.karty_na_reku[gracz_id].remove(karta)

    def ruch_gracza(self, gracz_id):
        #UI.pokaz_karty(gracz_id)
        pass

    def rozgrywka(self, gracze):
        #plansza powinna miec liste graczy/botow
        koniec = False
        while koniec is False:
            for gracz in gracze:
                print('RUCH GRACZA: ', gracz.gracz_id)
                sleep(0.3)
                print('Karty na rece: ')
                for i in self.karty_na_reku[gracz.gracz_id]:
                    print(i.kolor, i.funkcja, end=" ")
                sleep(0.3)
                print('\nKarty wylozone: ')
                for i in  self.karty_polozone[gracz.gracz_id]:              
                    print(i.kolor, i.funkcja, end=" ")
                sleep(0.3)
                gracz.wykonaj_ruch()
                input('\nNacisnij dowolny przycisk aby kontynuowac: ')
        

