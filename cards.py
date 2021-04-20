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