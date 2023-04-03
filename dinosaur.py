
import random 
from attacks import Attack
class Dinosaur:
    def __init__(self, name_passed):
        self.name = name_passed
        self.attack_power = random.choice([Attack('slash', 500), Attack('cut', 800), Attack('tailwhip', 900), Attack('roar', 100)])
        self.health = 10000
    
    def attack_robot(self, target):
        target.health -= self.attack_power.attack
        print(f'\n{self.name} has attacked with {self.attack_power.name} and has ministered {self.attack_power.attack} damage to {target.name}. \n {self.name} has {self.health} left. {target.name} has {target.health}.\n')
    
