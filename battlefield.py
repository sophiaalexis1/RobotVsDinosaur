from dinosaur import Dinosaur
from robot import Robot

class Battlefield(Robot, Dinosaur):
    def __init__(self):
        self.dinosaur1 = Dinosaur('Tyrannosaurus')
        self.dinosaur2 = Dinosaur('Allosaurus')
        self.dinosaur3 = Dinosaur('Deinonychus')
        self.robot1 = Robot('R2-D2')
        self.robot2 = Robot('Johnny 5')
        self.robot3 = Robot('Optimus Prime')

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
    
    def display_welcome(self):
        print('\nWelcome to an epic battle for the ages! \n Only one side can win!\n')

    def battle_phase(self):
        while self.robot1.health > 0 and self.robot2.health > 0 and self.robot3.health > 0 and self.dinosaur1.health > 0 and self.dinosaur2.health>0 and self.dinosaur3.health > 0:
            self.robot1.attack_dinosaur(self.dinosaur1)
            self.robot2.attack_dinosaur(self.dinosaur2)
            self.robot3.attack_dinosaur(self.dinosaur3)
            self.dinosaur1.attack_robot(self.robot1)
            self.dinosaur2.attack_robot(self.robot2)
            self.dinosaur3.attack_robot(self.robot3)
        return

    def display_winner(self):
        if self.robot1.health > 0 and self.robot2.health > 0 and self.robot3.health > 0 and self.dinosaur1.health <= 0 and self.dinosaur2.health <= 0 and self.dinosaur3.health <= 0:
            print('Robot wins the game!')
        elif self.robot1.health > 0 and self.robot2.health >= 0 and self.robot3.health >= 0 and self.dinosaur1.health <= 0 and self.dinosaur2.health <= 0 and self.dinosaur3.health <= 0:
            print('Robot wins the game!')
        elif self.robot1.health >= 0 and self.robot2.health > 0 and self.robot3.health >= 0 and self.dinosaur1.health <= 0 and self.dinosaur2.health <= 0 and self.dinosaur3.health <= 0:
            print('Robot wins the game!')
        elif self.robot1.health >= 0 and self.robot2.health >= 0 and self.robot3.health > 0 and self.dinosaur1.health <= 0 and self.dinosaur2.health <= 0 and self.dinosaur3.health <= 0:
            print('Robot wins the game!')
        elif self.robot1.health <= 0 and self.robot2.health <= 0 and self.robot3.health <= 0 and self.dinosaur1.health > 0 and self.dinosaur2.health > 0 and self.dinosaur3.health > 0:
            print('Dinosaur wins the game!')
        elif self.robot1.health <= 0 and self.robot2.health <= 0 and self.robot3.health <= 0 and self.dinosaur1.health > 0 and self.dinosaur2.health >= 0 and self.dinosaur3.health >= 0:
            print('Dinosaur wins the game!')
        elif self.robot1.health <= 0 and self.robot2.health <= 0 and self.robot3.health <= 0 and self.dinosaur1.health >= 0 and self.dinosaur2.health > 0 and self.dinosaur3.health >= 0:
            print('Dinosaur wins the game!')
        elif self.robot1.health <= 0 and self.robot2.health <= 0 and self.robot3.health <= 0 and self.dinosaur1.health >= 0 and self.dinosaur2.health >= 0 and self.dinosaur3.health > 0:
            print('Dinosaur wins the game!')
        elif self.robot1.health <= 0 and self.robot2.health <= 0 and self.robot3.health <= 0 and self.dinosaur1.health <= 0 and self.dinosaur2.health <= 0 and self.dinosaur3.health <= 0:
            print('It is a tie!')
        return