class Gracz:
    def __init__(self, id, nazwa):
        self.id = id
        self.nazwa = nazwa

    def wymien_karte(self):
        print("Wymineniam karte!")

    def wyloz_karte(self):
        print("Wykladam karte!")

def main():
    gracz1 = Gracz(1, "Gracz1")
    gracz1.wymien_karte()
    gracz1.wyloz_karte()

main()
