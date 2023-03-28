from weapon import Weapon

weapons = ['Excalibur', 'Master_Sword']
class Robot(Weapon):
    def __init__(self, name_passed):
        self.name = name_passed
        self.active_weapon = Weapon()
        self.health = 10000
    
    def attack_dinosaur(self, dinosaur):
        dinosaur -= self.active_weapon
        print(f'Robot has attacked and has ministered {Weapon} damage to Dinosaur. Robot has {self.health} left.')
    



robot_one = Robot('Arthur')
robot_one.attack_weapon.append(Weapon())
print(robot_one.name, robot_one.health, robot_one.attack_weapon)
dinosaur_to_attack = 10000

robot_one.attack_dinosaur(dinosaur_to_attack)

