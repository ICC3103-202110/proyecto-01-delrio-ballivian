#clase jugador


from cartas import *
class Player:

    def __init__(self):
        #self.name = name
        self.turn = 0
        self.coins = 2

        self.alive = True

    def in_game(self):
        card1=Mazo.select_card()
        card2=Mazo.select_card()
        self.cards_influece=[card1,card2]
player=Player()
print("carta 1 y carta 2",player.in_game())



