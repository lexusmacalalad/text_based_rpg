import sys
from time import sleep
import os
from random import randint, random
# imported random twice as the one above wouldn't let me explicitly import the random function "choice"
import random

sys.path.append('../classes')
import classes.classes as class_objects

# *** SYSTEM ***
def clear():
    """To clear out terminal screen"""
    os.system('clear')

# *** MAIN MENU ***
def introduction():
    intro = "Yggdra, once was a peaceful kingdom, until one day. Lucifer the Behemoth has appeared from the depths of hell and devoured everything in its path. As the kingdom nears its demise, you have volunteered to put an end to the endless suffering of the remaining population of Yggdra.\n"
    # To add typewriter effect on introduction
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
    pass

def exit_game():
    """Closes the program completely"""
    print("Thank you for playing Tales of Yggdra. See you back soon, hero!")
    quit

# *** GAME ***
def save_game(): # ####### COMPLETE THIS LATER #########
    """Saves current progression of the player"""
    f = open("load.txt", "w")



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


