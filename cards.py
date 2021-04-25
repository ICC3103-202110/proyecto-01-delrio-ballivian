
from player import *
from random import *

class Cards:
    def __init__(self):
        self.deck = ["duke",  "assasin", "captain", "ambassador", "contessa" ]*3
        self.__deck1 = ["duke",  "assasin", "captain", "ambassador", "contessa" ]*3
        

    def give_cards(self, player):
        #current_cards = len(self.deck)
        print(self.deck, "DECK ALL")
        card1 = randint(0, len(self.deck)-1)        
        print(card1 ,"card1", self.deck[card1])
        
        card2 = randint(0, len(self.deck)-2)
        print(card2 ,"card2", self.deck[card2])
        
        print(len(self.deck), "LEN deck pre")
        
        
        dos_cartas = [self.deck[card1], self.deck[card2]]
        
        self.deck.pop(card1)
        self.deck.pop(card2)

        print(len(self.deck), "LEN deck post")
        
        print(self.deck, "DECK POS POP")
        
        print("player is cards ", player.name_id)
        return dos_cartas

    def return_card(self, player, index):
        self.deck.append(player.cards[index])
        player.cards.pop(index)
        card = randint(0, len(self.deck)-1)
        card_add=[self.deck[card]]
        player.cards.append(card_add[0])