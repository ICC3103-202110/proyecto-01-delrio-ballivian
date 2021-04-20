import tkinter as tki 
from player import *
from cartas import *
class UI:
    def __init__(self, many_players):
        self.default = 0
        self.__many_players = many_players
    def Interface(self):
        global playern 
        playern = 1
        main_panel = tki.Tk()
        main_panel.title("CUOP v0.0.2")
        main_panel.geometry("500x500")
        
        def next_player(many_players, playern):
            if many_players == 3:
                if playern == 1:
                    N_plabel.config(text = "Player 2 is your turn")
                    N_plabel.pack()
                    playern = 2
                elif playern == 2:
                    N_plabel.config(text = "Player 3 is your turn")
                    N_plabel.pack()
                    playern = 3
                elif playern == 3:
                    N_plabel.config(text = "Player 1 is your turn")
                    N_plabel.pack()
                    playern = 1
            elif many_players == 4:
                if playern == 1:
                    N_plabel.config(text = "Player 2 is your turn")
                    N_plabel.pack()
                    playern = 2
                elif playern == 2:
                    N_plabel.config(text = "Player 3 is your turn")
                    N_plabel.pack()
                    playern = 3
                elif playern == 3:
                    N_plabel.config(text = "Player 1 is your turn")
                    N_plabel.pack()
                    playern = 4
                elif playern == 4:
                    N_plabel.config(text = "Player 1 is your turn")
                    N_plabel.pack()
                    playern = 1
            print(playern, "NEXT PLAYER after")
            return playern
            
        def action(action): 
            global playern #Este es el return practicamente
            #si puede probocar memory leak pero solo para esta variable no deberia haber problema
            
            player_panel.destroy() #This deletes the window after an action is choose
            #actions
            if action == "income":
                print("Player do: income")
            elif action == "foreingn_aid":
                print("Player do: foreingn_aid")
            elif action == "coup":
                print("Player do: coup")
                
            #Cartas
            elif action == "tax":
                print("Player do: tax")
            elif action == "assassinate":
                print("Player do: assassinate")
            elif action == "exchange":
                print("Player do: exchange")
            elif action == "steal":
                print("Player do: steal")
                
            print(playern, "PLAYERN BEFORE")
            playern = next_player(self.__many_players, playern)
            print(playern, "PLAYERN AFTER")
                
            
            #return playern #No hay forma de retornar en los botones solo con globales
        
        def counteraction(counteraction):
            return 0
        
        def playerpanel(playern):

            global player_panel
            player_panel = tki.Toplevel(main_panel)
            player_panel.title("PLAYER")
          
            player_label = tki.Label(player_panel, text="CHOSE AN ACTION", font="times 20")
            player_label.grid(row = 0, column = 1)
            
            #actions options
            buttom_income = tki.Button(player_panel, text = " Income ", width = 5, height = 1, font = "consolas 10", bg = "grey", fg = "white", command = lambda: action("income"))
            buttom_income.config(padx=10)
            buttom_foreingn_aid = tki.Button(player_panel, text = " Foreingn Aid ", width = 5, height = 1, font = "consolas 10", bg = "grey", fg = "white", command = lambda: action("foreingn_aid"))
            buttom_foreingn_aid.config(padx=22)
            buttom_coup = tki.Button(player_panel, text = " Coup ", width = 5, height = 1, font = "consolas 10", bg = "grey", fg = "white", command = lambda: action("coup"))
            buttom_coup.config(padx=10)
            
            #Posicionar
            buttom_income.grid(row = 2, column = 0, padx = 20)
            buttom_foreingn_aid.grid(row = 2, column = 1, padx = 20)
            buttom_coup.grid(row = 2, column = 2, padx = 20)
            
            #card options
            
        #Stuff
        tilecoup = tki.Label(main_panel, text="COUP", font=("Times", 40, "bold"), bg="grey", fg="white")
        tilecoup.pack()
        
        global N_plabel #Para poder hacerle .config en cualquier funcion
        N_plabel = tki.Label(main_panel, font="consolas 10", bg="white", fg="black")
        N_plabel.config(text = "Player 1 is your turn")
        N_plabel.pack()

        nextturn = tki.Button(main_panel, text="Next Turn", font="consolas 20", command = lambda: playerpanel(playern)) 
        nextturn.pack()
        
        main_panel.mainloop() #El programa se ejecuta hasta aqui y se queda en este "Loop"


#screen_main = UI()
#screen_main.Interface(1)
