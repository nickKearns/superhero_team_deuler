import random


class Hero(object):
    def __init__(self, name, starting_health=100):
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
        self.starting_health =  starting_health
        self.current_health = starting_health
        self.kills = 0
        self.deaths = 0

    def add_kills(self, num_kills):
        self.kills += num_kills

    def add_deaths(self, num_deaths):
        self.deaths += num_deaths


    def fight(self, opponent):
        ''' have one hero instance fight another hero instance '''
        while self.is_alive() and opponent.is_alive():
            if self.abilities or opponent.abilities:
                self.take_damage(opponent.attack())
                opponent.take_damage(self.attack())
            else:
                print("DRAW!")
                return 0
                continue
        if self.current_health <= 0:
            print(opponent.name + " is the winner!")
            opponent.add_kills(1)
            self.add_deaths(1)
            return self.name
        else:
            print(self.name + " is the winner!")
            self.add_kills(1)
            opponent.add_deaths(1)
            return opponent.name
    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        self.abilities.append(ability)


    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        self.abilities.append(weapon)

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
        return random.randint(self.max_damage//2, self.max_damage)







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
        ''' display the names of each hero on the team '''
        for hero in self.heroes:
            print(hero.name)
    def add_hero(self, new_hero):
        self.heroes.append(new_hero)
    def attack(self, other_team):
        ''' Battle each team against each other.'''
        while self.heroes and other_team.heroes:
            hero_1 = random.choice(self.heroes)
            hero_2 = random.choice(other_team.heroes)
            if hero_1.is_alive() and hero_2.is_alive():
                hero_1.fight(hero_2)
            
    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''
        for hero in self.heroes:
            if not hero.is_alive():
                hero.current_health = hero.starting_health

    def stats(self):
        '''Print team statistics'''
        for hero in self.heroes:
            ratio = hero.kills / hero.deaths
            print(hero.name + "'s ratio is: " + ratio)


            

class Arena:
    def __init__(self):
        self.team_one: None
        self.team_two: None


    def create_ability(self):
        name = input("Please enter the name of the ability.\n")
        max_damage = input("Please enter the maximum damage of the ability.\n")
        new_ability = Ability(name, max_damage)
        return new_ability

    def create_weapon(self):
        name = input("Please enter the name of the weapon.\n")   
        max_damage = input("Please enter the maximum damage of the weapon.\n")
        new_weapon = Weapon(name, max_damage)
        return new_weapon

    def create_armor(self):
        name = input("Please enter the name of the armor.\n")
        max_block = input("Please enter the maximum block of the armor\n.")
        new_armor = Armor(name, max_block)
        return new_armor

    def create_hero(self):
        name = input("Please enter the name of the hero.\n")
        starting_health = input("Please enter the starting health of the hero\n")
        new_hero = Hero(name, starting_health)
        num_abilities = int(input("How many abilities would you like to add?"))
        for i in range(0, num_abilities):
            new_hero.add_ability(self.create_ability())
        num__weapons = int(input("How many weapons would you like to add?"))
        for i in range(0, num__weapons):
            new_hero.add_weapon(self.create_weapon())
        num_armor = int(input("How many armors would you like to add?"))
        for i in range(0, num_armor):
            new_hero.add_armor(self.create_armor())
        return new_hero

    def build_team_one(self):
        num_heroes = input("How many heroes would you like on team one?\n")
        self.team_one = Team(input("What would you like the team name to be?\n"))
        for i in range(0, num_heroes):
            self.team_one.heroes.append(self.create_hero())
        
    def build_team_two(self):
        num_heroes = input("How many heroes would you like on team two?\n")
        self_team_two = Team(input("What would you like the team name to be?\n"))
        for i in range(0, num_heroes):
            self.team_two.heroes.append(self.create_hero())

    def team_battle(self):
        self.team_one.attack(self.team_two)


    def show_stats(self):
        team_one_total_kills = 0
        team_one_total_deaths = 0
        team_two_total_kills = 0
        team_two_total_deaths = 0
        for hero in self.team_one.heroes:
            team_one_total_kills += hero.kills
            team_one_total_deaths += hero.deaths
        for hero in self.team_two.heroes:
            team_two_total_kills += hero.kills
            team_two_total_deaths += hero.deaths
        
        team_one_ratio = team_one_total_kills / team_one_total_deaths
        team_two_ratio = team_two_total_kills / team_two_total_deaths
        print("Team one's ratio: " + team_one_ratio)
        print("Team two's ratio: " + team_two_ratio)


            

    







if __name__ == '__main__':
    my_hero = Hero("Superman")
    their_hero = Hero("Batman")
    test_hero1 = Hero("Aquaman")
    # print(my_hero.name)
    # print(my_hero.starting_health)
    test_ability = Ability("punch", 50)
    test_ability2 = Ability("kick", 30)
    test_armor = Armor('armor', 10)
    test_armor2 = Armor('armor 2', 12)
    test_weapon = Weapon("test_weapon", 80)
    #print(test_weapon.attack())
    my_hero.add_ability(test_ability)
    my_hero.add_ability(test_ability2)
    my_hero.add_armor(test_armor)
    my_hero.add_armor(test_armor2)
    test_hero1.add_ability(test_ability)
    test_hero1.add_ability(test_ability2)
    test_hero1.add_armor(test_armor)
    test_hero1.add_armor(test_armor2)
    their_hero.add_ability(test_ability)
    their_hero.add_ability(test_ability2)
    their_hero.add_armor(test_armor)
    their_hero.add_armor(test_armor2)
    team1 = Team('Team1')
    team2 = Team('Team2')
    team1.add_hero(my_hero)
    team1.add_hero(test_hero1)
    team2.add_hero(their_hero)
    team1.attack(team2)
    



