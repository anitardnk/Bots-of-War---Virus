import random
from interfejsy import InterfejsPlanszy
from time import sleep
from UI import ui

class Plansza(InterfejsPlanszy):

    def __init__(self, talia):
        self.talia = talia  # lista objektow klasy Karta
        self.karty_pozostale = self.talia[:]
        self.karty_uzyte = []
        self.ui=ui(self)
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
    
    def wymien_karte(self, indeks_karty, gracz_id):
        #print('wymieniam karte '+ self.karty_na_reku[gracz_id][indeks_karty].kolor + self.karty_na_reku[gracz_id][indeks_karty].funkcja)
        self.karty_uzyte.append(self.karty_na_reku[gracz_id][indeks_karty])
        self.karty_na_reku[gracz_id].remove(self.karty_na_reku[gracz_id][indeks_karty])

    def ruch_gracza(self, gracz_id):
        #UI.pokaz_karty(gracz_id)
    # self.ui.pokaz_karty_gracza(gracz_id)
        pass

    def poinformuj_graczy_o_ruchu(self, delta, gracz_id):
        if delta['akcja'] == 'wymien':
            karta = self.karty_uzyte[0].kolor, self.karty_uzyte[0].funkcja
            for gracz in self.gracze:
                gracz.aktualizacja_planszy_po_ruchu_wymien(delta, gracz_id, karta)
        elif delta['akcja'] == 'wyloz':
            karta = self.karty_polozone[gracz_id][0]
            for gracz in self.gracze:
                gracz.aktualizacja_planszy_po_ruchu_wyloz(delta, gracz_id, karta)
    
    def sprawdz_czy_koniec(self):
        for gracz_id, karty_gracza in self.karty_polozone.items():
            karty_z_organem = [karta for karta in karty_gracza if karta.funkcja == "organ"]
            if len(karty_z_organem) == 4:
                print(f"\nKoniec gry! Gracz {gracz_id} ma 4 karty z organem.")
                exit()


    def rozgrywka(self):
        #plansza powinna miec liste graczy/botow
        koniec = False
        while koniec is False:

            for gracz in self.gracze:
                print('RUCH GRACZA: ', gracz.gracz_id)
                sleep(0.3)
                print('Karty na rece: ')
                self.ui.pokaz_karty_na_reku(gracz.gracz_id)
                sleep(0.3)
                print('\nKarty wylozone prez gracza ' + str(gracz.gracz_id) + ': ')
                self.ui.pokaz_karty_wylozone_gracza(gracz.gracz_id)
                sleep(0.3)
                print('\nKarty wylozone: ')
                self.ui.pokaz_wylozone_karty()
                sleep(0.3)
                gracz.wykonaj_ruch()
                self.sprawdz_czy_koniec()
                input('\nNacisnij dowolny przycisk aby kontynuowac: ')


