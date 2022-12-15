from random import randint
import sys
from tabulate import tabulate

sys.path.append('../functions')
import functions.main_menu_functions as functions

sys.path.append('../../src')
import main as char_class

class Character:
    max_health = 50
    health = 50
    level = 1
    exp_to_lvl = 20
    exp = 0
    attack = 4
    inventory = {"Health Potion": 2}

    def __init__(self, name):
        self.name = name

    def use_potion(self):
        if self.health != self.max_health:
            if self.inventory["Health Potion"] > 0:
                self.health += 15
                self.inventory["Health Potion"] -= 1
                functions.clear()
                print("You healed for 15 health points!")
                functions.enter()
                if self.health > self.max_health:
                    self.health = self.max_health
            else:
                functions.clear()
                print("You don't have any potions left.")
                functions.enter()
        else:
            functions.clear()
            print("Your health is maxed out!")
            functions.enter()

    def level_up(self):
        self.level += 1;
        self.exp_to_lvl = int(self.exp_to_lvl + (self.exp_to_lvl * 0.25))
        self.exp = 0
        self.max_health += 5
        self.health = self.max_health
        self.attack += 2

        return self

    def show_stats(self):
        """Show player stats as table format"""
        
        table = [["Name ", self.name], ["Health ", f"{self.health}/{self.max_health}"], ["Experience ", f"{self.exp}/{self.exp_to_lvl}"], ["Attack ", self.attack], ["Health Potions", self.inventory["Health Potion"]]]

        print(tabulate(table, tablefmt = "simple_grid"))


# *** MONSTER CLASSES ***
class Monster:

    def __init__(self, name, health, attack, spoils, exp_given):
        self.name = name
        self.health = health
        self.attack = attack
        self.spoils = spoils
        self.exp_given = exp_given

    def fight(self):
        while self.health > 0:
            char_class.character.health = char_class.character.health - randint(1,(self.attack * 2))
            print(char_class.character.health)
            self.health -= char_class.character.attack

        print(f"You've defeated {self.name}. You have gained {self.exp_given} experience!")
        return char_class.character



