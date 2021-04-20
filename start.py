import tkinter as tki 
from UI import * 

class startmenu:
    def __init__(self):
        self.default = 0
    def start(self):
        menu_panel = tki.Tk()
        menu_panel.title("CUOP v0.0.2")
        menu_panel.geometry("500x300")
        def player_selection(nplayers):
            menu_panel.destroy()
            if nplayers == 3:
                print("3 player mode selected")
                main_panel = UI(3)
                main_panel.Interface()
            elif nplayers == 4:
                print("4 player mode selected")
                main_panel = UI(4)
                main_panel.Interface()
        #Menu Text
        tilecoup = tki.Label(menu_panel, text="COUP", font=("Times", 40, "bold"), bg="grey", fg="white")
        tilecoup.pack()
        question = tki.Label(menu_panel, text="How many players?", font=("Times", 20, "italic"), bg="grey", fg="white")
        question.pack()
        players3 = tki.Button(menu_panel, text="3 players", font="consolas 20", command = lambda: player_selection(3)) 
        players3.pack()
        players4 = tki.Button(menu_panel, text="4 players", font="consolas 20", command = lambda: player_selection(4))
        players4.pack()
        menu_panel.mainloop()
