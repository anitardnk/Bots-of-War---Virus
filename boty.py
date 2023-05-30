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
