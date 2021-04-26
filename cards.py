
from player import *
from random import *

class Cards:
    def __init__(self):
        self.deck = ["duke",  "assasin", "captain", "ambassador", "contessa" ]*3
        self.__deck1 = ["duke",  "assasin", "captain", "ambassador", "contessa" ]*3
        

    def give_cards(self, player):
        card1 = randint(0, len(self.deck)-1)
        
        card2 = randint(0, len(self.deck)-2)
        
        
        dos_cartas = [self.deck[card1], self.deck[card2]]
        contador1=0
        contador2=0
        aux1 = self.deck[card1]
        aux2 = self.deck[card2]
        for i in self.deck:
            if aux1 == i and contador1==0:

                self.deck.remove(i)
                contador1=contador1+1
            elif aux2 == i and contador2==0:
                self.deck.remove(i)
                contador2 = contador2 + 1
        return dos_cartas

    def return_card(self, player, index):
        self.deck.append(player.cards[index])
        player.cards.pop(index)
        card = randint(0, len(self.deck)-1)
        card_add=[self.deck[card]]
        player.cards.append(card_add[0])