from player import *
from screen_update import *
import tkinter as tki
class Actions:
    def __init__(self):
        
        pass
    def foreingn_aid(self, player_list,playern):
        #COUNTER ACTION
        screen_update = Screen_update(player_list)
        self.counteraction(player_list[playern], player_list, playern,"foreingn_aid")
        """
        ca_panel = tki.Tk()
        ca_panel.title("COUNTER ACTION")
        ca_panel.geometry("300x300")

        def action(action, target, playern, player_list):
            if playern == target:
                print("AUTO CONTRACTION BLOCKED")
            else:
                ca_panel.destroy()
                if action == "ca_p1":
                    print("Player 1 DO COUNTERACTION TO ", playern + 1)
                    #preguntar otra vez quien quiere dudarle la carta al que
                    #esta contraatacando, cambialo a botones
                    
                    self.desafiar(player_list[0],"duke", player_list, playern)
                elif action == "ca_p2":
                    print("Player 2 DO COUNTERACTION TO ", playern + 1)

                    self.desafiar(player_list[1],"duke", player_list, playern)
                elif action == "ca_p3":
                    print("Player 3 DO COUNTERACTION TO ", playern + 1)

                    self.desafiar(player_list[2],"duke", player_list, playern)
                elif action == "ca_p4":
                    print("Player 4 DO COUNTERACTION TO ", playern + 1)

                    self.desafiar(player_list[3],"duke", player_list, playern)
                elif action == "ca_none":
                    print("PASS")
                    player_list[playern].coins += 2
                    screen_update.info()
        #PANEL DE COUNTER ACTION

        ca_label = tki.Label(ca_panel, text="WHO IS COUNTERACTION?", font="Consolas 15")
        ca_label.pack()

        #PLAYER WHO

        ca_1 = tki.Button(ca_panel, text="Player 1", font="consolas 20", command = lambda: action("ca_p1", 0, playern,player_list))
        ca_1.pack()
        ca_2 = tki.Button(ca_panel, text="Player 2", font="consolas 20", command = lambda: action("ca_p2", 1, playern,player_list))
        ca_2.pack()
        ca_3 = tki.Button(ca_panel, text="Player 3", font="consolas 20", command = lambda: action("ca_p3", 2, playern,player_list))
        ca_3.pack()

        if len(player_list) == 4:
            ca_4 = tki.Button(ca_panel, text="Player 4", font="consolas 20", command = lambda: action("ca_p4", 3, playern,player_list))
            ca_4.pack()

        ca_none = tki.Button(ca_panel, text =" Pass ", font="consolas 20", command = lambda: action("ca_none", 10, playern,player_list))
        ca_none.pack()

        ca_panel.mainloop()
        """
        return True

    #funcion que evalua el desafio y a quien quitar carta, la llamo en contraataque
    #tienes que juntar tu lista hidden con las cartas reveladas aqui
    def quitar_carta(self,player, player_list, playern):
        print(playern, "PLAYERN EN QUITAR CARTA---------------------")
        screen_update = Screen_update(player_list)
        cardloose_select = tki.Tk()
        cardloose_select.title("Coup")
        cardloose_select.geometry("300x200")
        def cardloose(card): #VER BIEN PARA VER CUALES SI ESTAN PERDIDAS, ACTUALMENTE SOLO ESTAN EN player.show[] -----------------------------------
            cardloose_select.destroy()
            #Lose card 0
            if card == player_list[playern].cards[0]:
                player_list[playern].show[0] = player_list[playern].cards[0]  #Reemplazo el show
            #Lose card 1
            elif card == player_list[playern].cards[1]: 
                player_list[playern].show[1] = player_list[playern].cards[1] #Reemplazo el show

            screen_update.info()
        
        cardloose_label = tki.Label(cardloose_select, text=("Select card to lose " + str(player_list[playern].name_id)), font="times 15")
        cardloose_label.pack()
        cardname1 = str(player_list[playern].cards[0])
        card1 = tki.Button(cardloose_select, text=(cardname1), command = lambda: cardloose(cardname1), font="consolas 12")
        card1.pack()
        cardname2 = str(player_list[playern].cards[1])
        card2 = tki.Button(cardloose_select, text=(cardname2), command = lambda: cardloose(cardname2), font="consolas 12")
        card2.pack()
        cardloose_select.mainloop()
        
        player.cartas_reveladas.append(player.cards[carta_a_revelar])
        
    def desafiar(self,player,name, player_list, playern):
            #print("hola soy al que desafiaron",player.name_id,player.cards[0], player.cards[1])
            #print("chao soy el que desafio al men",player2.name_id, player2.cards[0], player2.cards[1])
            
            #PANEL
            desafiar_panel = tki.Tk()
            desafiar_panel.geometry("300x300")
            desafiar_label = tki.Label(desafiar_panel, text="WHO DOUBTS THIS ACTION?", font="Consolas 15")
            desafiar_label.pack()
            def action(action, target, playern):
                print(playern, "PLAYERN EN ACTION DEL DESAFIAR")
                desafiar_panel.destroy()
                player2 = target
                if action == "desafiar_none":
                    print("PASS desafiar")
                    return 0
                elif action == "desafiar_p1":
                    if name in player.cards:
                        # quitar 1 carta al azar a jugador desafiador
                        self.quitar_carta(player2, player_list, playern)
                        # dar nada a jugador i
                    else:
                        # quitar carta alzar a jugador j
                        self.quitar_carta(player, player_list, playern)

                elif action == "desafiar_p2":
                    if name in player.cards:
                        # quitar 1 carta al azar a jugador desafiador
                        self.quitar_carta(player2, player_list, playern)
                        # dar nada a jugador i
                    else:
                        # quitar carta alzar a jugador j
                        self.quitar_carta(player, player_list, playern)

                elif action == "desafiar_p3":
                    if name in player.cards:
                        # quitar 1 carta al azar a jugador desafiador
                        self.quitar_carta(player2, player_list, playern)
                        # dar nada a jugador i
                    else:
                        # quitar carta alzar a jugador j
                        self.quitar_carta(player, player_list, playern)

                elif action == "desafiar_p4":
                    if name in player.cards:
                        # quitar 1 carta al azar a jugador desafiador
                        self.quitar_carta(player2, player_list, playern)
                        # dar nada a jugador i
                    else:
                        # quitar carta alzar a jugador j
                        self.quitar_carta(player, player_list, playern)

                pass
                
            #PLAYER WHO
    
            desafiar_1 = tki.Button(desafiar_panel, text="Player 1", font="consolas 20", command = lambda: action("desafiar_p1", player_list[0], playern))
            desafiar_1.pack()
            desafiar_2 = tki.Button(desafiar_panel, text="Player 2", font="consolas 20", command = lambda: action("desafiar_p2", player_list[1], playern))
            desafiar_2.pack()
            desafiar_3 = tki.Button(desafiar_panel, text="Player 3", font="consolas 20", command = lambda: action("desafiar_p3", player_list[2], playern))
            desafiar_3.pack()
    
            if len(player_list) == 4:
                desafiar_4 = tki.Button(desafiar_panel, text="Player 4", font="consolas 20", command = lambda: action("desafiar_p4", player_list[3], playern))
                desafiar_4.pack()
    
            desafiar_none = tki.Button(desafiar_panel, text =" Pass ", font="consolas 20", command = lambda: action("desafiar_none", player_list[2], playern))
            desafiar_none.pack()
            
            desafiar_panel.mainloop()

    def counteraction(self,player, player_list, playern, name):
        #COUNTER ACTION
        screen_update = Screen_update(player_list)
        ca_panel = tki.Tk()
        ca_panel.title("COUNTER ACTION")
        ca_panel.geometry("300x300")

        def action(action, target, playern, player_list, name):
            if playern == target:
                print("AUTO CONTRACTION BLOCKED")
            else:
                ca_panel.destroy()
                if action == "ca_p1":
                    print("Player 1 DO COUNTERACTION TO ", playern + 1)
                    #preguntar otra vez quien quiere dudarle la carta al que
                    #esta contraatacando, cambialo a botones
                    
                    self.desafiar(player_list[0], name, player_list, playern)
                elif action == "ca_p2":
                    print("Player 2 DO COUNTERACTION TO ", playern + 1)

                    self.desafiar(player_list[1], name, player_list, playern)
                elif action == "ca_p3":
                    print("Player 3 DO COUNTERACTION TO ", playern + 1)

                    self.desafiar(player_list[2], name, player_list, playern)
                elif action == "ca_p4":
                    print("Player 4 DO COUNTERACTION TO ", playern + 1)

                    self.desafiar(player_list[3], name, player_list, playern)
                elif action == "ca_none":
                    if name == "foreingn_aid":
                        print("PASS")
                        player_list[playern].coins += 2
                        screen_update.info()
                    elif name == "duke":
                        print("PASS")
                        player_list[playern].coins += 3
                        screen_update.info()
        #PANEL DE COUNTER ACTION

        ca_label = tki.Label(ca_panel, text="WHO IS COUNTERACTION?", font="Consolas 15")
        ca_label.pack()

        #PLAYER WHO

        ca_1 = tki.Button(ca_panel, text="Player 1", font="consolas 20", command = lambda: action("ca_p1", 0, playern, player_list, name))
        ca_1.pack()
        ca_2 = tki.Button(ca_panel, text="Player 2", font="consolas 20", command = lambda: action("ca_p2", 1, playern, player_list, name))
        ca_2.pack()
        ca_3 = tki.Button(ca_panel, text="Player 3", font="consolas 20", command = lambda: action("ca_p3", 2, playern, player_list, name))
        ca_3.pack()

        if len(player_list) == 4:
            ca_4 = tki.Button(ca_panel, text="Player 4", font="consolas 20", command = lambda: action("ca_p4", 3, playern,player_list, name))
            ca_4.pack()

        ca_none = tki.Button(ca_panel, text =" Pass ", font="consolas 20", command = lambda: action("ca_none", 10, playern,player_list, name))
        ca_none.pack()

        ca_panel.mainloop()

        return True
        return True



    def tax(self,player_list,playern):
        
        dudar = int(input("ingrese el numero del jugador que quiere dudarle, si no quiere nadie dudar"
                          "entonces ingrese '5'\n"))
        print("los jugadores son: ", player_list[playern-1].name_id, player_list[dudar].name_id)
        if player_list[playern-1].name_id == player_list[dudar].name_id:
            print("estas dentro?")
            while player_list[playern-1].name_id == player_list[dudar].name_id:
                dudar = int(input("ingrese el numero del jugador que quiere dudarle, si no quiere nadie dudar"
                                  "entonces ingrese '5'\n"))
        if dudar == 5:
            print("nadie dudo prosigan jugando.")
            player_list[playern-1].coins += 3
        else:
            veredicto = self.desafiar(player_list[playern-1], player_list[dudar],"duke")
            if veredicto == True:
                player_list[playern-1].coins += 3
            else:
                print("la jugada era falsa, la jugada no se seguira.")
    def steal(self,player_list,playern):
        player_steal=int(input(F"{player_list[playern-1].name_id} type de number of the player you want to steal his coins"))
        if player_list[playern - 1].name_id == player_list[player_steal].name_id:
            while player_list[playern - 1].name_id == player_list[player_steal].name_id:
                player_steal = int(
                    input(F"{player_list[playern-1].name_id} type de number of the player you want to steal his coins"))

        dudar = int(input("ingrese el numero del jugador que quiere dudarle, si no quiere nadie dudar"
                          "entonces ingrese '5'\n"))
        if player_list[playern - 1].name_id == player_list[dudar].name_id:
            print("estas dentro?")
            while player_list[playern - 1].name_id == player_list[dudar].name_id:
                dudar = int(input("ingrese el numero del jugador que quiere dudarle, si nadie quiere dudar"
                                  "entonces ingrese '5'\n"))
        if dudar == 5:
            print("nadie dudo prosigan jugando.")
            contraatacar()
            dudar()
            if player_list[player_steal].coins >= 2:
                player_list[playern-1].coins += 2
            else:
                player_list[playern - 1].coins += 1
        else:
            veredicto = self.desafiar(player_list[playern - 1], player_list[dudar], "captain")
            if veredicto == True:
                if player_list[player_steal].coins >= 2:
                    player_list[playern - 1].coins += 2
                else:
                    player_list[playern - 1].coins += 1
            else:
                print("la jugada era falsa, la jugada no se seguira.")




    def assassinte(self,player_list):
        pass
    def exchange(self,player_list):
        pass







    def coup(self, player, player_list):
        screen_update = Screen_update(player_list)
        #MENU COUP
        coup_panel = tki.Tk()
        coup_panel.title("Coup")
        coup_panel.geometry("300x300")

        def coup_target(playern, target):
            print("ATTACKER ",player.name_id , "TARGET ", target)
            if player_list[playern].alive == False: #Verifico si esta vivo
                print("Player attacked is OUT")
                return(0)
            elif player_list[playern].alive == True:
                if target == player.name_id: #verificar autoataque
                    print("Auto Ataque no permitido")
                    return(0)
                elif target != player.name_id:
                    coup_panel.destroy()
                    
                    player_list[playern].influence -=1
                    print(player_list[playern].influence, " INFLUENCIA DEL ATACADO ")
                    #Check if card 1 or 2 is losed
                    
                    self.quitar_carta(player, player_list, playern)


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
