from plansza import Plansza

talia = ["zielony_organ",    
         "zielony_lek",    
         "zielony_wirus",    
         "czerwony_organ",    
         "czerwony_lek",    
         "czerwony_wirus",    
         "niebieski_organ",    
         "niebieski_lek",    
         "niebieski_wirus",    
         "żółty_organ",    
         "żółty_lek",    
         "żółty_wirus",    
         "wielokolorowy_organ",    
         "wielokolorowy_lek",    
         "wielokolorowy_wirus"]

#jezeli plik nie jest importowany
if __name__ == "__main__":
    Plansza = Plansza(talia)
    Plansza.rozdaj_karty(4)

    # zamiast tych printow bedzie klasa UI
    print(Plansza.karty_na_reku[1])
    print(Plansza.karty_na_reku[2])
    print(Plansza.karty_na_reku[3])
    print(Plansza.karty_na_reku[4])

    Plansza.poloz_karte(0, 1)
    Plansza.poloz_karte(0, 2)
    Plansza.poloz_karte(0, 3)
    Plansza.poloz_karte(0, 4)

    print(Plansza.karty_na_reku[1])
    print(Plansza.karty_na_reku[2])
    print(Plansza.karty_na_reku[3])
    print(Plansza.karty_na_reku[4])