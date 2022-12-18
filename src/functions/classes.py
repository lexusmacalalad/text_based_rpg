from random import randint
import sys
from tabulate import tabulate

import functions.system_func as system_func


class Character:
    max_health = 50
    health = 50
    level = 1
    exp_to_lvl = 20
    exp = 0
    attack = 5
    inventory = {"Health Potion": 2}

    def __init__(self, name):
        self.name = name

    def use_potion(self):
        if self.health != self.max_health:
            if self.inventory["Health Potion"] > 0:
                self.health += 15
                self.inventory["Health Potion"] -= 1
                system_func.clear()
                print("You used 1 potion and healed for 15 health points!")
                system_func.enter()
                if self.health > self.max_health:
                    self.health = self.max_health
            else:
                system_func.clear()
                print("You don't have any potions left.")
                system_func.enter()
        else:
            system_func.clear()
            print("Your health is maxed out!")
            system_func.enter()

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
        
        table = [["Name ", self.name], ["Health ", f"{self.health}/{self.max_health}"], ["Level", self.level], ["Experience ", f"{self.exp}/{self.exp_to_lvl}"], ["Attack ", self.attack], ["Health Potions", self.inventory["Health Potion"]]]

        print(tabulate(table, tablefmt = "simple_grid"))


# *** MONSTER CLASSES ***
class Monster:

    def __init__(self, name, health, attack, spoils, exp_given):
        self.name = name
        self.health = health
        self.attack = attack
        self.spoils = spoils
        self.exp_given = exp_given

    def fight(self, character):
        fight = True
        while self.health > 0:
            system_func.clear()
            character.show_stats()
            fight = input("[1] Fight\n[2] Use Potion\n[3] Flee\n")

            if fight == "1":
                system_func.clear()
                character.show_stats()
                character.health = character.health - self.attack
                print(f"You attacked {self.name} with {character.attack}")
                system_func.enter()
                self.health -= character.attack
                print(f"{self.name} attacked you for {self.attack} damage.")
                system_func.enter()

                if self.name == "Lucifer the Behemoth":
                    print("The Kingdom of Yggdra cannot thank you enough adventurer. Thank you for accepting this quest and defeating Lucifer the Behemoth. You have saved our kingdom from Perill.")
                    quit
                
                elif self.name != "Lucifer the Behemoth":
                    print(f"You've defeated {self.name}. You have gained {self.exp_given} experience!")
                    Character.exp += self.exp_given
                    if Character.exp >= Character.exp_to_lvl:
                        character.level_up()
                        print("You leveled up and grew stronger. You might be able to take on the demon king soon.")
                        character.show_stats()
            
            elif fight == "2":
                character.use_potion()

            elif fight == "3":
                if self.name == "Lucifer the Behemoth":
                    print("You cannot run away from the demon king")
                
                else:
                    system_func.clear()
                    print("You have fled")
                    system_func.enter()
                    fight = False
                    break
            
            else:
                print("That is not the correct input.")
       
        return character
    
    def show_stats(self):
        print(self.name, self.health, self.attack, self.spoils, self.exp_given)



