from plansza import Plansza
from gracz import Gracz
from interfejsy import InterfejsPlanszy
from plansza import Plansza
from karta import Karta
from gracz import Gracz

karta1 = Karta("zielony", "wirus")
karta2 = Karta("zielony", "wirus")
karta3 = Karta("zielony", "wirus")
karta4 = Karta("zielony", "wirus")

karta5 = Karta("zielony", "organ")
karta6 = Karta("zielony", "organ")
karta7 = Karta("zielony", "organ")
karta8 = Karta("zielony", "organ")
karta9 = Karta("zielony", "organ")

karta10 = Karta("zielony", "lek")
karta11 = Karta("zielony", "lek")
karta12 = Karta("zielony", "lek")
karta13 = Karta("zielony", "lek")

karta14 = Karta("czerwony", "wirus")
karta15 = Karta("czerwony", "wirus")
karta16 = Karta("czerwony", "wirus")
karta17 = Karta("czerwony", "wirus")

karta18 = Karta("czerwony", "organ")
karta19 = Karta("czerwony", "organ")
karta20 = Karta("czerwony", "organ")
karta21 = Karta("czerwony", "organ")
karta22 = Karta("czerwony", "organ")

karta23 = Karta("czerwony", "lek")
karta24 = Karta("czerwony", "lek")
karta25 = Karta("czerwony", "lek")
karta26 = Karta("czerwony", "lek")

karta27 = Karta("niebieski", "wirus")
karta28 = Karta("niebieski", "wirus")
karta29 = Karta("niebieski", "wirus")
karta30 = Karta("niebieski", "wirus")

karta31 = Karta("niebieski", "organ")
karta32 = Karta("niebieski", "organ")
karta33 = Karta("niebieski", "organ")
karta34 = Karta("niebieski", "organ")
karta35 = Karta("niebieski", "organ")

karta36 = Karta("niebieski", "lek")
karta37 = Karta("niebieski", "lek")
karta38 = Karta("niebieski", "lek")
karta39 = Karta("niebieski", "lek")

karta40 = Karta("żółty", "wirus")
karta41 = Karta("żółty", "wirus")
karta42 = Karta("żółty", "wirus")
karta43 = Karta("żółty", "wirus")

karta44 = Karta("żółty", "organ")
karta45 = Karta("żółty", "organ")
karta46 = Karta("żółty", "organ")
karta47 = Karta("żółty", "organ")
karta48 = Karta("żółty", "organ")

karta49 = Karta("żółty", "lek")
karta50 = Karta("żółty", "lek")
karta51 = Karta("żółty", "lek")
karta52 = Karta("żółty", "lek")

karta53 = Karta("wielokolorowy", "wirus")

karta54 = Karta("wielokolorowy", "organ")

karta55 = Karta("wielokolorowy", "lek")
karta56 = Karta("wielokolorowy", "lek")
karta57= Karta("wielokolorowy", "lek")
karta58 = Karta("wielokolorowy", "lek")

#okroić talie tylko do organow
talia = [karta1, karta2, karta3, karta4, karta5, karta6, karta7, karta8, karta9, karta10, 
         karta11, karta12, karta13, karta14, karta15, karta16, karta17, karta18, karta19, 
         karta20, karta21, karta22, karta23, karta24, karta25, karta26, karta27, karta28, karta29, 
         karta30, karta31, karta32, karta33, karta34, karta35, karta36, karta37, karta38, karta39, 
         karta40, karta41, karta42, karta43, karta44, karta45, karta46, karta47, karta48, karta49, 
         karta50, karta51, karta52, karta53, karta54, karta55, karta56, karta57, karta58]


if __name__ == "__main__":

    liczba_graczy = int(input('Podaj liczbe graczy: '))
    gracze = []
    for gracz_id in range(1, liczba_graczy+1):
        gracze.append(Gracz(gracz_id, 'bot'))
    Plansza = Plansza(talia)
    Plansza.rozdaj_karty(liczba_graczy)


#    koniec = False
#    while koniec is False:
 #       for gracz in gracze:
            #UI.pokaz_karty(gracz_id)
    ########ta czesc trwa dopoki gracz nie zrobi legalnego ruchu (nie wylozy karty lubi nie wymieni kart - wymiana kart zawsze legalna)
    ########while True:
    ############ gracz.wykonaj_ruch()
    ############ if interfejsPlanszy.sprawdz_czy_ruch_legalny(): funkcja zwraca True/False
    ################ interfejsPlanszy.wykonaj_ruch(gracz.id)
    ################ break

    ############# if self.sprawdz_czy_wygral(gracz.id): funkcja zwraca True/False
    ################# break
    ############ self.daj_karty_graczowi(1, gracz.id)
