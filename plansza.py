import random
from interfejsy import InterfejsPlanszy
from time import sleep
from UI import ui


class Plansza(InterfejsPlanszy):

    def __init__(self, talia):
        self.talia = talia  # lista objektow klasy Karta
        self.karty_pozostale = self.talia[:]
        self.karty_uzyte = []
        self.ui = ui(self)
        self.karty_polozone = {}
        self.karty_na_reku = {}
        self.ilosc_graczy = 0
        self.rachunek = {}
        self.count_rund = 1

    def rozdaj_karty(self, ilosc_graczy):
        self.ilosc_graczy = ilosc_graczy
        self.ui.pokaz_nr_rounda(self.count_rund)
        self.count_rund += 1
        for gracz_id in range(1, ilosc_graczy + 1):
            self.karty_polozone[gracz_id] = []
            self.karty_na_reku[gracz_id] = []
            self.daj_karty_graczowi(3, gracz_id)

    '''def daj_karty_graczowi(self, ilosc_kart, gracz_id):
        rozdane_karty = 0
        while rozdane_karty != ilosc_kart:
            karta = random.choice(self.karty_pozostale)
            self.karty_na_reku[gracz_id].append(karta)
            self.karty_pozostale.remove(karta)
            rozdane_karty += 1'''

    def daj_karty_graczowi(self, ilosc_kart, gracz_id):
        rozdane_karty = 0
        while rozdane_karty != ilosc_kart:
            if not self.karty_pozostale:
                self.tasuj_karty(self.karty_uzyte, self.karty_pozostale)
            karta = random.choice(self.karty_pozostale)

            if type(karta) is list:
                print(self.karty_pozostale)
                for i in karta:
                    print(i.funkcja, i.kolor)
                input()

            self.karty_na_reku[gracz_id].append(karta)

            self.karty_pozostale.remove(karta)
            rozdane_karty += 1

    def sprawdz_czy_ruch_legalny(self, karta, gracz_id, gracz_id_wyloz):
        if karta in self.karty_na_reku[gracz_id]:
            wylozone_karty_gracza = self.karty_polozone[gracz_id_wyloz]
            if karta.funkcja == 'lek':
                leki_tego_samego_koloru = [
                    i for i in wylozone_karty_gracza if i.funkcja == 'lek' and i.kolor == karta.kolor]
                if len(leki_tego_samego_koloru) >= 2:
                    return False
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
                leki_tego_samego_koloru = [
                    i for i in wylozone_karty_gracza if i.funkcja == 'lek' and i.kolor == karta.kolor]
                if len(leki_tego_samego_koloru) >= 2:
                    return False
                for i in wylozone_karty_gracza:
                    if (i.funkcja == 'organ' or i.funkcja == 'lek' or i.funkcja == 'wirus') and i.kolor == karta.kolor:
                        return True
                return False
        return False

    def sprawdz_skutki_ruchu(self, karta, gracz_id_wyloz):
        wylozone_karty_gracza = self.karty_polozone[gracz_id_wyloz]
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
            self.karty_polozone[gracz_id_wyloz] = [
                i for i in self.karty_polozone[gracz_id_wyloz] if i not in karty_do_usuniecia]
            self.karty_uzyte += karty_do_usuniecia
        elif len(wirusy) == 1 and len(leki) == 1:
            karty_do_usuniecia = leki + wirusy
            self.karty_polozone[gracz_id_wyloz] = [
                i for i in self.karty_polozone[gracz_id_wyloz] if i not in karty_do_usuniecia]
            self.karty_uzyte += karty_do_usuniecia

    def poloz_karte(self, indeks_karty, gracz_id, gracz_id_wyloz):
        karta = self.karty_na_reku[gracz_id][indeks_karty]
        self.karty_polozone[gracz_id_wyloz].append(karta)
        self.karty_na_reku[gracz_id].remove(karta)

    def wymien_karte(self, indeks_karty, gracz_id):
        # print('wymieniam karte '+ self.karty_na_reku[gracz_id][indeks_karty].kolor + self.karty_na_reku[gracz_id][indeks_karty].funkcja)
        self.karty_uzyte.append(self.karty_na_reku[gracz_id][indeks_karty])
        self.karty_na_reku[gracz_id].remove(
            self.karty_na_reku[gracz_id][indeks_karty])

    def ruch_gracza(self, gracz_id):
        # UI.pokaz_karty(gracz_id)
        # self.ui.pokaz_karty_gracza(gracz_id)
        pass

    def poinformuj_graczy_o_ruchu(self, delta):
        # delta = {'akcja': wyloz/wyien, 'indeks_karty': indeks_karty wykladanej/wymienianej, 'gracz_id' : gracz_id osoby wykonujacej ruch,
        #  'gracz_id_wyloz': gracz_id u kogo sie wyklada karte }
        if delta['akcja'] == 'wymien':
            karta = self.karty_uzyte[0].kolor, self.karty_uzyte[0].funkcja
            for gracz in self.gracze:
                gracz.aktualizacja_planszy_po_ruchu_wymien(delta, karta)
        elif delta['akcja'] == 'wyloz':
            karta = self.karty_polozone[delta['gracz_id_wyloz']][0]
            for gracz in self.gracze:
                gracz.aktualizacja_planszy_po_ruchu_wyloz(delta, karta)

    def tasuj_karty(self, ilosc_kart, gracz_id):
        self.karty_pozostale = self.karty_uzyte[:-1]
        self.karty_uzyte = [self.karty_uzyte[-1]]
        # random.shuffle(karty_tasowane)

        # input()

    def sprawdz_czy_koniec(self):
        # 4 ograny bez zadnego wirusa - stan na 23.05 4 kolory organow - nie moze byc zadnego wirusa
        for gracz_id, karty_gracza in self.karty_polozone.items():
            karty_z_organem = [
                karta for karta in karty_gracza if karta.funkcja == "organ"]
            if len(karty_z_organem) == 4:
                wirusy = [
                    karta for karta in karty_gracza if karta.funkcja == "wirus"]
                if len(wirusy) == 0:
                    # print(f"\nKoniec gry! Gracz {gracz_id} ma 4 karty z organem.")
                    # quit()
                    # self.tasuj_karty(self, gracz_id)
                    return gracz_id
        return False

    def rozgrywka(self, doi, delay):
        # plansza powinna miec liste graczy/botow
        koniec = False
        while koniec is False:
            for gracz in self.gracze:
                print('RUCH GRACZA: ', gracz.gracz_id)
                # sleep(0.1)
                if doi == 'd':
                    sleep(delay)
                if doi == 'i':
                    input()
                print('Karty na rece: ')
                self.ui.pokaz_karty_na_reku(gracz.gracz_id)
                # sleep(0.1)
                if doi == 'd':
                    sleep(delay)
                if doi == 'i':
                    input()
                print('\nKarty wylozone prez gracza ' +
                      str(gracz.gracz_id) + ': ')
                self.ui.pokaz_karty_wylozone_gracza(gracz.gracz_id)
                # sleep(0.1)
                if doi == 'd':
                    sleep(delay)
                if doi == 'i':
                    input()
                print('\nKarty wylozone: ')
                self.ui.pokaz_wylozone_karty()
                # sleep(0.1)
                if doi == 'd':
                    sleep(delay)
                if doi == 'i':
                    input()
                gracz.wykonaj_ruch()
                wygrany = self.sprawdz_czy_koniec()
                if wygrany:
                    self.ui.pokaz_rezultat_gry(
                        self.ilosc_graczy, gracz.gracz_id)
                    koniec = True
                    input()
                    # break

                # input('\nNacisnij dowolny przycisk aby kontynuowac: ')

    def inizilizacja_rachuku(self, liczba_graczy):
        for i in range(liczba_graczy):
            self.rachunek["Gracz-" + str(i+1)] = 0
