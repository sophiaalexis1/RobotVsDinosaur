from weapon import Weapon

weapons = ['Excalibur', 'Master_Sword']
class Robot(Weapon):
    def __init__(self, name_passed):
        self.name = name_passed
        self.active_weapon = Weapon('sword')
        self.health = 10000
    
    def attack_dinosaur(self, dinosaur):
        dinosaur.health -= self.active_weapon
        print(f'Robot has attacked and has ministered {self.active_weapon.attack} damage to Dinosaur. Robot has {self.health} left. Dinosaur has {dinosaur.health}')
    



robot_one = Robot('Arthur')
print(robot_one.name, robot_one.health, robot_one.active_weapon)
# dinosaur_to_attack = 10000

# robot_one.attack_dinosaur(dinosaur_to_attack)

