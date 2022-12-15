import os
# from random import randint, random
# import random
from functions.main_menu_functions import *

run = True
menu = True
game = False
move = False

while run:
    os.system('clear')
    # functions.introduction()

    # *** MAIN MENU ***
    while menu:
        main_choice = input("Please select the following options.\n [1] Start New Game\n [2] Load Game\n [3] How to Play\n [4] Exit Game\n")
        clear()

        if main_choice == "1":
            character = new_game()
            print("Your starting stats are:")
            character.show_stats()
            enter()
            menu = False
            game = True

        elif main_choice == "2":
            print(f"Welcome back, {character.name}!")
            input("Press enter to continue your journey.")
            menu = False
            game = True
        
        elif main_choice == "3":
            instructions()

        elif main_choice == "4":
            exit_game()
            menu = False
            run = False
        
        else:
            clear()
            print("That was an incorrect input!")

    # *** GAME ***
    while game:
        clear()
        character.show_stats()
        game_menu = input(f"Select the following options:\n [1] Traverse the map\n [2] Use Potion\n [3] Save Progress\n")

        if game_menu == "1":
            pass
            # game = False
            # functions.move()

        elif game_menu == "2":
            character.use_potion()
        
        elif game_menu == "3":
            # functions.save_game()
            game = False
            menu = True