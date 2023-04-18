import random
from gracz import Gracz
from posrednik import PosrednikGraczPlansza

class BotRandomowy(Gracz):

    def wykonaj_ruch(self):
        ruch = random.choice(['wymien', 'wyloz'])
        indeks_karty = random.randrange(0, 3)
        print(ruch, indeks_karty)
        if ruch == "wymien":
            if self.PosrednikGraczPlansza.wymien_karte(indeks_karty, self.gracz_id) == False:
                print('bledny ruch')
                self.wykonaj_ruch()
        elif ruch == "wyloz":
            if self.PosrednikGraczPlansza.wyloz_karte(indeks_karty, self.gracz_id) == False:
                print('bledny ruch')
                self.wykonaj_ruch()
