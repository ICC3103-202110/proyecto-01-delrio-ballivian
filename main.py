
from actions import *
from player import *
from cards import *
from screen_update import *
from start import *
import tkinter as tki


# play order:
#  1. Choose an action to play or bluff
#  2. Announce to everyone the play
#  3. Allow other players to block move
#  3.a. Allow active player to call bluff
#  3.b. Challenge Check
#  4. Allow other players to challenge move
#  5. Play card's effect if no challenge or blocking fails

#  Challenge Check:
#    1. If challenge succeeds, kill the player's one card
#    2. Check if player is dead
#    3. If challenge fails, kill challenger's one card
#    4. Check if player is dead

def main():
    #StartUP
    start_info = startinfo(0)
    start_menu = startmenu()
    start_menu.start(start_info)
    many_players = start_info.players
    
    #Action Creation
    obj_actions=Actions()
    
    #deck creations
    if many_players == 3:
        Mazo = Cards()
        player_list=[]
        #Player creation
        for i in range(many_players):
            player_list.append(Player("jugador " + str(i+1), i))
            #dos_cartas = [Cards.give_cards(player_list[i], Mazo)]
            player_list[i].cards = Mazo.give_cards(player_list[i])
            print(player_list[i].cards[0],player_list[i].cards[1])



    elif many_players == 4:
        Mazo = Cards()
        player_list=[]
        #Player creation
        for i in range(many_players):
            player_list.append(Player("jugador " + str(i+1), i))
            #dos_cartas = [Cards.give_cards(player_list[i], Mazo)]
            player_list[i].cards = Mazo.give_cards(player_list[i])
            print(player_list[i].cards[0],player_list[i].cards[1])

    #Start infobox
    screen_update = Screen_update(player_list)
    
    #VER TODAS LAS CARTAS
    for i in range(len(player_list)):
            print(player_list[i].cards, "cartas jugador ", player_list[i].name_id)
    
    #Show players cards
    def show_cards(player_list, player_n):
        show = tki.Tk()
        show.geometry("300x200")
        def nextplayer():
            show.destroy()
            pass
        
        your_cards = str("Player " + str(player_n) + "\nYour cards:\n" + str(player_list[player_n-1].cards[0]) + " / " + str(player_list[player_n-1].cards[1]))
        cards_show = tki.Label(show, text=(your_cards), font="times 20")
        cards_show.pack()
        buttom_next = tki.Button(show, text="Show next player", command = nextplayer, font="consolas 15")
        buttom_next.pack()
        
        show.mainloop()
    
    show_cards(player_list, 1)
    show_cards(player_list, 2)
    show_cards(player_list, 3)
    if many_players == 4:
        show_cards(player_list, 4)
    
    #Panel Creation
    global playern
    playern = 1
    main_panel = tki.Tk()
    main_panel.title("CUOP v0.4.2")
    main_panel.geometry("500x200")



    #Esta la puedo meter en una Class!!
    def next_player(many_players, playern): #funcion para loopear para saber los turnos una vez que llegan al ultimo jugador
        if many_players == 3:
            print(playern,"esto es playern")

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
        elif many_players == 4: #Modo para 4 jugadores RECUERDA CAMBIARLO CON LO DE ARRIBA
            if playern == 1:
                N_plabel.config(text = "Player 2 is your turn")
                N_plabel.pack()
                playern = 2
            elif playern == 2:
                N_plabel.config(text = "Player 3 is your turn")
                N_plabel.pack()
                playern = 3
            elif playern == 3:
                N_plabel.config(text = "Player 4 is your turn")
                N_plabel.pack()
                playern = 4
            elif playern == 4:
                N_plabel.config(text = "Player 1 is your turn")
                N_plabel.pack()
                playern = 1

        return playern



    #Aqui es donde el jugador realiza las acciones
    def action(action):
               
        global playern #Este es el return practicamente
        player_panel.destroy() #This deletes the window after an action is choose
       
        
        #actions
        if action == "income":
            player_list[playern-1].coins +=1
            print("Player", playern, " do: income")
            playern = next_player(many_players, playern)
            screen_update.info()
            
        elif action == "foreingn_aid":
            print("Player", playern, " do: foreingn_aid")

            playern = next_player(many_players, playern)
            obj_actions.foreingn_aid(player_list ,playern-2)

        elif action == "coup":
            print("Player", playern, " do: coup")
            if player_list[playern-1].coins < 7: #Verificar que tenga las monedas suficientes
                print("INSUFICIENTES FONDOS")
                playerpanel(playern)
                return 0
            elif player_list[playern-1].coins >= 7:
                player_list[playern-1].coins -= 7
                playern = next_player(many_players, playern) #Lo tengo que ejecutar ya que la funcion de Cuop deja de ejecutar lo que tenga abajo
                obj_actions.coup(player_list[playern-2], player_list) #AQUI VA UN -2 DE MANERA QUE PUEDA EJECUTAR EL next_player Tras hacer un Coup

        #Cartas
        elif action == "tax":
            print("Player do: tax(Duke)")
            playern = next_player(many_players, playern)
            obj_actions.tax(player_list ,playern-2)
        elif action == "assassinate":
            print("Player do: assassinate(Assassins)")
            playern = next_player(many_players, playern)
            obj_actions.assassinate(player_list[playern-2], player_list, playern-2, "assassin")
            # obj_actions.assassinate(player_list ,playern)
        elif action == "exchange":
            print("Player do: exchange(Ambassador)")
            # obj_actions.exchange(player_list ,playern)
        elif action == "steal":
            print("Player do: steal(captain)")
            playern = next_player(many_players, playern)
            obj_actions.steal(player_list[playern-2], player_list, playern-2, "captain")

        #WHEN PLAYER IS DEAD
        if action == "dead":
            print("Player is dead - No action")
            return 0
        print(playern , "TURNO --------------------------------------------")
        
        


        

    #PANELES DE JUGADORES AQUI -----------------------------------------------------------------------------

    def playerpanel(playern): #ESTE PANEL SOLO LO VE EL JUGADOR QUE TIENE EL TURNO
        global player_panel
        if player_list[playern-1].cards[0] == " " and player_list[playern-1].cards[1] == " ":
            print("player is dead")
            playern = next_player(many_players, playern)
            player_panel.destroy()

        #PANEL DE JUGADA DEL JUGADOR
        
        player_panel = tki.Toplevel(main_panel)
        player_panel.title("PLAYER")

        player_label = tki.Label(player_panel, text="CHOSE AN ACTION", font="times 20")
        player_label.grid(row = 0, column = 1)

        #Show Player Cards and Coins
        actual_player = str(player_list[playern-1].name_id)
        player_n = tki.Label(player_panel, text=(actual_player), font="times 20")
        player_n.grid(row = 1, column = 1)

        cards_str = str("Your Cards: " + player_list[playern-1].cards[0] + " ," + player_list[playern-1].cards[1] + "\nCoins: " + str(player_list[playern-1].coins))
        player_label_info = tki.Label(player_panel, text=(cards_str), font="times 15")
        player_label_info.grid(row = 2, column = 1)

        #actions options
        buttom_income = tki.Button(player_panel, text = " Income ", width = 5, height = 1, font = "consolas 10", bg = "grey", fg = "white", command = lambda: action("income"))
        buttom_income.config(padx=10)
        buttom_foreingn_aid = tki.Button(player_panel, text = " Foreingn Aid ", width = 5, height = 1, font = "consolas 10", bg = "grey", fg = "white", command = lambda: action("foreingn_aid"))
        buttom_foreingn_aid.config(padx=23)
        buttom_coup = tki.Button(player_panel, text = " Coup ", width = 5, height = 1, font = "consolas 10", bg = "grey", fg = "white", command = lambda: action("coup"))
        buttom_coup.config(padx=10)

        #Posicionar actions
        buttom_income.grid(row = 3, column = 0, padx = 20)
        buttom_foreingn_aid.grid(row = 3, column = 1, padx = 20)
        buttom_coup.grid(row = 3, column = 2, padx = 20)

        #card options
        cards_title = tki.Label(player_panel, text="or Choose card Action: ", font="times 10")
        cards_title.grid(row = 4, column = 1)

        buttom_tax = tki.Button(player_panel, text = " DUKE ", width = 5, height = 1, font = "consolas 12", bg = "pink", fg = "black", command = lambda: action("tax"))
        buttom_tax.config(padx = 20, pady = 20)

        buttom_assassinate = tki.Button(player_panel, text = " ASSASSIN ", width = 5, height = 1, font = "consolas 12", bg = "grey", fg = "white", command = lambda: action("assassinate"))
        buttom_assassinate.config(padx = 20, pady = 20)

        buttom_exchange = tki.Button(player_panel, text = " ABBASSADOR ", width = 5, height = 1, font = "consolas 12", bg = "lime", fg = "black", command = lambda: action("exchange"))
        buttom_exchange.config(padx = 20, pady = 20)

        buttom_steal = tki.Button(player_panel, text = " CAPTAIN ", width = 5, height = 1, font = "consolas 12", bg = "cyan", fg = "black", command = lambda: action("steal"))
        buttom_steal.config(padx = 20, pady = 20)



        #Posicionar Carts
        buttom_tax.grid(row = 5, column = 0)
        buttom_assassinate.grid(row = 5, column = 1)
        buttom_exchange.grid(row = 5, column = 2)
        buttom_steal.grid(row = 6, column = 1)
        
        #INFO EN PANEL JUGADOR
        info_1 = str("PLAYER 1: \nCoins: " + str(player_list[0].coins) + " \nCards: " + player_list[0].show[0] + " " + player_list[0].show[1])
        info_player_1 = tki.Label(player_panel, text=(info_1), fg="white", bg="black")
        info_player_1.grid(row = 8, column = 0)
    
        info_2 = str("PLAYER 2: \nCoins: " + str(player_list[1].coins) + " \nCards: " + player_list[1].show[0] + " " + player_list[1].show[1])
        info_player_2 = tki.Label(player_panel, text=(info_2), fg="white", bg="black")
        info_player_2.grid(row = 8, column = 1)
    
        info_3 = str("PLAYER 3: \nCoins: " + str(player_list[2].coins) + " \nCards: " + player_list[2].show[0] + " " + player_list[2].show[1])
        info_player_3 = tki.Label(player_panel, text=(info_3), fg="white", bg="black")
        info_player_3.grid(row = 8, column = 2)
    
        if len(player_list) == 4:
            info_4 = str("PLAYER 4: \nCoins: " + str(player_list[3].coins) + " \nCards: " + player_list[3].show[0] + " " + player_list[3].show[1])
            info_player_4 = tki.Label(player_panel, text=(info_4), fg="white", bg="black")
            info_player_4.grid(row = 9, column = 1)

        #DEBUGS EN CONSOLA
        #COINS
        print(player_list[0].coins , "INCOME DEL JUGADOR 1", player_list[0].name_id)
        print(player_list[1].coins , "INCOME DEL JUGADOR 2", player_list[1].name_id)
        print(player_list[2].coins , "INCOME DEL JUGADOR 3", player_list[2].name_id)
        print()

        #INFLUENCE
        print(player_list[0].influence , "influence DEL JUGADOR 1", player_list[0].name_id)
        print(player_list[1].influence , "influence DEL JUGADOR 2", player_list[1].name_id)
        print(player_list[2].influence , "influence DEL JUGADOR 3", player_list[2].name_id)
        print()

        #ALIVE
        print(player_list[0].alive , "alive DEL JUGADOR 1", player_list[0].name_id)
        print(player_list[1].alive , "alive DEL JUGADOR 2", player_list[1].name_id)
        print(player_list[2].alive , "alive DEL JUGADOR 3", player_list[2].name_id)
        print()

        #CARDS
        print(player_list[0].cards , "alive DEL JUGADOR 1", player_list[0].name_id)
        print(player_list[1].cards , "alive DEL JUGADOR 2", player_list[1].name_id)
        print(player_list[2].cards , "alive DEL JUGADOR 3", player_list[2].name_id)
        print()


    def Update_info():
        #AQUI SE ACTUALIZA LA INFO DEL PANEL PRINCIPAL Para que se actualize apenas se hagas la accion ====================================================== ARREGLAR CARTAS
        info_1 = str("PLAYER 1: \nCoins: " + str(player_list[0].coins) + " \nCards: " + player_list[0].show[0] + " " + player_list[0].show[1])
        info_player_1.config(text=(info_1))

        info_2 = str("PLAYER 2: \nCoins: " + str(player_list[1].coins) + " \nCards: " + player_list[1].show[0] + " " + player_list[1].show[1])
        info_player_2.config(text=(info_2))

        info_3 = str("PLAYER 3: \nCoins: " + str(player_list[2].coins) + " \nCards: " + player_list[2].show[0] + " " + player_list[2].show[1])
        info_player_3.config(text=(info_3))

        if len(player_list) == 4:
            info_4 = str("PLAYER 4: \nCoins: " + str(player_list[3].coins) + " \nCards: " + player_list[3].show[0] + " " + player_list[3].show[1])
            info_player_4.config(text=(info_4))



    #PANEL PRINCIPAL
    tilecoup = tki.Label(main_panel, text="COUP", font=("Times", 40, "bold"), bg="grey", fg="white")
    #tilecoup.grid(row = 0, column=1)
    tilecoup.pack()

    global N_plabel #Para poder hacerle .config en cualquier funcion
    N_plabel = tki.Label(main_panel, font="consolas 10", bg="white", fg="black")
    N_plabel.config(text = "Player 1´s your turn", font="times 20")
    N_plabel.pack()

    nextturn = tki.Button(main_panel, text="Play Turn", font="consolas 20", command = lambda: playerpanel(playern))
    nextturn.pack()


    #Close
    exit_all = tki.Button(main_panel, text="Exit", command=main_panel.destroy)
    exit_all.pack()
    
    main_panel.mainloop() #Aqui abre la ventana y ejecuta los botones
    
    
if __name__== '__main__':
    main();
    
    
    
    
    #Notas del programa> Creo que hacer la lista de jugadores fue una estupidez dxdxdx