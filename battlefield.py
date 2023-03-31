from dinosaur import Dinosaur
from robot import Robot 
valid_response = False
class Battlefield(Robot, Dinosaur):
    def __init__(self):
        self.dinosaur = Dinosaur()
        self.robot = Robot()

    def run_game(self):
        display_welcome(self)
        battle_phase()
        display_winner()
    
    def display_welcome(self):
        print('\nWelcome to an epic battle for the ages! \n Only one side can win!\n')

    def battle_phase(self):
        while self.robot.health > 0 and self.dinosaur.health > 0:
            self.robot.attack_dinosaur(Dinosaur)
            self.dinosaur.attack_robot(Robot)
        return

    def display_winner(self):
        if self.robot.health > 0 and self.dinosaur.health <= 0:
            print('Robot wins the game!')
        elif self.robot.health <= 0 and self.dinosaur.health > 0:
            print('Dinosaur wins the game!')
        elif self.robot.health <= 0 and self.dinosaur.health <= 0:
            print('It is a tie!')
        return