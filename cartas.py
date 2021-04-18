from player import Player

class action():
    name = ""
    description = ""
    coins_needed = 0
    def plays(self,players):
        return (False, None)

class income(action):
    name = "income"
    description = "gain 1 coin"
    def plays(self,players):
        Player.coins += 1
        return True, "Succed"

class foreing_aid(action):
    name = "foreing_aid"
    description = "gains 2 coins"
    def plays(self,players):
        Player.coins += 2
        return True, "Succed"

class coup(action):
    name = "coup"
    description = "Pay 7 gold to remove target player's influence"
    coins_needed = 7
    def plays(self,players):
        if Player.coins < self.coins_needed:
            



    def assasin(self):
        return 0
    def duke(self):
        return 0
    def abassador(self):
        return 0
    def captain(self):
        return 0
    def contessa(self):
        return 0
