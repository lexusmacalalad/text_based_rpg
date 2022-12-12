

class Character:
    max_health = 50
    health = 50
    level = 1
    exp_to_lvl = 20
    exp = 0
    attack = 10
    items = []

    def __init__(self, name):
        self.name = name

    def level_up(self):
        self.level += 1;
        self.exp_to_lvl = int(self.exp_to_lvl + (self.exp_to_lvl * 0.25))
        self.exp = 0
        self.health += 5
        self.attack += 1

        return self



