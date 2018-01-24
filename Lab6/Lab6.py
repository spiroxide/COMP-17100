# Erich Ostendarp
# 10/28/17
# The game "Doubles"

from random import *


def die_roll():
    """
    Simulates rolling a 6 sided die
    :return: a random number between 1 and 6 inclusive
    """
    return int(random() * 6 + 1)


def check_input():
    """
    Makes sure an integer between 1 and 6 is chosen
    :return: a user's number between 1 and 6
    """
    invalid = True
    while invalid:
        value = int(input("Enter an integer between 1 and 6: "))
        if 1 <= value <= 6:
            invalid = False
    return value


def doubles_round(value):
    """
    Simulates 1 round of "Doubles"
    :param value: the value for double rolls to be counted
    :return: the number of double rolls of value
    """
    score = 0
    for rolls in range(100):
        die = die_roll()
        if die == die_roll():
            print("Double")
            if die == value:
                print("You scored a double!")
                score += 1
    print("\nYour score was " + str(score) + " this round.\n")
    return score


def doubles():
    """
    Simulates 3 rounds of "Doubles"
    :return: The largest score between 3 rounds
    """
    score = 0
    for rounds in range(3):
        round_score = doubles_round(check_input())
        if score < round_score:
            score = round_score
    print("Your final score was " + str(score) + ".")
    return score


def main():
    doubles()


main()
