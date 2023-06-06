import random
from gracz import Gracz
from posrednik import PosrednikGraczPlansza

class BotRandomowy(Gracz):

    def wykonaj_ruch(self):
        ruch = random.choice(['wymien', 'wyloz'])
        indeks_karty = random.randrange(0, 3)
        karta = self.PosrednikGraczPlansza.karty_gracza()
        if ruch == "wymien":
            print('\n', ruch, karta[indeks_karty])
            if self.PosrednikGraczPlansza.wymien_karte(indeks_karty) == False:
                print('bledny ruch')
                self.wykonaj_ruch()
        elif ruch == "wyloz":
            gracz_id_wyloz = random.randrange(1, self.ilosc_graczy+1)
            print('\n', ruch, karta[indeks_karty], 'na pole gracza: ', gracz_id_wyloz)
            if self.PosrednikGraczPlansza.wyloz_karte(indeks_karty, gracz_id_wyloz) == False:
                print('bledny ruch')
                self.wykonaj_ruch()

class BotSchematyczny(Gracz):

    def wykonaj_ruch(self):
        karty = self.PosrednikGraczPlansza.karty_gracza_obiekt()
        for karta in karty:
            if karta.funkcja == 'organ':
                 indeks_karty = karty.index(karta)
                # print('\n wyloz ', karta.funkcja, karta.kolor, 'na pole gracza: ', self.gracz_id)
                 if self.PosrednikGraczPlansza.wyloz_karte(indeks_karty, self.gracz_id) == False:
                    #print('bledny ruch')
                    pass
        for karta in karty:
            if karta.funkcja == 'lek':
                 indeks_karty = karty.index(karta)
                 gracz_id_wyloz = random.randrange(1, self.ilosc_graczy+1)
                 #print('\n wyloz ', karta.funkcja, karta.kolor, 'na pole gracza: ', gracz_id_wyloz)
                 if self.PosrednikGraczPlansza.wyloz_karte(indeks_karty, gracz_id_wyloz) == False:
                   # print('bledny ruch')
                   pass
        for karta in karty:
            if karta.funkcja == 'wirus':
                 indeks_karty = karty.index(karta)
                 gracz_id_wyloz = random.randrange(1, self.ilosc_graczy+1)
                # print('\n wyloz', karta.funkcja, karta.kolor, 'na pole gracza: ', gracz_id_wyloz)
                 if self.PosrednikGraczPlansza.wyloz_karte(indeks_karty, gracz_id_wyloz) == False:
                    #print('bledny ruch')
                    pass
        
        print('\n wymien', karta.funkcja, karta.kolor)
        indeks_karty = random.randrange(0, 3)
        if self.PosrednikGraczPlansza.wymien_karte(indeks_karty) == False:
            #print('bledny ruch')
            pass
