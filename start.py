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
        menu_panel = tki.Tk()
        menu_panel.title("CUOP Start")
        menu_panel.geometry("500x300")
        def player_selection(nplayers):
            menu_panel.destroy()
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
        
        menu_panel = tki.Tk()
        menu_panel.title("CUOP Start")
        menu_panel.geometry("350x150")
        question = tki.Label(menu_panel, text="Now player cards will show \n starting from player 1", font=("Arial", 20, "italic"), bg="white", fg="black")
        question.pack()
        nextpage = tki.Button(menu_panel, text="Show cards", font="consolas 18", command = menu_panel.destroy) 
        nextpage.pack()
        menu_panel.mainloop()