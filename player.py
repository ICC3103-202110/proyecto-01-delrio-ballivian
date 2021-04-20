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
