import random

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
    ability = Ability("debug ability", 20)
    print(ability.name)
    print(ability.attack())
    armor = Armor("debug armor", 20)
    print(armor.block())

