import random
from main import talia
class Karta:
    def __init__(self):
        self.talia = talia
    
    def losuj_karte(self):
        wylosowana_karta = random.choice(self.talia)
        print("Wylosowana karta to:", wylosowana_karta)

Karta().losuj_karte()
