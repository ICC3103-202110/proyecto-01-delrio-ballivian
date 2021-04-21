#clase jugador
class Player:

    def __init__(self, name_id, turno):
        self.name_id = name_id
        self.turno = turno
        self.coins = 2
        self.influence = 2
        self.alive = True
        self.cards = []
        self.show = ["hidden", "hidden"] #Cartas de aqui
    def player_state(player_list):
        for i in range(len(player_list)):
            if player_list[i].influence == 0:
                player_list[i].alive = False
            else:
                continue

    def cards_state(player_list):
        for i in range(len(player_list)):
            if (player_list[i].cards[0] == "duke" or player_list[i].cards[0] == "assasin" 
            or player_list[i].cards[0] == "ambassador" or player_list[i].cards[0] == "captain" 
            or player_list[i].cards[0] == "contessa"):
                print("none")
            elif (player_list[i].cards[1] == "duke" or player_list[i].cards[1] == "assasin" 
            or player_list[i].cards[1] == "ambassador" or player_list[i].cards[1] == "captain" 
            or player_list[i].cards[1] == "contessa"):
                print("none")
            else:
                if player_list[i].cards[0] == "Card losed": #La misma variable que en COUP
                    player_list[i].show[0] == player_list[i].cards_0[0]
                elif player_list[i].cards[1] == "Card losed": #La misma variable que en COUP
                    player_list[i].show[1] == player_list[i].cards_0[1]
                return 0

