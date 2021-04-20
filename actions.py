from player import Player
import tkinter as tki 
class Actions:
    def foreingn_aid(self,player_list,playern):



        player_list[playern].coins += 2
        return True
    """
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
        """ 
        
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
           
    def golpe(): #SI EL JUGADOR TIENE 10 MONEDAS DEBE REALIZAR ESTA EJECUCION SI O SI
        return 0 
