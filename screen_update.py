import tkinter as tki
from player import *

class Screen_update:
    def __init__(self, player_list):
        self.player_list = player_list
    def info(self):
        def close():
            info_panel.destroy()
            
        info_panel = tki.Tk()
        info_panel.title("Player info")
        #info_panel.geometry("250x500")
        
        #INICIALIZAR LA INFO DE LOS JUGADORES
        info_1 = str("PLAYER 1: \nCoins: " + str(self.player_list[0].coins) + " \nCards: " + self.player_list[0].show[0] + " " + self.player_list[0].show[1] + "\n")
        info_player_1 = tki.Label(info_panel, text=(info_1), font="times 15")
        info_player_1.pack()
    
        info_2 = str("PLAYER 2: \nCoins: " + str(self.player_list[1].coins) + " \nCards: " + self.player_list[1].show[0] + " " + self.player_list[1].show[1]+ "\n")
        info_player_2 = tki.Label(info_panel, text=(info_2), font="times 15")
        info_player_2.pack()
    
        info_3 = str("PLAYER 3: \nCoins: " + str(self.player_list[2].coins) + " \nCards: " + self.player_list[2].show[0] + " " + self.player_list[2].show[1]+ "\n")
        info_player_3 = tki.Label(info_panel, text=(info_3), font="times 15")
        info_player_3.pack()
    
        if len(self.player_list) == 4:
            info_4 = str("PLAYER 4: \nCoins: " + str(self.player_list[3].coins) + " \nCards: " + self.player_list[3].show[0] + " " + self.player_list[3].show[1]+ "\n")
            info_player_4 = tki.Label(info_panel, text=(info_4), font="times 15")
            info_player_4.pack()
        close = tki.Button(info_panel, text="Close", command=close, font="consolas 10")
        close.pack(padx=20, pady=20)
        info_panel.mainloop()
    
    