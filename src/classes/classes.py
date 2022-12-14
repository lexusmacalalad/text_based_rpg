from random import randint
import sys

sys.path.append('../functions')
import functions.main_menu_functions as functions

class Character:
    max_health = 50
    health = 50
    level = 1
    exp_to_lvl = 20
    exp = 0
    attack = 10
    inventory = []

    def __init__(self, name):
        self.name = name

    def level_up(self):
        self.level += 1;
        self.exp_to_lvl = int(self.exp_to_lvl + (self.exp_to_lvl * 0.25))
        self.exp = 0
        self.max_health += 5
        self.health = self.max_health
        self.attack += 1

        return self

    def show_stats(self):
        functions.draw()
        print(
            f"  Name: {self.name}",
            f"  Health: {self.health}/{self.max_health}",
            f"  Experience: {self.exp}/{self.exp_to_lvl}",
            f"  Attack: {self.attack}",
            f"  Inventory: {self.inventory}",
            sep = "\n"
            )
        functions.draw()


# *** MONSTER CLASSES ***
class Monster:
    def battle(self):
        while self.health > 0:
            Character.health = Character.health - randint(1,(self.attack * 2))
            print(Character.health)
            self.health -= Character.attack

        print(f"You've defeated {self.name}. You have gained {self.exp_given} experience!")


class Goblin(Monster):

    def __init__(self, name, health, attack, spoils, exp_given):
        self.name = name
        self.health = health
        self.attack = attack
        self.spoils = spoils
        self.exp_given = exp_given


