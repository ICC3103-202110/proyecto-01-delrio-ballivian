import tkinter as tki 
from player import *

class starup:
    def __init__(self, many_players):
        self.many_players = many_players
    
class startmenu:
    def __init__(self):
        self.default = 0
    def start(self):
        
        global many_players
        many_players = 1
        menu_panel = tki.Tk()
        menu_panel.title("CUOP v0.1.0")
        menu_panel.geometry("500x300")
        def player_selection(nplayers):
            menu_panel.destroy()
            if nplayers == 3:
                print("3 player mode selected")
                many_players = 3
                return many_players
            elif nplayers == 4:
                print("4 player mode selected")
                many_players = 4
                return many_players    
        #Menu Text
        tilecoup = tki.Label(menu_panel, text="COUP", font=("Times", 40, "bold"), bg="grey", fg="white")
        tilecoup.pack()
        question = tki.Label(menu_panel, text="How many players?", font=("Times", 20, "italic"), bg="grey", fg="white")
        question.pack()
        players3 = tki.Button(menu_panel, text="3 players", font="consolas 20", command = lambda: player_selection(3)) 
        players3.pack()
        players4 = tki.Button(menu_panel, text="4 players", font="consolas 20", command = lambda: player_selection(4))
        players4.pack()
        exit_all = tki.Button(menu_panel, text="Exit", command=menu_panel.destroy)
        exit_all.pack()
        menu_panel.mainloop()
        
        return 3 #ARREGLAR ESTE RETURN