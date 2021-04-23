from player import *
from screen_update import *
import tkinter as tki
class Actions:
    def __init__(self):
        
        pass
    def foreingn_aid(self, player_list,playern):
        print(playern, "PLAYERN EN forngein esa wea---------------------")
        
        screen_update = Screen_update(player_list)
        self.counteraction(player_list[playern], player_list, playern,"foreingn_aid")
        return True

    #funcion que evalua el desafio y a quien quitar carta, la llamo en contraataque
    #tienes que juntar tu lista hidden con las cartas reveladas aqui
    def quitar_carta(self,player, player_list, playern, name):
        #print(playern, "PLAYERN EN QUITAR CARTA---------------------")
        #print(player.name_id ,"Jugador daaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        print(name, "= duke")
        
        screen_update = Screen_update(player_list)
        cardloose_select = tki.Tk()
        cardloose_select.title("Coup")
        cardloose_select.geometry("300x200")

        def cardloose(card, player, player_list, name): #VER BIEN PARA VER CUALES SI ESTAN PERDIDAS, ACTUALMENTE SOLO ESTAN EN player.show[] -----------------------------------
            cardloose_select.destroy()
            #print(name, "NAMWEEERWEIWEEUIKUIEI92381890123128932183091========================")
            if name == "duke" or name == "coup" or name == "foreingn_aid" or name == "assassin" :
                print(player.name_id ,"Jugador decente por facasdsah jkdasjkgdfjkasjf jsatjkftg sa")
                #Lose card 0
                if card == player.cards[0]:
                    player.show[0] = player.cards[0]  #Reemplazo el show
                    player.cards[0] = " "
                #Lose card 1
                elif card == player.cards[1]: 
                    player.show[1] = player.cards[1] #Reemplazo el show
                    player.cards[1] = " "
                    
            elif name == "captain":
                print(player.name_id ,"Jugador CAPTAAAAAAAAAAAAAAAAAAAAAAAAAAIN LOOOOOOOOOOOOOOOOOOOOK")
                if card == player.cards[0]:
                    player.show[0] = player.cards[0]  #Reemplazo el show
                    player.cards[0] = " "
                    
                    if player.coins == 1:
                        player.coins -= 1
                        player_list[playern].coins += 1
                    else:
                        player.coins -= 2
                        player_list[playern].coins += 2
                #Lose card 1
                elif card == player.cards[1]: 
                    player.show[1] = player.cards[1] #Reemplazo el show
                    player.cards[1] = " "
                    if player.coins == 1:
                        player.coins -= 1
                        player_list[playern].coins += 1
                    else:
                        player.coins -= 2
                        player_list[playern].coins += 2
            screen_update.info()
        
        cardloose_label = tki.Label(cardloose_select, text=("Select card to lose " + str(player_list[playern].name_id)), font="times 15")
        cardloose_label.pack()
        cardname1 = str(player_list[playern].cards[0])
        card1 = tki.Button(cardloose_select, text=(cardname1), command = lambda: cardloose(cardname1, player, player_list, name), font="consolas 12")
        card1.pack()
        cardname2 = str(player_list[playern].cards[1])
        card2 = tki.Button(cardloose_select, text=(cardname2), command = lambda: cardloose(cardname1, player, player_list, name), font="consolas 12")
        card2.pack()
        cardloose_select.mainloop()
        
        player.cartas_reveladas.append(player.cards[carta_a_revelar])
        
    def desafiar(self,player, player_list, playern, name): #player ES EL QUE DESAFIO AL player_list[playern]
            print(playern, "PLAYERN EN DESAFIAR---------------------")
            #print("hola soy al que desafiaron",player.name_id,player.cards[0], player.cards[1])
            #print("chao soy el que desafio al men",player2.name_id, player2.cards[0], player2.cards[1])
            
            #PANEL
            desafiar_panel = tki.Tk()
            desafiar_panel.geometry("300x300")
            desafiar_label = tki.Label(desafiar_panel, text="WHO DOUBTS THIS ACTION?", font="Consolas 15")
            desafiar_label.pack()
            def action(action, player, playern):
                print(playern, "PLAYERN EN ACTION DEL DESAFIAR")
                desafiar_panel.destroy()
                if action == "desafiar_none":
                    if name == "duke":
                        player_list[playern].coins +=3
                    elif name == "captain":
                        if player.coins == 1:
                            player.coins -= 1
                            player_list[playern].coins += 1
                        else:
                            player.coins -= 2
                            player_list[playern].coins += 2
                    elif name == "assassin":
                        player.coins -= 3 
                        self.quitar_carta(player, player_list, playern, name)
                    print("PASS desafiar")
                    return 0
                elif action == "desafiar_p1":
                    if name in player.cards:

                        # quitar 1 carta al azar a jugador desafiador
                        self.quitar_carta(player, player_list, playern, name)
                        # dar nada a jugador i
                    else:
                        # quitar carta alzar a jugador j
                        self.quitar_carta(player, player_list, playern, name)

                elif action == "desafiar_p2":
                    if name in player.cards:

                        # quitar 1 carta al azar a jugador desafiador
                        self.quitar_carta(player, player_list, playern, name)
                        # dar nada a jugador i
                    else:
                        # quitar carta alzar a jugador j
                        self.quitar_carta(player, player_list, playern, name)

                elif action == "desafiar_p3":
                    if name in player.cards:

                        # quitar 1 carta al azar a jugador desafiador
                        self.quitar_carta(player, player_list, playern, name)
                        # dar nada a jugador i
                    else:
                        # quitar carta alzar a jugador j
                        self.quitar_carta(player, player_list, playern, name)

                elif action == "desafiar_p4":
                    if name in player.cards:

                        # quitar 1 carta al azar a jugador desafiador
                        self.quitar_carta(player, player_list, playern, name)
                        # dar nada a jugador i
                    else:
                        # quitar carta alzar a jugador j
                        self.quitar_carta(player, player_list, playern, name)
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

    def counteraction(self, player, player_list, playern, name):
        print(playern, "PLAYERN EN COUNTERACTION---------------------")
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
                    
                    self.desafiar(player_list[0], player_list, playern, name)
                elif action == "ca_p2":
                    print("Player 2 DO COUNTERACTION TO ", playern + 1)

                    self.desafiar(player_list[1], player_list, playern, name)
                elif action == "ca_p3":
                    print("Player 3 DO COUNTERACTION TO ", playern + 1)

                    self.desafiar(player_list[2], player_list, playern, name)
                elif action == "ca_p4":
                    print("Player 4 DO COUNTERACTION TO ", playern + 1)

                    self.desafiar(player_list[3], player_list, playern, name)
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



    def tax(self, player_list, playern):
        screen_update = Screen_update(player_list)
        self.desafiar(player_list[playern], player_list, playern,"duke")
        
        
    def steal(self,player, player_list, playern, name):
        print(playern, "PLAYERN EN STEAL --------------------------------------------------")
        
        screen_update = Screen_update(player_list)
        steal_panel = tki.Tk()
        steal_panel.title("STEAL")
        steal_panel.geometry("320x300")
        
        
        def action(action, target, playern, player_list, name):
            if playern == target:
                print("AUTO STEAL BLOCKED")
            else:
                steal_panel.destroy()
                if action == "steal_p1":
                    print("Player ", playern + 1, " STEAL TO Player 1", )
                    #preguntar otra vez quien quiere dudarle la carta al que
                    #esta contraatacando, cambialo a botones
                    
                    self.desafiar(player_list[0], player_list, playern, name)
                elif action == "steal_p2":
                    print("Player ", playern + 1, " STEAL TO Player 2", )
                    
                    self.desafiar(player_list[1], player_list, playern, name)
                elif action == "steal_p3":
                    print("Player ", playern + 1, " STEAL TO Player 3", )

                    self.desafiar(player_list[2], player_list, playern, name)
                elif action == "steal_p4":
                    print("Player ", playern + 1, " STEAL TO Player 4", )

                    self.desafiar(player_list[3], player_list, playern, name)
    
                    
        #PANEL DE COUNTER ACTION

        steal_label = tki.Label(steal_panel, text="WHO are going to steal from?", font="Consolas 15")
        steal_label.pack()

        #PLAYER WHO

        steal_1 = tki.Button(steal_panel, text="Player 1", font="consolas 20", command = lambda: action("steal_p1", 0, playern, player_list, name))
        steal_1.pack()
        steal_2 = tki.Button(steal_panel, text="Player 2", font="consolas 20", command = lambda: action("steal_p2", 1, playern, player_list, name))
        steal_2.pack()
        steal_3 = tki.Button(steal_panel, text="Player 3", font="consolas 20", command = lambda: action("steal_p3", 2, playern, player_list, name))
        steal_3.pack()

        if len(player_list) == 4:
            steal_4 = tki.Button(steal_panel, text="Player 4", font="consolas 20", command = lambda: action("steal_p4", 3, playern,player_list, name))
            steal_4.pack()


        steal_panel.mainloop()

        return True
        

    def assassinate(self,player, player_list, playern, name):
        print(playern, "PLAYERN EN ASSASIN --------------------------------------------------")
        
        screen_update = Screen_update(player_list)
        kill_panel = tki.Tk()
        kill_panel.title("kill")
        kill_panel.geometry("320x300")
        
        
        def action(action, target, playern, player_list, name):
            if playern == target:
                print("AUTO kill BLOCKED")
            else:
                kill_panel.destroy()
                if action == "kill_p1":
                    print("Player ", playern + 1, " kill TO Player 1", )
                    #preguntar otra vez quien quiere dudarle la carta al que
                    #esta contraatacando, cambialo a botones
                    
                    player.coins -= 3 
                    self.quitar_carta(player_list[0], player_list, playern, name)
            
                elif action == "kill_p2":
                    print("Player ", playern + 1, " kill TO Player 2", )
                    
                    player.coins -= 3 
                    self.quitar_carta(player_list[1], player_list, playern, name)
                    
                elif action == "kill_p3":
                    print("Player ", playern + 1, " kill TO Player 3", )
                    
                    player.coins -= 3 
                    self.quitar_carta(player_list[2], player_list, playern, name)
                    
                elif action == "kill_p4":
                    print("Player ", playern + 1, " kill TO Player 4", )
                    
                    player.coins -= 3 
                    self.quitar_carta(player_list[3], player_list, playern, name)
                    
    
                    
        #PANEL DE COUNTER ACTION

        kill_label = tki.Label(kill_panel, text="WHO are going to assassinate?", font="Consolas 15")
        kill_label.pack()

        #PLAYER WHO

        kill_1 = tki.Button(kill_panel, text="Player 1", font="consolas 20", command = lambda: action("kill_p1", 0, playern, player_list, name))
        kill_1.pack()
        kill_2 = tki.Button(kill_panel, text="Player 2", font="consolas 20", command = lambda: action("kill_p2", 1, playern, player_list, name))
        kill_2.pack()
        kill_3 = tki.Button(kill_panel, text="Player 3", font="consolas 20", command = lambda: action("kill_p3", 2, playern, player_list, name))
        kill_3.pack()

        if len(player_list) == 4:
            kill_4 = tki.Button(kill_panel, text="Player 4", font="consolas 20", command = lambda: action("kill_p4", 3, playern,player_list, name))
            kill_4.pack()


        kill_panel.mainloop()

        return True

    def exchange(self,player_list):
        pass






    #playern es como privado aqui no se xxd payday alli voy
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
                    self.quitar_carta(player_list[playern], player_list, playern, "coup")


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
