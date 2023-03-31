from weapon import Weapon

weapons = ['Excalibur', 'Master_Sword']
class Robot(Weapon):
    def __init__(self):
        self.name = 'Arthur'
        self.active_weapon = Weapon('Excalibur')
        self.health = 10000
    
    def attack_dinosaur(self):
        self.target = Dinosaur() 
        self.target.health -= self.active_weapon
        print(f'Robot has attacked and has ministered {self.active_weapon.attack} damage to Dinosaur. Robot has {self.health} left. Dinosaur has {self.target.health}')
    



