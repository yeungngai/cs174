import random


class Die:
    def __init__(self, number_of_sides):
        self.sides = number_of_sides

    def roll(self):
        return random.randint(1, self.sides)


def main():
    d6 = Die(6)  # An object is created
    print(d6.roll())
    d20 = Die(20)
    print(d20.roll())
    d8 = Die(8)
    print(d8.roll())


main()
