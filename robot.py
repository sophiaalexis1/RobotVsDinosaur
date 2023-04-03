from weapon import Weapon
import random
weapons = ['Excalibur', 'Master_Sword']

class Robot:
    def __init__(self):
        self.name = 'Arthur'
        self.active_weapon = random.choice([Weapon('Excalibur', 500), Weapon('Master Sword', 900), Weapon('Buster Sword', 800)])
        self.health = 15000
    
    def attack_dinosaur(self, target):
        target.health -= self.active_weapon.attack
        print(f'Robot has attacked with {self.active_weapon.name} and has ministered {self.active_weapon.attack} damage to Dinosaur. Robot has {self.health} left. Dinosaur has {target.health}')
    



