class Dinosaur:
    def __init__(self, name_passed, attack_power):
        self.name = name_passed
        self.attack_power = attack_power
        self.health = 10000
    
    def attack_robot(self, robot):
        robot -= self.attack_power
        print(f'Dinosaur has attacked and has ministered {self.attack_power} damage to Robot. Dinosaur has {self.health} left.')
    
# t_rex = Dinosaur('T-Rex', 1000)
# print (t_rex.name, t_rex.attack_power, t_rex.health)

# robot_to_attack = 10000

# t_rex.attack_robot(robot_to_attack)