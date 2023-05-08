from plansza import Plansza
from gracz import Gracz
from interfejsy import InterfejsPlanszy
from plansza import Plansza
from karta import Karta
from gracz import Gracz
from boty import BotRandomowy


karta1 = Karta("zielony", "organ")
karta2 = Karta("zielony", "organ")
karta3 = Karta("zielony", "organ")
karta4 = Karta("zielony", "organ")
karta5 = Karta("zielony", "organ")

karta6 = Karta("czerwony", "organ")
karta7 = Karta("czerwony", "organ")
karta8 = Karta("czerwony", "organ")
karta9 = Karta("czerwony", "organ")
karta10 = Karta("czerwony", "organ")

karta11 = Karta("niebieski", "organ")
karta12 = Karta("niebieski", "organ")
karta13 = Karta("niebieski", "organ")
karta14 = Karta("niebieski", "organ")
karta15 = Karta("niebieski", "organ")

karta16 = Karta("żółty", "organ")
karta17 = Karta("żółty", "organ")
karta18 = Karta("żółty", "organ")
karta19 = Karta("żółty", "organ")
karta20 = Karta("żółty", "organ")

karta21 = Karta("wielokolorowy", "organ")
'''
karta22 = Karta("zielony", "lek")
karta23 = Karta("zielony", "lek")
karta24 = Karta("zielony", "lek")
karta25 = Karta("zielony", "lek")

karta26 = Karta("czerwony", "lek")
karta27 = Karta("czerwony", "lek")
karta28 = Karta("czerwony", "lek")
karta29 = Karta("czerwony", "lek")

karta30 = Karta("niebieski", "lek")
karta31 = Karta("niebieski", "lek")
karta32 = Karta("niebieski", "lek")
karta33 = Karta("niebieski", "lek")

karta34 = Karta("żółty", "lek")
karta35 = Karta("żółty", "lek")
karta36 = Karta("żółty", "lek")
karta37 = Karta("żółty", "lek")

karta38 = Karta("wielokolorowy", "lek")
karta39 = Karta("wielokolorowy", "lek")
karta40= Karta("wielokolorowy", "lek")
karta41 = Karta("wielokolorowy", "lek")

karta42 = Karta("zielony", "wirus")
karta43 = Karta("zielony", "wirus")
karta44 = Karta("zielony", "wirus")
karta45 = Karta("zielony", "wirus")

karta46 = Karta("czerwony", "wirus")
karta47 = Karta("czerwony", "wirus")
karta48 = Karta("czerwony", "wirus")
karta49 = Karta("czerwony", "wirus")

karta50 = Karta("niebieski", "wirus")
karta51 = Karta("niebieski", "wirus")
karta52 = Karta("niebieski", "wirus")
karta53 = Karta("niebieski", "wirus")

karta54 = Karta("żółty", "wirus")
karta55 = Karta("żółty", "wirus")
karta56 = Karta("żółty", "wirus")
karta57 = Karta("żółty", "wirus")

karta58 = Karta("wielokolorowy", "wirus")
'''

#okroić talie tylko do organow
'''
talia = [karta1, karta2, karta3, karta4, karta5, karta6, karta7, karta8, karta9, karta10, 
         karta11, karta12, karta13, karta14, karta15, karta16, karta17, karta18, karta19, 
         karta20, karta21, karta22, karta23, karta24, karta25, karta26, karta27, karta28, karta29, 
         karta30, karta31, karta32, karta33, karta34, karta35, karta36, karta37, karta38, karta39, 
         karta40, karta41, karta42, karta43, karta44, karta45, karta46, karta47, karta48, karta49, 
         karta50, karta51, karta52, karta53, karta54, karta55, karta56, karta57, karta58]
'''
talia = [karta1, karta2, karta3, karta4, karta5, karta6, karta7, karta8, karta9, karta10, 
         karta11, karta12, karta13, karta14, karta15, karta16, karta17, karta18, karta19, 
         karta20, karta21]


if __name__ == "__main__":

    #liczba_graczy = int(input('Podaj liczbe graczy: '))
    #main ma teraz wykonywac k meczy - jeden TURNIEJ
    #main ma przechowywac liste zwyciezcow i zwracac ja na koniec TURNIEJU
    
    liczba_graczy = 1
    gracze = []
    Plansza = Plansza(talia)
    for gracz_id in range(1, liczba_graczy+1):
        gracze.append(BotRandomowy(gracz_id, 'bot', liczba_graczy, Plansza))
    Plansza.gracze = gracze
    Plansza.rozdaj_karty(liczba_graczy)
    Plansza.rozgrywka()
