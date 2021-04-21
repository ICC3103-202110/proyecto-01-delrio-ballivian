<<<<<<< HEAD

from actions import *
from player import *
=======
from player import Player
from actions import *
>>>>>>> eb18f2692faeecdd62207848803734ed4968a7ca
from start import *
from cards import *
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
    number_start = startmenu(); N = number_start.start()
    many_players = N
    print(many_players, "N players")
<<<<<<< HEAD
    #deck creations

    #Player creation

    if many_players == 3:
        Mazo = Cards()
        player_list=[]

        for i in range(many_players):
            player_list.append(Player("jugador " + str(i), i))
            #dos_cartas = [Cards.give_cards(player_list[i], Mazo)]
            player_list[i].cards = Mazo.give_cards(player_list[i])
            print(player_list[i].cards[0],player_list[i].cards[1])



    elif many_players == 4:
        Mazo = Cards()
        player_list=[]

        for i in range(many_players):
            player_list.append(Player("jugador " + str(i), i))
            #dos_cartas = [Cards.give_cards(player_list[i], Mazo)]
            player_list[i].cards = Mazo.give_cards(player_list[i])
            print(player_list[i].cards[0],player_list[i].cards[1])
    

=======
    #Player creation
    if many_players == 3:
        player_1 = Player(1)
        player_2 = Player(2)
        player_3 = Player(3)
        player_list = [player_1, player_2, player_3]
    elif many_players == 4:
        player_1 = Player(1)
        player_2 = Player(2)
        player_3 = Player(3)
        player_4 = Player(4)
        player_list = [player_1, player_2, player_3, player_4]
    
    #Player Cards
    Cards.give_cards(player_list)
>>>>>>> eb18f2692faeecdd62207848803734ed4968a7ca
    
    #VER TODAS LAS CARTAS
    for i in range(len(player_list)):
            print(player_list[i].cards, "cartas jugador ", player_list[i].name_id)
    
    
    #Panel Creation
    global playern 
    playern = 1
    main_panel = tki.Tk()
    main_panel.title("CUOP v0.1.0")
    main_panel.geometry("500x500")
    
    #Esta la puedo meter en una Class!!
    def next_player(many_players, playern): #funcion para loopear para saber los turnos una vez que llegan al ultimo jugador
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
<<<<<<< HEAD
            player_list[playern-1].coins +=1
            print("Player", playern, " do: income")
            
=======
            print("Player", playern, " do: income")
            
            Actions.income(player_list[playern-1])
            
>>>>>>> eb18f2692faeecdd62207848803734ed4968a7ca
        elif action == "foreingn_aid":
            print("Player", playern, " do: foreingn_aid")
            
            Actions.foreingn_aid(player_list[playern-1])
            
        elif action == "coup":
            print("Player", playern, " do: coup")
            
            playern = next_player(many_players, playern) #Lo tengo que ejecutar ya que la funcion de Cuop deja de ejecutar lo que tenga abajo
            Actions.coup(player_list[playern-2], player_list) #AQUI VA UN -2 DE MANERA QUE PUEDA EJECUTAR EL next_player Tras hacer un Coup
            #LO DE ARRIBA ESTOY BUSCANDO UNA SOLUCION PARA QUE FUNCIONE DE FORMA MAS CORRECTA
            
        #Cartas
        elif action == "tax":
            print("Player do: tax")
        elif action == "assassinate":
            print("Player do: assassinate")
        elif action == "exchange":
            print("Player do: exchange")
        elif action == "steal":
            print("Player do: steal")
        
        elif action == "dead":
            print("Player is dead - No action")
            
        #CHALLENGE
        
        
        #Siguiente turno
        playern = next_player(many_players, playern)
        print(playern , "TURNO --------------------------------------------")
        
        #ACTULIZAR EL ESTADO DEL JUGADOR 
        Player.player_state(player_list) 
        if player_list[playern-1].alive == False: #auto ejecutar la funcion dead
            action("dead") #La unica manera que se me ocurrio para poder pasar turno
            return 
<<<<<<< HEAD


            
        
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

=======
        #ACTUALIZAR ESTADO DE LAS CARTAS DEL JUGADOR
        Player.cards_state(player_list)
            
        
        #AQUI SE ACTUALIZA LA INFO DEL PANEL PRINCIPAL Para que se actualize apenas se hagas la accion ====================================================== ARREGLAR CARTAS
        info_1 = str("PLAYER 1: \nCoins: " + str(player_1.coins) + " \nCards: " + player_1.show[0] + " " + player_1.show[1])
        info_player_1.config(text=(info_1))
        
        info_2 = str("PLAYER 1: \nCoins: " + str(player_2.coins) + " \nCards: " + player_2.show[0] + " " + player_2.show[1])
        info_player_2.config(text=(info_2))
        
        info_3 = str("PLAYER 1: \nCoins: " + str(player_3.coins) + " \nCards: " + player_3.show[0] + " " + player_3.show[1])
        info_player_3.config(text=(info_3))
        
        if len(player_list) == 4:
            info_4 = str("PLAYER 1: \nCoins: " + str(player_4.coins) + " \nCards: " + player_4.show[0] + " " + player_4.show[1])
            info_player_4.config(text=(info_4))
>>>>>>> eb18f2692faeecdd62207848803734ed4968a7ca
        
    def counteraction(counteraction):
        return 0
        
    def playerpanel(playern): #ESTE PANEL SOLO LO VE EL JUGADOR QUE TIENE EL TURNO
            
            #PANEL DE JUGADA DEL JUGADOR
            global player_panel
            player_panel = tki.Toplevel(main_panel)
            player_panel.title("PLAYER")
          
            player_label = tki.Label(player_panel, text="CHOSE AN ACTION", font="times 20")
            player_label.grid(row = 0, column = 1)
            
            #Show Player Cards and Coins
            cards_str = str("Your Cards: " + player_list[playern-1].cards[0] + " ," + player_list[playern-1].cards[1] + "\nCoins: " + str(player_list[playern-1].coins))
            print(cards_str)
            player_label_info = tki.Label(player_panel, text=(cards_str), font="times 15")
            player_label_info.grid(row = 1, column = 1)
            
            #actions options
            buttom_income = tki.Button(player_panel, text = " Income ", width = 5, height = 1, font = "consolas 10", bg = "grey", fg = "white", command = lambda: action("income"))
            buttom_income.config(padx=10)
            buttom_foreingn_aid = tki.Button(player_panel, text = " Foreingn Aid ", width = 5, height = 1, font = "consolas 10", bg = "grey", fg = "white", command = lambda: action("foreingn_aid"))
            buttom_foreingn_aid.config(padx=23)
            buttom_coup = tki.Button(player_panel, text = " Coup ", width = 5, height = 1, font = "consolas 10", bg = "grey", fg = "white", command = lambda: action("coup"))
            buttom_coup.config(padx=10)
            
            #Posicionar actions
            buttom_income.grid(row = 2, column = 0, padx = 20)
            buttom_foreingn_aid.grid(row = 2, column = 1, padx = 20)
            buttom_coup.grid(row = 2, column = 2, padx = 20)
            
            #card options
            cards_title = tki.Label(player_panel, text="or Choose card Action: ", font="times 10")
            cards_title.grid(row = 3, column = 1)
            
            buttom_tax = tki.Button(player_panel, text = " DUKE ", width = 5, height = 1, font = "consolas 12", bg = "pink", fg = "black", command = lambda: action("tax"))
            buttom_tax.config(padx = 20, pady = 20)
            
            buttom_assassinate = tki.Button(player_panel, text = " ASSASSIN ", width = 5, height = 1, font = "consolas 12", bg = "grey", fg = "white", command = lambda: action("assassinate"))
            buttom_assassinate.config(padx = 20, pady = 20)
            
            buttom_exchange = tki.Button(player_panel, text = " ABBASSADOR ", width = 5, height = 1, font = "consolas 12", bg = "lime", fg = "black", command = lambda: action("exchange"))
            buttom_exchange.config(padx = 20, pady = 20)
            
            buttom_steal = tki.Button(player_panel, text = " CAPTAIN ", width = 5, height = 1, font = "consolas 12", bg = "cyan", fg = "black", command = lambda: action("steal"))
            buttom_steal.config(padx = 20, pady = 20)
            
            
            
            #Posicionar Carts
            buttom_tax.grid(row = 4, column = 0)
            buttom_assassinate.grid(row = 4, column = 1)
            buttom_exchange.grid(row = 4, column = 2)
            buttom_steal.grid(row = 5, column = 1)
            
            
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
            
            
            
    #PANEL PRINCIPAL
    tilecoup = tki.Label(main_panel, text="COUP", font=("Times", 40, "bold"), bg="grey", fg="white")
    #tilecoup.grid(row = 0, column=1)
    tilecoup.pack()
    
    global N_plabel #Para poder hacerle .config en cualquier funcion
    N_plabel = tki.Label(main_panel, font="consolas 10", bg="white", fg="black")
    N_plabel.config(text = "Player 1 is your turn", font="times 20")
    #N_plabel.grid(row = 1, column=1)
    N_plabel.pack()

    nextturn = tki.Button(main_panel, text="Play Turn", font="consolas 20", command = lambda: playerpanel(playern)) 
    #nextturn.grid(row = 2, column=1)
    nextturn.pack()
    
    
    #INICIALIZAR LA INFO DE LOS JUGADORES
<<<<<<< HEAD
    info_1 = str("PLAYER 1: \nCoins: " + str(player_list[0].coins) + " \nCards: " + player_list[0].show[0] + " " + player_list[0].show[1])
    info_player_1 = tki.Label(main_panel, text=(info_1))
    info_player_1.pack()
    
    info_2 = str("PLAYER 1: \nCoins: " + str(player_list[1].coins) + " \nCards: " + player_list[1].show[0] + " " + player_list[1].show[1])
    info_player_2 = tki.Label(main_panel, text=(info_2))
    info_player_2.pack()
    
    info_3 = str("PLAYER 1: \nCoins: " + str(player_list[2].coins) + " \nCards: " + player_list[2].show[0] + " " + player_list[2].show[1])
=======
    info_1 = str("PLAYER 1: \nCoins: " + str(player_1.coins) + " \nCards: " + player_1.show[0] + " " + player_1.show[1])
    info_player_1 = tki.Label(main_panel, text=(info_1))
    info_player_1.pack()
    
    info_2 = str("PLAYER 1: \nCoins: " + str(player_2.coins) + " \nCards: " + player_2.show[0] + " " + player_2.show[1])
    info_player_2 = tki.Label(main_panel, text=(info_2))
    info_player_2.pack()
    
    info_3 = str("PLAYER 1: \nCoins: " + str(player_3.coins) + " \nCards: " + player_3.show[0] + " " + player_3.show[1])
>>>>>>> eb18f2692faeecdd62207848803734ed4968a7ca
    info_player_3 = tki.Label(main_panel, text=(info_3))
    info_player_3.pack()
    
    if len(player_list) == 4:
<<<<<<< HEAD
        info_4 = str("PLAYER 1: \nCoins: " + str(player_list[3].coins) + " \nCards: " + player_list[3].show[0] + " " + player_list[3].show[1])
=======
        info_4 = str("PLAYER 1: \nCoins: " + str(player_4.coins) + " \nCards: " + player_4.show[0] + " " + player_4.show[1])
>>>>>>> eb18f2692faeecdd62207848803734ed4968a7ca
        info_player_4 = tki.Label(main_panel, text=(info_4))
        info_player_4.pack()
        
    #Close
    exit_all = tki.Button(main_panel, text="Exit", command=main_panel.destroy)
    exit_all.pack()
    
    main_panel.mainloop() #Aqui abre la ventana y ejecuta los botones
    
    
if __name__== '__main__':
    main();
    
    
    
    
    #Notas del programa> Creo que hacer la lista de jugadores fue una estupidez dxdxdx