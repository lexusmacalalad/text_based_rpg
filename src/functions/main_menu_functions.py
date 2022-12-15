import sys
from time import sleep
import os
from random import randint, random
# imported random twice as the one above wouldn't let me explicitly import the random function "choice"
import random

sys.path.append('../classes')
import classes.classes as class_objects

# sys.path.append('../src')
# import src.main as char_class

# *** SYSTEM ***
def clear():
    """To clear out terminal screen"""
    os.system('clear')

def enter():
    input("Press enter to continue.")

# *** MAIN MENU ***
def introduction():
    intro = "Yggdra, once was a peaceful kingdom, until one day. Lucifer the Behemoth has appeared from the depths of hell and devoured everything in its path. As the kingdom nears its demise, you have volunteered to put an end to the endless suffering of the remaining population of Yggdra.\n"

    # Add typewriter effect on introduction
    for char in intro:
        sleep(0.02)
        print(char, end='', flush=True)

    input("Press enter to start your journey!")
    clear()

def new_game():
    """Creates a new game"""
    char_name = input("Greetings adventurer, you are the last hope of the kingdom of Yggdra. Could you please tell me your name?\n")
    clear()
    print("The Kingdon of Yggdra is very thankful to have a brave adventurer like you, " + char_name + "!")
    
    return class_objects.Character(char_name)

def load_game():
    """Loads previously saved game"""
    pass

def instructions():
    clear()
    instruction = "You have been tasked to defeat the king of hell, Lucifer the Behemoth. Throughout your journey, you will encounter monsters that will help you get stronger. Defeating these monsters will allow you to level up, boosting your stats, as well as a chance to receive health potions that can heal you.\n \nThis game is inspired by the souls series games from From Software, therefore it will be challenging to beat, based on your luck. Lower tier monsters have a higher chance to spawn, whereas stronger monsters have a higher chance to spawn as you traverse the map. Choose your actions wisely as you will not be able to run away from Lucifer once you encounter him. You might need to play this game a few times to learn which monsters are weak, and which ones you should take earlier on to get stronger.\n \nYou will be prompted actions by the game, and which option to choose is up to you. Choose wisely! Good luck out there, adventurer.\n"
    
    # Add type writer effect to instruction
    for char in instruction:
        sleep(0.02)
        print(char, end='', flush=True)

    enter()
    clear()

def exit_game():
    """Closes the program completely"""
    print("Thank you for playing Tales of Yggdra. See you back soon, adventurer!")
    quit

# *** GAME ***
def save_game(): # ####### COMPLETE THIS LATER #########
    """Saves current progression of the player"""
    f = open("load.txt", "w")
    print("You have saved your progress.")

# *** MAP MOVEMENT ***
# def move():
#     move = True

#     while move:
#         clear()
#         # char_class.character.show_stats()
#         movement = input("[1] North\n [2] East\n [3] South\n [4] West\n [5] Back")

#         if movement == "1":
#             pass
#         elif movement == "2":
#             pass
#         elif movement == "3":
#             pass
#         elif movement == "4":
#             pass
#         elif movement == "5":
#             move = False
#             # char_class.game = True
#             pass
#         else:
#             print("You have entered the wrong input")



# *** ENEMY SPAWN ***
def spawn_enemy():
    """Randomly select enemy based on percentage - stronger monsters have a lower chance of spawning""" 
    spawn = randint(1, 100)
    if spawn <= 64:
        return random.choice(["Small Goblin", "Earth Golem", "Brown Python", "Peasant", "Outcast"])
    elif spawn <= 87:
        return random.choice(["Higher Goblin", "Stone Golem", "Spiked Turtoise", "Barbarian"])
    elif spawn <= 97:
        return random.choice(["Marauder", "The Colossus", "Flame Dragon"])
    else:
        return "Lucifer the Behemoth"

def create_enemy():
    """Creates a monster instance based on enemy spawned"""
    
    enemy = spawn_enemy()
    
    # Goblin Class
    if enemy == "Small Goblin":
        return class_objects.Monster("Small Goblin", 15, 3, {"Health Potion": 1}, 5)
    elif enemy == "Higher Goblin":
        return class_objects.Monster("Higher Goblin", 23, 9, {"Health Potion": 2}, 13)
    elif enemy == "Marauder":
        return class_objects.Monster("Marauder", 65, 20, {"Health Potion": 3}, 25)

    # Golem Class
    elif enemy == "Earth Golem":
        return class_objects.Monster("Earth Golem", 20, 2, {"Health Potion": 1}, 6)
    elif enemy == "Stone Golem":
        return class_objects.Monster("Stone Golem", 40, 5, {"Health Potion": 1}, 15)
    elif enemy == "The Colossus":
        return class_objects.Monster("The Colossus", 80, 14, {"Health Potion": 2}, 23)
    
    # Reptilian Class
    elif enemy == "Brown Python":
        return class_objects.Monster("Brown Python", 12, 5, "No items", 7)
    elif enemy == "Spiked Turtoise":
        return class_objects.Monster("Spiked Turtoise", 30, 6, {"Health Potion": 2}, 15)
    elif enemy == "Flame Dragon":
        return class_objects.Monster("Flame Dragon", 50, 25, {"Health Potion": 2}, 30)
    
    # Human Class
    elif enemy == "Peasant":
        return class_objects.Monster("Peasant", 8, 2, "No items", 3)
    elif enemy == "Outcast":
        return class_objects.Monster("Outcast", 10, 2, "No items", 5)
    elif enemy == "Barbarian":
        return class_objects.Monster("Barbarian", 20, 10, {"Health Potion": 2}, 15)

    # Boss Class
    else:
        return class_objects.Monster("Lucifer the Behemoth", 250, 35, "No items", 0)


