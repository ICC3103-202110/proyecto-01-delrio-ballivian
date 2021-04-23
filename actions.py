from player import *
from screen_update import *
from cards import *
import tkinter as tki
class Actions:
    def __init__(self):
        
        pass
    def foreingn_aid(self, player_list ,playern,Mazo):
        
        print(player_list[playern].name_id, playern, "yes")
        screen_update = Screen_update(player_list)
        self.counteraction(player_list[playern], player_list, playern,"foreingn_aid",Mazo)
        return True

    def remove(self,player, player_list, playern, name):
        screen_update = Screen_update(player_list)
        cardloose_select = tki.Tk()
        cardloose_select.title("Coup")
        cardloose_select.geometry("300x200")
        
        def cardloose(card, name):
            cardloose_select.destroy()

            if(name == "duke" or name == "coup" or name == "foreingn_aid" or name == "assassin"):

                if card == player.cards[0]:
                    player.show[0] = player.cards[0]
                    player.cards[0] = " "
                #Lose card 1
                elif card == player.cards[1]: 
                    player.show[1] = player.cards[1]
                    player.cards[1] = " "
                    
            elif name == "captain":
                if card == player.cards[0]:
                    player.show[0] = player.cards[0]
                    player.cards[0] = " "
                    
                    if player.coins == 1:
                        player.coins -= 1
                        player_list[playern].coins += 1
                    else:
                        player.coins -= 2
                        player_list[playern].coins += 2
                #Lose card 1
                elif card == player.cards[1]: 
                    player.show[1] = player.cards[1]
                    player.cards[1] = " "
                    if player.coins == 1:
                        player.coins -= 1
                        player_list[playern].coins += 1
                    else:
                        player.coins -= 2
                        player_list[playern].coins += 2
            
                
            screen_update.info()
        
        cardloose_label = tki.Label(cardloose_select, text=("Select card to lose " + str(player.name_id)), font="times 15")
        cardloose_label.pack()
        cardname1 = str(player.cards[0])
        card1 = tki.Button(cardloose_select, text=(cardname1), command = lambda: cardloose(cardname1, name), font="consolas 12")
        card1.pack()
        cardname2 = str(player.cards[1])
        card2 = tki.Button(cardloose_select, text=(cardname2), command = lambda: cardloose(cardname2, name), font="consolas 12")
        card2.pack()
        cardloose_select.mainloop()

    
    def challenge(self, playercounter, playerdoubt, player_list, playern, name,Mazo):
        print(playercounter.name_id, "EL PLAYER QUE ENTRA A CHALLENGE el counter")
        print(playerdoubt.name_id, "EL PLAYER QUE ENTRA A CHALLENGE el dudas")
        challenge_panel = tki.Tk()
        challenge_panel.geometry("300x300")
        challenge_label = tki.Label(challenge_panel, text="WHO DOUBTS THIS ACTION?", font="Consolas 15")
        challenge_label.pack()
        
        
        def action(action, playercounter, playerdoubt, playern, name,Mazo):
            print(playerdoubt.name_id, "Doubts  ", playercounter.name_id, "with ", action, "\ncard name: ", name)
            print(playerdoubt)
            if name == "foreingn_aid":
                challenge_panel.destroy()
                name = "duke" #DUKE BLOCKS FEINGN AID
                print("DUDASTE FOREGINNASDA AID DXDXAAA")
                if action == "challenge_none":
                    player_list[playern].coins +=2
                    
                elif action == "challenge_p1":
                    print(playerdoubt.name_id, "Este sopenco dudo challenge p1")
                    print(playercounter.name_id, "Este sopenco counterio challenge p1, sus cartas son: ", playercounter.cards)
                    
                    if name in playercounter.cards:
                        print("ESTOY DENTRO P1")
                        index=playercounter.cards.index(name)
                        Mazo.return_card(playercounter, index)
                        print(playerdoubt.cards)
                        print("cartas son",playercounter.cards)
                        self.remove(playerdoubt, player_list, playern, name)
    
                    else:
                        self.remove(playercounter, player_list, playern, name)
    
                elif action == "challenge_p2":
                    print(playerdoubt.name_id, "Este sopenco dudo challenge p2")
                    print(playercounter.name_id, "Este sopenco counterio challenge p2, sus cartas son: ", playercounter.cards)
                    
                    if name in playercounter.cards:
                        print("ESTOY DENTRO P1")
                        index = playercounter.cards.index(name)
                        Mazo.return_card(playercounter, index)
                        print(playerdoubt.cards)
                        print("cartas son", playercounter.cards)


                        self.remove(playerdoubt, player_list, playern, name)
                    else:
                        self.remove(playercounter, player_list, playern, name)
    
                elif action == "challenge_p3":
                    print(playerdoubt.name_id, "Este sopenco dudo challenge p3")
                    print(playercounter.name_id, "Este sopenco counterio challenge p3, sus cartas son: ", playercounter.cards)
                    
                    if name in playercounter.cards:
                        print("ESTOY DENTRO P1")
                        index = playercounter.cards.index(name)
                        Mazo.return_card(playercounter, index)
                        print(playerdoubt.cards)
                        print("cartas son", playercounter.cards)
                        self.remove(playerdoubt, player_list, playern, name)
                    else:
                        self.remove(playercounter, player_list, playern, name)
    
                elif action == "challenge_p4":
                    if name in playercounter.cards:
                        index = playercounter.cards.index(name)
                        Mazo.return_card(playercounter, index)
                        print(playerdoubt.cards)
                        print("cartas son", playercounter.cards)
                        self.remove(playerdoubt, player_list, playern, name)
                    else:
                        self.remove(playercounter, player_list, playern, name)
                    
            #----------------------------------------------------------
            else:
                player = playerdoubt
                challenge_panel.destroy()
                if action == "challenge_none":
                    if name == "duke":
                        player_list[playern].coins +=3
                        
                    elif name == "captain":
                        if playerdoubt.coins == 1:
                            playerdoubt.coins -= 1
                            player_list[playern].coins += 1
                        else:
                            playerdoubt.coins -= 2
                            player_list[playern].coins += 2
                    elif name == "assassin":
                            self.remove(player, player_list, playern, name)
    
                    return 0
                elif action == "challenge_p1":
                    if name in player_list[playern].cards:
                        index=player_list[playern].cards.index(name)
                        Mazo.return_card(player_list[playern], index)
                        print("cartas son", playercounter.cards)

                        print(playerdoubt.cards)
                        self.remove(player, player_list, playern, name)
    
                    else:
                        self.remove(player_list[playern], player_list, playern, name)
    
                elif action == "challenge_p2":
                    if name in player_list[playern].cards:
                        index = player_list[playern].cards.index(name)
                        Mazo.return_card(player_list[playern], index)
                        print("cartas son", playercounter.cards)
                        print(playerdoubt.cards)
                        self.remove(player, player_list, playern, name)
                    else:
                        self.remove(player_list[playern], player_list, playern, name)
    
                elif action == "challenge_p3":
                    if name in player_list[playern].cards:
                        index = player_list[playern].cards.index(name)
                        Mazo.return_card(player_list[playern], index)
                        print("cartas son", playercounter.cards)
                        print(playerdoubt.cards)
                        self.remove(player, player_list, playern, name)
                    else:
                        self.remove(player_list[playern], player_list, playern, name)
    
                elif action == "challenge_p4":
                    if name in player_list[playern].cards:
                        index = player_list[playern].cards.index(name)
                        Mazo.return_card(player_list[playern], index)
                        print("cartas son", playercounter.cards)
                        print(playerdoubt.cards)
                        self.remove(player, player_list, playern, name)
                    else:
                        self.remove(player_list[playern], player_list, playern, name)
                pass
                
        #PLAYER WHO

        challenge_1 = tki.Button(challenge_panel, text="Player 1", font="consolas 20", command = lambda: action("challenge_p1", playercounter, player_list[0], playern, name,Mazo))
        challenge_1.pack()
        challenge_2 = tki.Button(challenge_panel, text="Player 2", font="consolas 20", command = lambda: action("challenge_p2", playercounter, player_list[1], playern, name,Mazo))
        challenge_2.pack()
        challenge_3 = tki.Button(challenge_panel, text="Player 3", font="consolas 20", command = lambda: action("challenge_p3", playercounter, player_list[2], playern, name,Mazo))
        challenge_3.pack()

        if len(player_list) == 4:
            challenge_4 = tki.Button(challenge_panel, text="Player 4", font="consolas 20", command = lambda: action("challenge_p4", playercounter, player_list[3], playern, player_list,Mazo))
            challenge_4.pack()

        challenge_none = tki.Button(challenge_panel, text =" Pass ", font="consolas 20", command = lambda: action("challenge_none", playercounter, player_list[0], playern, player_list,Mazo))
        challenge_none.pack()
        
        challenge_panel.mainloop()
    def counteraction(self, player, player_list, playern, name,Mazo):

        screen_update = Screen_update(player_list)
        ca_panel = tki.Tk()
        ca_panel.title("COUNTER ACTION")
        ca_panel.geometry("300x300")

        def action(action, target, playern, player_list, name,Mazo):
            print("player action ", action, "el que recive challenge ", player_list[playern].name_id)
            if playern == target:
                print("AUTO CONTRACTION BLOCKED")
            else:
                ca_panel.destroy()
                if action == "ca_p1":
                    print(player_list[0].name_id, "DO COUNTERACTION TO ", player.name_id)
                    
                    
                    self.challenge(player_list[0], player_list[0], player_list, playern, name,Mazo)
                elif action == "ca_p2":
                    print(player_list[1].name_id, "DO COUNTERACTION TO ", player.name_id)

                    self.challenge(player_list[1], player_list[0],player_list, playern, name,Mazo)
                elif action == "ca_p3":
                    print(player_list[2].name_id, "DO COUNTERACTION TO ", player.name_id)
                    
                    self.challenge(player_list[2], player_list[0],player_list, playern, name,Mazo)
                elif action == "ca_p4":
                    print("Player 4 DO COUNTERACTION TO ", player.name_id)

                    print(player_list[3].name_id, "DO COUNTERACTION TO ", player.name_id)
                    self.challenge(player_list[3], player_list[0],player_list, playern, name,Mazo)
                elif action == "ca_none":
                    if name == "foreingn_aid":
                        print("PASS")
                        player_list[playern].coins += 2
                        screen_update.info()
                    elif name == "duke":
                        print("PASS")
                        player_list[playern].coins += 3
                        screen_update.info()
                    elif name == "captain":
                        
                        pass
                
        #PANEL DE COUNTER ACTION

        ca_label = tki.Label(ca_panel, text="WHO IS COUNTERACTION?", font="Consolas 15")
        ca_label.pack()

        #PLAYER WHO

        ca_1 = tki.Button(ca_panel, text="Player 1", font="consolas 20", command = lambda: action("ca_p1", 0, playern, player_list, name,Mazo))
        ca_1.pack()
        ca_2 = tki.Button(ca_panel, text="Player 2", font="consolas 20", command = lambda: action("ca_p2", 1, playern, player_list, name,Mazo))
        ca_2.pack()
        ca_3 = tki.Button(ca_panel, text="Player 3", font="consolas 20", command = lambda: action("ca_p3", 2, playern, player_list, name,Mazo))
        ca_3.pack()

        if len(player_list) == 4:
            ca_4 = tki.Button(ca_panel, text="Player 4", font="consolas 20", command = lambda: action("ca_p4", 3, playern,player_list, name,Mazo))
            ca_4.pack()

        ca_none = tki.Button(ca_panel, text =" Pass ", font="consolas 20", command = lambda: action("ca_none", 10, playern,player_list, name,Mazo))
        ca_none.pack()

        ca_panel.mainloop()

        return True



    def tax(self, player_list, playern,Mazo):
        screen_update = Screen_update(player_list)
        self.challenge(player_list[playern], player_list[playern], player_list, playern,"duke",Mazo)

        
    def steal(self,player, player_list, playern, name,Mazo):
        screen_update = Screen_update(player_list)
        steal_panel = tki.Tk()
        steal_panel.title("STEAL")
        steal_panel.geometry("320x300")
        def action(action, target, playern, player_list, name,Mazo):
            if playern == target:
                print("AUTO STEAL BLOCKED")
            else:
                steal_panel.destroy()
                if action == "steal_p1":
                    print("Player 1 DO STEAL TO ", playern + 1)
                    
                    self.challenge(player_list[0], player_list[0], player_list, playern, name,Mazo)
                elif action == "steal_p2":
                    print("Player 2 DO STEAL TO ", playern + 1)
                    
                    self.challenge(player_list[1], player_list[0], player_list, playern, name,Mazo)
                elif action == "steal_p3":
                    print("Player 3 DO STEAL TO ", playern + 1)

                    self.challenge(player_list[2], player_list[0], player_list, playern, name,Mazo)
                elif action == "steal_p4":
                    print("Player 4 DO STEAL TO ", playern + 1)
                    self.challenge(player_list[3], player_list[0], player_list, playern, name,Mazo)
    


        steal_label = tki.Label(steal_panel, text="WHO are going to steal from?", font="Consolas 15")
        steal_label.pack()


        steal_1 = tki.Button(steal_panel, text="Player 1", font="consolas 20", command = lambda: action("steal_p1", 0, playern, player_list, name,Mazo))
        steal_1.pack()
        steal_2 = tki.Button(steal_panel, text="Player 2", font="consolas 20", command = lambda: action("steal_p2", 1, playern, player_list, name,Mazo))
        steal_2.pack()
        steal_3 = tki.Button(steal_panel, text="Player 3", font="consolas 20", command = lambda: action("steal_p3", 2, playern, player_list, name,Mazo))
        steal_3.pack()

        if len(player_list) == 4:
            steal_4 = tki.Button(steal_panel, text="Player 4", font="consolas 20", command = lambda: action("steal_p4", 3, playern,player_list, name,Mazo))
            steal_4.pack()


        steal_panel.mainloop()

        return True

    def assassinate(self,player, player_list, playern, name,Mazo): #Añadir deabte de debate
        
        screen_update = Screen_update(player_list)
        kill_panel = tki.Tk()
        kill_panel.title("kill")
        kill_panel.geometry("320x300")
        
        
        def action(action, target, playern, player_list, name,Mazo):
            if playern == target:
                print("AUTO kill BLOCKED")
            else:
                kill_panel.destroy()
                if action == "kill_p1":
                    print("Player ", playern + 1, " kill TO Player 1", )
                    
                    
                    player.coins -= 3 
                    #self.remove(player_list[0], player_list, playern, name)
                    self.challenge(player_list[0], player_list[0], player_list, playern, name,Mazo)
            
                elif action == "kill_p2":
                    print("Player ", playern + 1, " kill TO Player 2", )
                    
                    player.coins -= 3 
                    #self.remove(player_list[1], player_list, playern, name)
                    self.challenge(player_list[1], player_list[0], player_list, playern, name,Mazo)
                    
                elif action == "kill_p3":
                    print("Player ", playern + 1, " kill TO Player 3", )
                    
                    player.coins -= 3 
                    #self.remove(player_list[2], player_list, playern, name)
                    self.challenge(player_list[2], player_list[0], player_list, playern, name,Mazo)
                    
                elif action == "kill_p4":
                    print("Player ", playern + 1, " kill TO Player 4", )
                    
                    player.coins -= 3 
                    #self.remove(player_list[3], player_list, playern, name)
                    self.challenge(player_list[3], player_list[0], player_list, playern, name,Mazo)

        kill_label = tki.Label(kill_panel, text="WHO are going to assassinate?", font="Consolas 15")
        kill_label.pack()

        kill_1 = tki.Button(kill_panel, text="Player 1", font="consolas 20", command = lambda: action("kill_p1", 0, playern, player_list, name,Mazo))
        kill_1.pack()
        kill_2 = tki.Button(kill_panel, text="Player 2", font="consolas 20", command = lambda: action("kill_p2", 1, playern, player_list, name,Mazo))
        kill_2.pack()
        kill_3 = tki.Button(kill_panel, text="Player 3", font="consolas 20", command = lambda: action("kill_p3", 2, playern, player_list, name,Mazo))
        kill_3.pack()

        if len(player_list) == 4:
            kill_4 = tki.Button(kill_panel, text="Player 4", font="consolas 20", command = lambda: action("kill_p4", 3, playern,player_list, name,Mazo))
            kill_4.pack()


        kill_panel.mainloop()

        return True
    def exchange(self,player, player_list, playern, name,Mazo):
        screen_update = Screen_update(player_list)
        self.challenge(self, player_list[playern], player_list[playern], player_list, playern, name, Mazo)
        dos_cartas=Mazo.give_cards(player)
        print(dos_cartas,player.cards)
        cards_total=[]
        for i in range(len(dos_cartas)):
            cards_total.append(dos_cartas[i])
        for i in range(len(player.cards)):
            cards_total.append(player.cards[i])

        card1=int(input("ingrese del 1 al 4 las cartas que quiere mantener"))
        card2=int(input("ingrese del 1 al 4 las cartas que quiere mantener"))
        player.cards[0]=cards_total[card1-1]
        player.cards[0] = cards_total[card1 - 1]
        print(player.cards)
        return True






    def coup(self, player, player_list):
        screen_update = Screen_update(player_list)

        coup_panel = tki.Tk()
        coup_panel.title("Coup")
        coup_panel.geometry("300x300")

        def coup_target(playern, target):
            
            print("ATTACKER ",player.name_id , "TARGET ", target)
            if player_list[playern].alive == False:
                print("Player attacked is OUT")
                return(0)
            elif player_list[playern].alive == True:
                if target == player.name_id:
                    print("Auto Attack not allowed")
                    return(0)
                elif target != player.name_id:
                    coup_panel.destroy()
                    
                    player_list[playern].influence -=1
                    print(player_list[playern].influence, " INFLUENCE OF THE ATTACK ")
                    self.remove(player_list[playern], player_list, playern, "coup")


            return 0

        coup_title = tki.Label(coup_panel, text="Who to Coup?", font=("Times", 35, "bold italic"), bg="grey", fg="white")
        coup_title.pack()
        coup_1 = tki.Button(coup_panel, text="coup Player 1", font="consolas 20", command = lambda: coup_target(0, "jugador 1"))
        coup_1.pack()
        coup_2 = tki.Button(coup_panel, text="coup Player 2", font="consolas 20", command = lambda: coup_target(1, "jugador 2"))
        coup_2.pack()
        coup_3 = tki.Button(coup_panel, text="coup Player 3", font="consolas 20", command = lambda: coup_target(2, "jugador 3"))
        coup_3.pack()
        if len(player_list) == 4:
            coup_4 = tki.Button(coup_panel, text="coup Player 4", font="consolas 20", command = lambda: coup_target(3, "jugador 4"))
            coup_4.pack()
        coup_panel.mainloop()
        return True


    #def golpe(): #SI EL JUGADOR TIENE 10 MONEDAS DEBE REALIZAR ESTA EJECUCION SI O SI
     #   return 0
