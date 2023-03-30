class Weapon:
    def __init__(self, name_passed):
        # self.exc = self.Excalibur
        # self.ma = self.Master_Sword
        self.name = name_passed
        self.attack = 1000

    def show(self):
        print('Name:', self.name)

    class Excalibur:
        def __init__(self):
            self.name = 'Exalibur'
            self.attack_power = 2500
        
        def display(self):
            print('Weapon:', self.name)
    
    class Master_Sword:
        def __init__(self):
            self.name = 'Master Sword'
            self.attack_power = 3000
        
        def display(self):
            print('Weapon:', self.name)
