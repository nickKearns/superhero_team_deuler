import random

class Ability(object):
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage


    def attack(self):
        return random.randint(0, self.max_damage)

if __name__ == '__main__':
    ability = Ability("debug ability", 20)
    print(ability.name)
    print(ability.attack())

