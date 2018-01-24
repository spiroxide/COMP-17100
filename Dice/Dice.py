from random import *


def roll_six_sided_die():
    """
    rolls a number between 1 and 6
    :return: number (int 1 - 6)
    """
    return int(random() * 6) + 1


def roll_die(sides):
    """
    rolls a die with a user defined number of sides
    :param sides: number of die sides
    :return: number (int 1 - sides)
    """
    return int(random() * sides) + 1


def main():
    print(roll_six_sided_die())
    print(roll_die(13))


main()
