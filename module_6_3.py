import random
from random import randint
class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0,0,0]
        self.speed = speed

    def move(self, dx, dy, dz):
        new_z = dz * self.speed
        if new_z < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords = [dx * self.speed, dy * self.speed, new_z]

    def get_cords(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER > 5:
            print("Sorry, i'm peaceful")
        else:
            print("Be careful, i'm attacking you O_O")


class Bird(Animal):
    beak = True
    random_eggs = random.randint(1,4)
    def lay_eggs(self):
        print(f'Here are(is) {self.random_eggs} eggs for you')

class Aquatic_Animal(Animal):
    _DEGREE_OF_DANGER = 3
    def dive_in(self, dz):
        dz = abs(dz)
        new_z = int(dz * (self.speed / 2) * -1)
        if new_z + self._cords[2] < 0:
            self._cords[2] = 0
        else:
            self._cords[2] += new_z


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, Aquatic_Animal, PoisonousAnimal):
    def sound(self):
        print('Click-click-click')

db = Duckbill(10)

print(db.live)
print(db.beak)

db.sound()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()
