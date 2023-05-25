import random
from gracz import Gracz
from posrednik import PosrednikGraczPlansza

class BotRandomowy(Gracz):

    def wykonaj_ruch(self):
        ruch = random.choice(['wymien', 'wyloz'])
        indeks_karty = random.randrange(0, 3)
        print('\n', ruch, indeks_karty)
        if ruch == "wymien":
            if self.PosrednikGraczPlansza.wymien_karte(indeks_karty, self.gracz_id) == False:
                print('bledny ruch')
                self.wykonaj_ruch()
        elif ruch == "wyloz":
            with open('Bots-of-War---Virus-main\Bots.txt', 'r') as plik:
                gracze = plik.readlines()
                ilosc_graczy = len(gracze)
            gracz_id_wyloz = random.randrange(1, ilosc_graczy)
            if self.PosrednikGraczPlansza.wyloz_karte(indeks_karty, self.gracz_id, gracz_id_wyloz) == False:
                print('bledny ruch')
                self.wykonaj_ruch()
