
import random 
from attacks import Attack
class Dinosaur:
    def __init__(self):
        self.name = 'T-Rex'
        self.attack_power = random.choice([Attack('slash', 500), Attack('cut', 800), Attack('tailwhip', 900)])
        self.health = 15000
    
    def attack_robot(self, target):
        target.health -= self.attack_power.attack
        print(f'Dinosaur has attacked with {self.attack_power.name} and has ministered {self.attack_power} damage to Robot. Dinosaur has {self.health} left. Robot has {target.health}.')
    
