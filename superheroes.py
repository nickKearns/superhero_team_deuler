import random


class Hero(object):
    def __init__(self, name):
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
        self.starting_health =  200
        self.current_health = 200


    def fight(self, opponent):
        ''' have one hero instance fight another hero instance '''
        while self.is_alive() and opponent.is_alive():
            if self.abilities or opponent.abilities:
                self.take_damage(opponent.attack())
                opponent.take_damage(self.attack())
            else:
                print("DRAW!")
                continue
        if self.current_health <= 0:
            print(opponent.name + " is the winner!")
        else:
            print(self.name + " is the winner!")

    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        self.abilities.append(ability)

    def add_armor(self, armor):
        ''' add armor to armor list '''
        self.armors.append(armor)

    def take_damage(self, damage):
        if damage - self.defend() > 0:
            self.current_health -= (damage - self.defend())
            print(self.name + " current health: " + str(self.current_health))
        else:
            print("The attack was completely blocked")
            print(self.name + " current health: " + str(self.current_health))




    def defend(self):
        ''' add up all the total blocks from all the armors '''
        total_block = 0
        for block in self.armors:
            total_block += block.block()
        return total_block

    def attack(self):
        ''' add up the total attacks from all the abilities '''
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage


    def is_alive(self):
        '''checks if there is health left for the hero'''
        if self.current_health <= 0:
            return False
        else:
            return True




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



class Weapon(Ability):
    def __init__(self, name, max_damage):
        super().__init__(name, max_damage)
    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        multiplier = random.uniform(1.0, 2.0)
        return self.max_damage // multiplier







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



class Team(object):
    def __init__(self, name):
        self.name = name
        self.heroes = []
    def remove_hero(self, name):
        success = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                success = True
        if success:
            return 1
        else:
            return 0
    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)
    def add_hero(self, new_hero):
        self.heroes.append(new_hero)

    







if __name__ == '__main__':
    my_hero = Hero("Superman", 200)
    their_hero = Hero("Batman", 200)
    # print(my_hero.name)
    # print(my_hero.starting_health)
    test_ability = Ability("punch", 50)
    test_ability2 = Ability("kick", 30)
    test_armor = Armor('armor', 10)
    test_armor2 = Armor('armor 2', 12)
    test_weapon = Weapon("test_weapon", 80)
    print(test_weapon.attack())
    # my_hero.add_ability(test_ability)
    # my_hero.add_ability(test_ability2)
    # my_hero.add_armor(test_armor)
    # my_hero.add_armor(test_armor2)
    # their_hero.add_ability(test_ability)
    # their_hero.add_ability(test_ability2)
    # their_hero.add_armor(test_armor)
    # their_hero.add_armor(test_armor2)
    # my_hero.fight(their_hero)
    



