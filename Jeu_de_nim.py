# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 09:21:03 2023

@author: JordanKamto && CamatoDev
"""

import tkinter

#création de la fenêtre principale  
menuApp = tkinter.Tk()
menuApp.title("NIM GAME")

menuApp.resizable(width=False, height=False)
menuApp.geometry("600x400") 

def main():
    #fermeture de la fenêtre principale 
    menuApp.destroy()
    
    #création de la fenêtre de jeu 
    mainApp = tkinter.Tk()
    mainApp.title("NIM GAME")

    mainApp.resizable(width=False, height=False)
    mainApp.geometry("600x400") 
    
    board_frame = tkinter.Frame(mainApp, width= 400, height=200)
    
    pile_label = tkinter.Label(mainApp, text="Choisissez un tas (1, 2, 3, 4) : ")
    pile_entry=tkinter.Entry(mainApp)
    
    num_to_remove_label = tkinter.Label(mainApp, text="Combien d'allumettes souhaitez-vous retirer du tas ? ")
    remove_entry=tkinter.Entry(mainApp)
    
    message_label = tkinter.Label(board_frame, text="", fg="red")
    
    tas_label = tkinter.Label(mainApp)
    tas_label2 = tkinter.Label(mainApp)
    tas_label3 = tkinter.Label(mainApp)
    tas_label4 = tkinter.Label(mainApp)
    
    piles = [1, 3, 5, 7]
    
    def display_board(piles):
        
        tas_label.config(text=f"Tas {0+1} : {'|' * piles[0]} ({piles[0]}) allumettes", font=("Helvetica",16))
        tas_label2.config(text=f"Tas {1+1} : {'|' * piles[1]} ({piles[1]}) allumettes", font=("Helvetica",16))
        tas_label3.config(text=f"Tas {2+1} : {'|' * piles[2]} ({piles[2]}) allumettes", font=("Helvetica",16))
        tas_label4.config(text=f"Tas {3+1} : {'|' * piles[3]} ({piles[3]}) allumettes", font=("Helvetica",16))
        tas_label.pack()
        tas_label2.pack()
        tas_label3.pack()
        tas_label4.pack()
            
        pile_entry.delete(0, 'end')
        remove_entry.delete(0, 'end')
            
            
    def is_game_over(piles):
        return all(pile == 0 for pile in piles)
    
    display_board(piles)
    # Tour du joueur
    def player():
        try:
            pile_choice = int(pile_entry.get()) -1 
            num_to_remove = int(remove_entry.get())
            if pile_choice <= len(piles) and 1 <= num_to_remove <= piles[pile_choice]:
                piles[pile_choice] -= num_to_remove
                message_label.config(text=f"vous avez retiré {num_to_remove} du tas {pile_choice + 1}")
                message_label.pack()
            else:
                message_label.config(text="Choix invalide. Réessayez.")
                message_label.pack()
        except (ValueError, IndexError):
            message_label.config(text="Entrée invalide. Réessayez.")
            message_label.pack()
            
        if is_game_over(piles):
            message_label.config(text="Félicitations, vous avez gagné !")
            message_label.pack()
        
        #mise à jour des tas
        tas_label.config(text="")
        tas_label2.config(text="")
        tas_label3.config(text="")
        tas_label4.config(text="")
        display_board(piles)
    
    # Tour de la machine (adversaire parfait)
    def cambot():
        for x in range(1, 7):
            x_to_remove = x
            for i, pile in enumerate(piles):
                v = piles[i]
                piles[i] -= x_to_remove
                if piles[0] ^ piles[1] ^ piles[2] ^ piles[3] == 0:
                    message_label.config(text=f"la machine a retiré {x_to_remove} du tas {i + 1}")
                    message_label.pack()
                    break
                else:
                    piles[i] = v
            
        display_board(piles)
        if is_game_over(piles):
            message_label.config(text="Désolé, vous avez perdu ! CAMBOT est trop fort :)")
    
    valid_button = tkinter.Button(mainApp, text="Valider", command=player)
    cambot_button = tkinter.Button(mainApp, text="Cambot_PLAY", command=cambot)
    
    board_frame.pack()
    
    pile_label.pack()
    pile_entry.pack()
    num_to_remove_label.pack()
    remove_entry.pack()
    valid_button.pack()
    cambot_button.pack()
    message_label.pack()
    

#fenêtre principal 
main_label = tkinter.Label(menuApp, text="JEU DE NIM", height=2, font=("Helvetica",20))
label_1 = tkinter.Label(menuApp, text="Pourras-tu battre CAMBOT.....?", height=2, font=("Helvetica",16))

frame_1 = tkinter.Frame(menuApp, width= 100, height=100)

def close():
    menuApp.destroy()

button_play = tkinter.Button(menuApp, text="JOUER", width=15, height=2, command=main)
frame_play = tkinter.Frame(menuApp, width= 100, height=10)
button_option = tkinter.Button(menuApp, text="OPTION", width=15, height=2)
frame_option = tkinter.Frame(menuApp, width= 100, height=10)
button_quit = tkinter.Button(menuApp, text="QUITTER", width=15, height=2, command=close)
frame_quit = tkinter.Frame(menuApp, width= 100, height=10)

main_label.pack()
label_1.pack()



frame_play.pack()
button_play.pack()
frame_option.pack()
button_option.pack()
frame_quit.pack()
button_quit.pack()

menuApp.mainloop()