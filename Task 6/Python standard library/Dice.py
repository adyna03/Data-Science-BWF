# Class
from random import randint
x = randint(1, 6)

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return random.randint(1, self.sides)

six_sided_die = Die()
for _ in range(10):
    result = six_sided_die.roll_die()
    print(f"6-sided die roll: {result}")

ten_sided_die = Die(10)
for _ in range(10):
    result = ten_sided_die.roll_die()
    print(f"10-sided die roll: {result}")

twenty_sided_die = Die(20)
for _ in range(10):
    result = twenty_sided_die.roll_die()
    print(f"20-sided die roll: {result}")
