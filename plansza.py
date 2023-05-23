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

    def sprawdz_czy_ruch_legalny(self, karta, gracz_id):
        if karta in self.karty_na_reku[gracz_id]:
            wylozone_karty_gracza = self.karty_polozone[gracz_id]
            if karta.funkcja == 'lek':
                for i in wylozone_karty_gracza:
                    if i.funkcja == 'organ' and i.kolor == karta.kolor:
                        if wylozone_karty_gracza.count(karta) < 2:
                            return True
            elif karta.funkcja == 'organ':
                for i in wylozone_karty_gracza:
                    if i.funkcja == 'organ' and i.kolor == karta.kolor:
                        return False
                return True
            elif karta.funkcja == 'wirus':
                for i in wylozone_karty_gracza:
                    if (i.funkcja == 'organ' or i.funkcja == 'szczepionka' or i.funkcja == 'wirus') and i.kolor == karta.kolor:
                        return True
                return False
        return False

    def sprawdz_skutki_ruchu(self, karta, gracz_id):
        wylozone_karty_gracza = self.karty_polozone[gracz_id]
        leki = []
        wirusy = []
        organ = 0
        for i in wylozone_karty_gracza:
            if i.kolor == karta.kolor:
                if i.funkcja == 'wirus':
                    wirusy.append(i)
                elif i.funkcja == 'lek':
                    leki.append(i)
                else:
                    organ = i
        # 2 wirusy - usun organ i 2 wirusy
        # 1 wirus 1 lek - usun oba
        # 2 leki 1 wirus - niemozliwe, sprawdzane podczas walidacji ruchu
        if len(wirusy) == 2:
            karty_do_usuniecia = wirusy + [organ]
            self.karty_polozone[gracz_id] = [i for i in self.karty_polozone[gracz_id] if i not in karty_do_usuniecia]
            self.karty_uzyte.append(karty_do_usuniecia)
        elif len(wirusy) == 1 and len(leki) == 1:
            karty_do_usuniecia = leki + wirusy
            self.karty_polozone[gracz_id] = [i for i in self.karty_polozone[gracz_id] if i not in karty_do_usuniecia]
            self.karty_uzyte.append(karty_do_usuniecia)

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
        #delta = {'akcja': wyloz/wymien, 'indeks_karty': indeks wykladanej/wymienianej karty}
        if delta['akcja'] == 'wymien':
            karta = self.karty_uzyte[0].kolor, self.karty_uzyte[0].funkcja
            for gracz in self.gracze:
                gracz.aktualizacja_planszy_po_ruchu_wymien(delta, gracz_id, karta)
        elif delta['akcja'] == 'wyloz':
            karta = self.karty_polozone[gracz_id][0]
            for gracz in self.gracze:
                gracz.aktualizacja_planszy_po_ruchu_wyloz(delta, gracz_id, karta)
    
    def sprawdz_czy_koniec(self):
        #4 ograny bez zadnego wirusa - stan na 23.05 4 kolory organow - nie moze byc zadnego wirusa
        for gracz_id, karty_gracza in self.karty_polozone.items():
            karty_z_organem = [karta for karta in karty_gracza if karta.funkcja == "organ"]
            if len(karty_z_organem) == 4:
                wirusy = [karta for karta in karty_gracza if karta.funkcja == "wirus"]
                if len(wirusy) == 0:
                    print(f"\nKoniec gry! Gracz {gracz_id} ma 4 karty z organem.")
                    exit()


    def rozgrywka(self):
        #plansza powinna miec liste graczy/botow
        koniec = False
        while koniec is False:

            for gracz in self.gracze:
                print('RUCH GRACZA: ', gracz.gracz_id)
                #sleep(0.1)
                print('Karty na rece: ')
                self.ui.pokaz_karty_na_reku(gracz.gracz_id)
                #sleep(0.1)
                print('\nKarty wylozone prez gracza ' + str(gracz.gracz_id) + ': ')
                self.ui.pokaz_karty_wylozone_gracza(gracz.gracz_id)
                #sleep(0.1)
                print('\nKarty wylozone: ')
                self.ui.pokaz_wylozone_karty()
                #sleep(0.1)
                gracz.wykonaj_ruch()
                self.sprawdz_czy_koniec()


                #input('\nNacisnij dowolny przycisk aby kontynuowac: ')


