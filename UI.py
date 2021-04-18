import tkinter as tki 
from player import *
class UI:
    def __init__(self):
        self.default = 0
    def Interface(self):
        main_panel = tki.Tk()
        main_panel.title("CUOP v0.0.1")
        main_panel.geometry("500x500")
        
        def action(action):
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
            
        def counteraction(counteraction):
            return 0;
        
        def playerpanel():
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

            buttom_income.grid(row = 2, column = 0, padx = 20)
            buttom_foreingn_aid.grid(row = 2, column = 1, padx = 20)
            buttom_coup.grid(row = 2, column = 2, padx = 20)
            
            #card options

        #Stuff
        tilecoup = tki.Label(main_panel, text="COUP", font=("Times", 40, "bold"), bg="grey", fg="white")
        tilecoup.pack()
        nextturn = tki.Button(main_panel, text="Next Turn", font="consolas 20", command = playerpanel) 
        nextturn.pack()
        
        main_panel.mainloop()

screen_main = UI()
screen_main.Interface()
