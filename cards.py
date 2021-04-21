<<<<<<< HEAD
from player import *
from random import *

class Cards:
    def __init__(self):
        self.deck = ["duke",  "assasin", "captain", "ambassador", "contessa" ]*3

    def give_cards(self, player):
        cartas_actuales=len(self.deck)
        print(self.deck, "DECK")
        carta1 = randint(0, cartas_actuales-1)
        carta2 = randint(0, cartas_actuales-1)
        dos_cartas = [self.deck[carta1], self.deck[carta2]]


        self.deck.pop(carta1)
        self.deck.pop(carta2)
        print("cartas jugador ", player.name_id)
        return dos_cartas


    def devolver_carta(self, deck):
        pass
"""
varta=Cards()

jugador = Player("hola",0)
jugador_2= Player("chao",1)
print(varta.give_cards(jugador,varta))
print(varta.give_cards(jugador_2,varta))
print(len(varta.deck))
"""
=======
from player import Player
import random as rng
class Cards:
    def give_cards(player_list):
        deck = ["duke", "duke", "duke", "assasin", "assasin", "assasin", 
                "captain", "captain", "captain", "ambassador", "ambassador", "ambassador", 
                "contessa", "contessa", "contessa", ]
        rng.shuffle(deck)
        print(deck, "DECK")
        for i in range(len(player_list)):
            print("cartas jugador ", player_list[i].name_id)
            for j in range(2):
                player_list[i].cards[j] = deck[i+j]
                player_list[i].cards_0[j] = player_list[i].cards[j]
>>>>>>> eb18f2692faeecdd62207848803734ed4968a7ca
