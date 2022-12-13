import sys
from time import sleep
import os
from random import randint, random

import random

def spawn_enemy():
    num = randint(1, 100)
    if num <= 64:
        return random.choice(["Small Goblin", "Earth Golem", "Brown Python", "Peasant", "Outcast"])
    elif num <= 87:
        return random.choice(["Higher Goblin", "Stone Golem", "Spiked Turtoise", "Barbarian"])
    elif num <= 97:
        return random.choice(["Marauder", "The Colosus", "Flame Dragon"])
    else:
        return "Lucifer the Behemoth"

enemy = spawn_enemy()

print(enemy)