import tkinter as tki 
from player import *
from cartas import *
class UI:
    def __init__(self, many_players, playern):
        self.default = 0
        self.__many_players = many_players
        self.playern = playern 
    def Interface(self, playern):
        main_panel = tki.Tk()
        main_panel.title("CUOP v0.0.2")
        main_panel.geometry("500x500")
        
        def next_loop(many_players, playern):
            if many_players == 3:
                if playern == 3:
                    playern = 1
                    return playern
                else:
                    return playern
            if many_players == 4:
                if playern == 4:
                    playern = 1        
                    return playern
        def next_player(many_players, playern):
            N_plabel = tki.Label(main_panel, font="consolas 10", bg="white", fg="black")
            if self.__many_players == 3:
                if playern == 0:
                    N_plabel.config(text = "Player 1 is your turn")
                    N_plabel.pack()
                    playern = 1
                elif playern == 1:
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
                return playern, self.__many_players
            
            elif self.__many_players == 4:
                if playern == 0:
                    N_plabel.config(text = "Player 1 is your turn")
                    N_plabel.pack()
                elif playern == 1:
                    N_plabel.config(text = "Player 2 is your turn")
                    N_plabel.pack()
                elif playern == 2:
                    N_plabel.config(text = "Player 3 is your turn")
                    N_plabel.pack()
                elif playern == 3:
                    N_plabel.config(text = "Player 4 is your turn")
                    N_plabel.pack()
                elif playern == 4:
                    N_plabel.config(text = "Player 1 is your turn")
                    N_plabel.pack()
                return playern, self.__many_players
        def action(action, playern):
            player_panel.destroy() #This deletes the window after an action is choose
            #actions
            if action == "income":
                print("Player do: income")
                
                #playern = next_loop(many_players, playern)
                
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
            
            
        def counteraction(counteraction):
            return 0;
        
        def playerpanel(playern):
            global player_panel
            player_panel = tki.Toplevel(main_panel)
            player_panel.title("PLAYER")
          
            player_label = tki.Label(player_panel, text="CHOSE AN ACTION", font="times 20")
            player_label.grid(row = 0, column = 1)
            
            #actions options
            buttom_income = tki.Button(player_panel, text = " Income ", width = 5, height = 1, font = "consolas 10", bg = "grey", fg = "white", command = lambda: action("income", playern))
            buttom_income.config(padx=10)
            buttom_foreingn_aid = tki.Button(player_panel, text = " Foreingn Aid ", width = 5, height = 1, font = "consolas 10", bg = "grey", fg = "white", command = lambda: action("foreingn_aid", playern))
            buttom_foreingn_aid.config(padx=22)
            buttom_coup = tki.Button(player_panel, text = " Coup ", width = 5, height = 1, font = "consolas 10", bg = "grey", fg = "white", command = lambda: action("coup", playern))
            buttom_coup.config(padx=10)

            buttom_income.grid(row = 2, column = 0, padx = 20)
            buttom_foreingn_aid.grid(row = 2, column = 1, padx = 20)
            buttom_coup.grid(row = 2, column = 2, padx = 20)
            
            #card options
            
        #Stuff
        tilecoup = tki.Label(main_panel, text="COUP", font=("Times", 40, "bold"), bg="grey", fg="white")
        tilecoup.pack()
        
        global N_plabel
        N_plabel = tki.Label(main_panel, font="consolas 10", bg="white", fg="black")
        N_plabel.config(text = "Player 1 is your turn")
        N_plabel.pack()

        nextturn = tki.Button(main_panel, text="Next Turn", font="consolas 20", command = lambda: playerpanel(playern)) 
        nextturn.pack()
        
        main_panel.mainloop()


#screen_main = UI()
#screen_main.Interface(1)
