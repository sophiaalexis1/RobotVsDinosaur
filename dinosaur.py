
class Dinosaur:
    def __init__(self):
        self.name = 'T-Rex'
        self.attack_power = 15000
        self.health = 10000
    
    def attack_robot(self, target):
        self.target = Robot()
        self.target.health -= self.attack_power
        print(f'Dinosaur has attacked and has ministered {self.attack_power} damage to Robot. Dinosaur has {self.health} left. Robot has {self.target.health}.')
    
rex = Dinosaur()
print(rex.health)