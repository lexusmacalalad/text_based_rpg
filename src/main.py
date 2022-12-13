import os

import functions.main_menu_functions as functions


os.system('clear')
# functions.draw()
# functions.introduction()

main_choice = input("Please select the following options.\n [1] To start a new game\n [2] To load a game\n [3] To exit the game\n")
os.system('clear')

if main_choice == "1":
    character = functions.new_game()

elif main_choice =="2":
    pass

elif main_choice == "3":
    functions.exit_game()
