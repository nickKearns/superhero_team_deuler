import random


class Hero(object):
    def __init__(self, name, starting_health):
        '''Instance properties:
          abilities: List
          armors: List
          name: String
          starting_health: Integer
          current_health: Integer
      '''
        
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        self.abilities.append(ability)



    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage






class Ability(object):
    def __init__(self, name, max_damage):
        '''Create Instance Variables:
          name:String
          max_damage: Integer
       '''
        self.name = name
        self.max_damage = max_damage


    def attack(self):
        ''' Return a value between 0 and the value set by self.max_damage.'''
        return random.randint(0, self.max_damage)


class Armor(object):
    def __init__(self, name, max_block):
        '''Instantiate instance properties.
            name: String
            max_block: Integer
        '''
        self.name = name
        self.max_block = max_block

    def block(self):
        ''' Return a random value between 0 and the initialized max_block strength. '''

        return random.randint(0, self.max_block)


if __name__ == '__main__':
    my_hero = Hero("test hero", 100)
    print(my_hero.name)
    print(my_hero.starting_health)
    test_ability = Ability("debug ability", 50)
    test_ability2 = Ability("debug ability 2", 30)
    my_hero.add_ability(test_ability)
    #print(my_hero.abilities)
    my_hero.add_ability(test_ability2)
    print(my_hero.attack())



