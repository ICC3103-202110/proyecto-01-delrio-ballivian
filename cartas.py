from player import Player
from core_dumped import *


class action():
    name = ""
    description = ""
    block=[]
    coins_needed = 0
    def plays(self,player,target = None):
        return (False, None)

class income(action):
    name = "income"
    description = "gain 1 coin"
    def plays(self,player,target = None):
        Player.coins += 1
        return True, "Succed"

class foreing_aid(action):
    name = "foreing_aid"
    description = "gains 2 coins"
    def plays(self,player,target = None):
        Player.coins += 2
        return True, "Succed"

class coup(action):
    name = "coup"
    description = "Pay 7 gold to remove target player's influence"
    coins_needed = 7

    def play(self, player, target=None):
        if player.coins < self.coinsNeeded:
            raise NotEnoughCoins(self.coinsNeeded)

        # target should be alive
        if target == None:
            raise TargetRequired

        if not target.alive:
            raise InvalidTarget("Target is dead")

        player.coins -= 7
        target.loseInfluence()
        return True, "Success"

    class assasin(action):
        name = "assasin"
        description = "Assasinate. Pay 3 coins to kill a player's influence."
        coins_needed = 3

        def play(self, player, target=None):
            if player.coins < self.coinsNeeded:
                raise NotEnoughCoins(self.coinsNeeded)
            if target == None:
                raise TargetRequired

            player.coins -= 3
            target.loseInfluence()

            return True, "Success"

    #el duke se debe poder bloquear con otra carta
    class duke(action):
        name = "duke"
        description = "Gain 3 gold. Blocks Foreign Aid"
        def plays(self,player,target = None):
            player.coins += 3

#embajador tambien se puede bloquear
    class abassador(action):
        name = "abassador"
        description = "Exchange your influence with 2 cards from the Court Deck. Blocks Steal"
    class captain(action):
        name = "captain"
        description = "Steal 2 gold from target. Blocks Steal"
        block=["captain"]
        def plays(self,player,target = None):
            if target == None:
                raise TargetRequired

            steal = 0
            if target.coins >= 2:
                steal = 2
            elif target.coins == 1:
                steal = 1

            target.coins -= steal
            if target.coins < 0: target.coins = 0
            player.coins += steal

            return True, "Success"

    class contessa(action):
        name = "contessa"
        description = "Blocks Assasination."
        block=["assasin"]
        def plays(self,player,taget = None):
            raise BlockOnly