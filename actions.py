from player import *
from screen_update import *
import tkinter as tki
class Actions:
    def __init__(self):
        pass
    def foreingn_aid(self, player_list,playern):
        #COUNTER ACTION
        screen_update = Screen_update(player_list)
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
                    dudar=int(input("ingrese el numero del jugador que quiere dudarle"))
                    self.desafiar(player_list[0],player_list[dudar-1])
                elif action == "ca_p2":
                    print("Player 2 DO COUNTERACTION TO ", playern + 1)
                    dudar = int(input("ingrese el numero del jugador que quiere dudarle"))
                    self.desafiar(player_list[1], player_list[dudar-1])
                elif action == "ca_p3":
                    print("Player 3 DO COUNTERACTION TO ", playern + 1)
                    dudar = int(input("ingrese el numero del jugador que quiere dudarle"))
                    self.desafiar(player_list[2], player_list[dudar-1])
                elif action == "ca_p4":
                    print("Player 4 DO COUNTERACTION TO ", playern + 1)
                    dudar = int(input("ingrese el numero del jugador que quiere dudarle"))
                    self.desafiar(player_list[3], player_list[dudar-1])
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

        return True

    #funcion que evalua el desafio y a quien quitar carta, la llamo en contraataque
    #tienes que juntar tu lista hidden con las cartas reveladas aqui
    def quitar_carta(self,player):
        carta_a_revelar = int(input(F"{player.name_id} tus cartas son " + player.cards[0] + " y " + player.cards[1] + " 0 para matar la primera y 1 para la segunda"))
        player.cartas_reveladas.append(player.cards[carta_a_revelar])
    def desafiar(self,player,player2):
            print("hola soy al que desafiaron",player.name_id,player.cards[0], player.cards[1])
            print("chao soy el que desafio al men",player2.name_id, player2.cards[0], player2.cards[1])
            if "duke" in player.cards:
                # quitar 1 carta al azar a jugador desafiador
                self.quitar_carta(player2)
                # dar nada a jugador i
            else:
                # quitar carta alzar a jugador j
                self.quitar_carta(player)



    def tax(self,player_list):
        pass
    def steal(self,player_list):
        pass
    def assassinte(self,player_list):
        pass
    def exchange(self,player_list):
        pass







    def coup(player, player_list):
        if player.coins < 7:
            print("INSUFICIENTES FONDOS")
            Actions.coup(player, player_list) #repetir WARNIRNG CON ESTA FUNCION PERO FUNCIONA :D
            return False
        elif player.coins >= 7:
            player.coins -= 7
            #MENU COUP
            coup_panel = tki.Tk()
            coup_panel.title("Coup")
            coup_panel.geometry("300x300")

            def coup_target(player_n):
                print("ATTACKER ",player.name_id , "TARGET ", player_n)
                if player_list[player_n-1].alive == False: #Verifico si esta vivo
                    print("Player attacked is OUT")
                    return(0)
                elif player_list[player_n-1].alive == True:
                    if player_n == player.name_id: #verificar autoataque
                        print("Auto Ataque no permitido")
                        return(0)
                    elif player_n != player.name_id -1:
                        coup_panel.destroy()
                        print(player_list[player_n-1].influence, " INFLUENCIA DEL ATACADO ")
                        player_list[player_n-1].influence -=1
                        #Check if card 1 or 2 is losed

                        if player_list[player_n-1].cards[0] == "Card losed":
                            player_list[player_n-1].cards[1] == "Card losed"
                        else:
                            player_list[player_n-1].cards[0] = "Card losed"


                return 0

            coup_title = tki.Label(coup_panel, text="Who to Coup?", font=("Times", 35, "bold italic"), bg="grey", fg="white")
            coup_title.pack()
            coup_1 = tki.Button(coup_panel, text="coup Player 1", font="consolas 20", command = lambda: coup_target(1))
            coup_1.pack()
            coup_2 = tki.Button(coup_panel, text="coup Player 2", font="consolas 20", command = lambda: coup_target(2))
            coup_2.pack()
            coup_3 = tki.Button(coup_panel, text="coup Player 3", font="consolas 20", command = lambda: coup_target(3))
            coup_3.pack()
            if len(player_list) == 4:
                coup_4 = tki.Button(coup_panel, text="coup Player 4", font="consolas 20", command = lambda: coup_target(4))
                coup_4.pack()
            coup_panel.mainloop()
            return True


    def coup(player, player_list):
        if player.coins < 7:
            print("INSUFICIENTES FONDOS")
            Actions.coup(player, player_list)
            return False
        elif player.coins >= 7:
            player.coins -= 7

            #MENU COUP
            coup_panel = tki.Tk()
            coup_panel.title("Coup")
            coup_panel.geometry("300x300")
            def coup_target(player_n):
                coup_panel.destroy()
                print("ATTACKER ",player.name_id , "TARGET ", player_n) #ESTO HACE NADA ACTUALMENTE


            coup_title = tki.Label(coup_panel, text="Who to Coup?", font=("Times", 35, "bold italic"), bg="grey", fg="white")
            coup_title.pack()
            coup_1 = tki.Button(coup_panel, text="coup Player 1", font="consolas 20", command = lambda: coup_target(1))
            coup_1.pack()
            coup_2 = tki.Button(coup_panel, text="coup Player 2", font="consolas 20", command = lambda: coup_target(2))
            coup_2.pack()
            coup_3 = tki.Button(coup_panel, text="coup Player 3", font="consolas 20", command = lambda: coup_target(3))
            coup_3.pack()
            if len(player_list) == 4:
                coup_4 = tki.Button(coup_panel, text="coup Player 4", font="consolas 20", command = lambda: coup_target(4))
                coup_4.pack()
            coup_panel.mainloop()

    #def golpe(): #SI EL JUGADOR TIENE 10 MONEDAS DEBE REALIZAR ESTA EJECUCION SI O SI
     #   return 0
