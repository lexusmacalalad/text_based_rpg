import sys
from time import sleep
import os

sys.path.append('../classes')
import classes.classes as character_class


def introduction():
    intro = "Yggdra, once was a peaceful kingdom, until one day. Lucifer the Behemoth has appeared from the depths of hell and devoured everything in its path. As the kingdom nears its demise, you have volunteered to put an end to the endless suffering of the remaining population of Yggdra.\n"
    for char in intro:
        sleep(0.02)
        print(char, end='', flush=True)

    enter = input("Press enter to start your journey!")
    if enter == "":
        pass


def new_game():
    char_name = input("Greetings adventurer, you are the last hope of the kingdom of Yggdra. Could you please tell me your name?\n")
    print("The Kingdon of Yggdra is very thankful to have a brave adventurer like you, " + char_name)

    character = character_class.Character(char_name)
    return character

def exit_game():
    print("Thank you for playing Tales of Yggdra. See you back here soon!")
    quit