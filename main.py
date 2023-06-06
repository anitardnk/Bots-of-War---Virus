from plansza import Plansza
from gracz import Gracz
from interfejsy import InterfejsPlanszy
from karta import Karta
from gracz import Gracz
from boty import BotRandomowy, BotSchematyczny
from posrednik import PosrednikGraczPlansza


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

karta21 = Karta("zielony", "lek")
karta22 = Karta("zielony", "lek")
karta23 = Karta("zielony", "lek")
karta24 = Karta("zielony", "lek")

karta25 = Karta("czerwony", "lek")
karta26 = Karta("czerwony", "lek")
karta27 = Karta("czerwony", "lek")
karta28 = Karta("czerwony", "lek")

karta29 = Karta("niebieski", "lek")
karta30 = Karta("niebieski", "lek")
karta31 = Karta("niebieski", "lek")
karta32 = Karta("niebieski", "lek")

karta33 = Karta("żółty", "lek")
karta34 = Karta("żółty", "lek")
karta35 = Karta("żółty", "lek")
karta36 = Karta("żółty", "lek")


karta37 = Karta("zielony", "wirus")
karta38 = Karta("zielony", "wirus")
karta39 = Karta("zielony", "wirus")
karta40 = Karta("zielony", "wirus")

karta41 = Karta("czerwony", "wirus")
karta42 = Karta("czerwony", "wirus")
karta43 = Karta("czerwony", "wirus")
karta44 = Karta("czerwony", "wirus")

karta45 = Karta("niebieski", "wirus")
karta46 = Karta("niebieski", "wirus")
karta47 = Karta("niebieski", "wirus")
karta48 = Karta("niebieski", "wirus")

karta49 = Karta("żółty", "wirus")
karta50 = Karta("żółty", "wirus")
karta51 = Karta("żółty", "wirus")
karta52 = Karta("żółty", "wirus")

'''
karta53 = Karta("wielokolorowy", "wirus")

karta54 = Karta("wielokolorowy", "organ")

karta55 = Karta("wielokolorowy", "lek")
karta56 = Karta("wielokolorowy", "lek")
karta57= Karta("wielokolorowy", "lek")
karta58 = Karta("wielokolorowy", "lek")
'''

# okroić talie tylko do organow
'''
talia = [karta1, karta2, karta3, karta4, karta5, karta6, karta7, karta8, karta9, karta10, 
         karta11, karta12, karta13, karta14, karta15, karta16, karta17, karta18, karta19, 
         karta20, karta21, karta22, karta23, karta24, karta25, karta26, karta27, karta28, karta29, 
         karta30, karta31, karta32, karta33, karta34, karta35, karta36, karta37, karta38, karta39, 
         karta40, karta41, karta42, karta43, karta44, karta45, karta46, karta47, karta48, karta49, 
         karta50, karta51, karta52, karta53, karta54, karta55, karta56, karta57, karta58]

talia = [karta1, karta2, karta3, karta4, karta5, karta6, karta7, karta8, karta9, karta10,
         karta11, karta12, karta13, karta14, karta15, karta16, karta17, karta18, karta19,
         karta20, karta21, karta22, karta23, karta24, karta25, karta26, karta27, karta28, karta29, 
         karta30, karta31, karta32, karta33, karta34, karta35, karta36]
'''

talia = [karta1, karta2, karta3, karta4, karta5, karta6, karta7, karta8, karta9, karta10,
         karta11, karta12, karta13, karta14, karta15, karta16, karta17, karta18, karta19,
         karta20, karta21, karta22, karta23, karta24, karta25, karta26, karta27, karta28, karta29,
         karta30, karta31, karta32, karta33, karta34, karta35, karta36, karta37, karta38, karta39,
         karta40, karta41, karta42, karta43, karta44, karta45, karta46, karta47, karta48, karta49,
         karta50, karta51, karta52]

if __name__ == "__main__":

    # liczba_graczy = int(input('Podaj liczbe graczy: '))
    # main ma teraz wykonywac k meczy - jeden TURNIEJ
    # main ma przechowywac liste zwyciezcow i zwracac ja na koniec TURNIEJU
    liczba_graczy = 0
    dict = {}
   
    with open('Bots.txt', 'r') as file:
        lines = file.readlines()
        liczba_graczy = len(lines)-1
        All_names = ''.join(lines)
        Buff = All_names.split('\n')
    for i in range(liczba_graczy):
        Buff[i] = Buff[i].split('|')
        dict[Buff[i][0]] = eval(Buff[i][1])
        
    last_line = lines[-1].strip()  # Extract the last line and remove leading/trailing whitespace

# Print the last line
    gracze = []
    liczba_graczy = 2  # do testowania lepiej dac jednego gracza
    Plansza = Plansza(talia)
    for gracz_id in range(1, liczba_graczy+1):
        posrednik = PosrednikGraczPlansza(Plansza, gracz_id)
        gracze.append(dict[Buff[gracz_id-1][0]](
            gracz_id, Buff[gracz_id-1][0], liczba_graczy, posrednik))
    Plansza.gracze = gracze
    Plansza.rozdaj_karty(liczba_graczy)
#    for i in range(int(Buff[-1])):
 #       print('----------------------------------------'+'Round '+str(i+1)+'--------------------------------------------------------')
        
    Plansza.rozgrywka()
    print("Gracz", All_names[gracz_id-1], "wygrał!")
