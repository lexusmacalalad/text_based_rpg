import os
# from functions.main_menu_functions import *
# from functions.system_func import *
# from functions.classes import *

# import functions.main_menu_functions as functions
# import functions.system_func as system_func
# import functions.classes

import functions.classes as classes
import functions. main_menu_functions as functions
import functions.system_func as system_func

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
        system_func.clear()

        if main_choice == "1":
            functions.new_game()
            menu = False
            game = True

        elif main_choice == "2":
            print(f"Welcome back, {functions.character.name}!")
            input("Press enter to continue your journey.")
            menu = False
            game = True
        
        elif main_choice == "3":
            functions.instructions()

        elif main_choice == "4":
            functions.exit_game()
            menu = False
            run = False
        
        else:
            system_func.clear()
            print("That was an incorrect input!")

    # *** GAME ***
    while game:
        system_func.clear()
        functions.character.show_stats()
        game_menu = input(f"Select the following options:\n [1] Traverse the map\n [2] Use Potion\n [3] Save Progress\n")

        if game_menu == "1":
            game = False
            functions.move()
            game = True

        elif game_menu == "2":
            functions.character.use_potion()
        
        elif game_menu == "3":
            # functions.save_game()
            game = False
            menu = True