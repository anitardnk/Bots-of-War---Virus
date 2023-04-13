

class Gracz:
    def __init__(self, gracz_id, nazwa):
        self.gracz_id = gracz_id
        self.nazwa = nazwa

    def wymien_karte(self, gracz_id):
        from interfejsy import InterfejsPlanszy
        karta=input("Wybierz karte do wymiany: ")
        return InterfejsPlanszy.wymien_karte(karta, gracz_id)

    def wyloz_karte(self, gracz_id):
        from interfejsy import InterfejsPlanszy
        karta=input("Wybierz karte do wylozenia: ")
        return InterfejsPlanszy.wyloz_karte(karta, gracz_id)
        

