import tkinter as tki 
from screen_update import *
from player import *
class starup:
    def __init__(self, many_players):
        self.many_players = many_players
    
class startmenu:
    def __init__(self):
        self.default = 0
    def start(self, start_info):
        global many_players
        many_players = 1
        panel_menu = tki.Tk()
        panel_menu.title("CUOP Start")
        panel_menu.geometry("500x300")
        def player_selection(nplayers):
            panel_menu.destroy()
            if nplayers == 3:
                print("3 player mode selected")
                many_players = 3
                start_info.players = 3
                return many_players
            elif nplayers == 4:
                print("4 player mode selected")
                many_players = 4
                start_info.players = 4
                return many_players    
        #Menu Text
        tilecoup = tki.Label(panel_menu, text="COUP", font=("Times", 40, "bold"), bg="grey", fg="white")
        tilecoup.pack()
        question = tki.Label(panel_menu, text="How many players?", font=("Times", 20, "italic"), bg="grey", fg="white")
        question.pack()
        players3 = tki.Button(panel_menu, text="3 players", font="consolas 20", command = lambda: player_selection(3))
        players3.pack()
        players4 = tki.Button(panel_menu, text="4 players", font="consolas 20", command = lambda: player_selection(4))
        players4.pack()
        exit_all = tki.Button(panel_menu, text="Exit", command=panel_menu.destroy)
        exit_all.pack()
        panel_menu.mainloop()
        
        panel_menu = tki.Tk()
        panel_menu.title("CUOP Start")
        panel_menu.geometry("350x150")
        question = tki.Label(panel_menu, text="Now player cards will show \n starting from player 1", font=("Arial", 20, "italic"), bg="white", fg="black")
        question.pack()
        nextpage = tki.Button(panel_menu, text="Show cards", font="consolas 18", command = panel_menu.destroy)
        nextpage.pack()
        panel_menu.mainloop()