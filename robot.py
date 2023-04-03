from weapon import Weapon
import random

class Robot:
    def __init__(self, name_passed):
        self.name = name_passed
        self.active_weapon = random.choice([Weapon('Excalibur', 800), Weapon('Master Sword', 1000), Weapon('Buster Sword', 900), Weapon('screech',100)])
        self.health = 5000
    
    def attack_dinosaur(self, target):
        target.health -= self.active_weapon.attack
        print(f'\n{self.name} has attacked with {self.active_weapon.name} and has ministered {self.active_weapon.attack} damage to {target.name}. \n {self.name} has {self.health} left. {target.name} has {target.health}\n')
    



