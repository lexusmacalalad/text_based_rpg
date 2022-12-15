import os
from random import randint, random
import random
import functions.main_menu_functions as functions

menu = True
game = False

os.system('clear')
# functions.introduction()

# *** MAIN MENU ***
while menu:
    main_choice = input("Please select the following options.\n [1] To start a new game\n [2] To load a game\n [3] To exit the game\n")
    functions.clear()

    if main_choice == "1":
        character = functions.new_game()
        print("Your starting stats are:")
        character.show_stats()
        input()
        menu = False
        game = True

    elif main_choice == "2":
        print(f"Welcome back, {character.name}!")
        input("Press enter to continue your journey.")
        menu = False
        game = True

    elif main_choice == "3":
        functions.exit_game()
        menu = False
    
    else:
        functions.clear()
        print("That was an incorrect input!")

# *** GAME ***
while game:
    functions.clear()
    character.show_stats()
    game_menu = input(f"Select the following options:\n [1] Traverse the map\n [2] Use Potion\n [3] Save Progress\n")

    if game_menu == "2":
        character.use_potion()