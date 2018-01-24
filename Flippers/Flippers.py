from random import *


def coinFlip():
    return randint(1, 2) == 1


def flipper1():
    heads = 0
    for i in range(100):
        if coinFlip():
            heads += 1
    return heads


def flipper2():
    flips = 0

    heads = 0
    while heads < 50:
        flips += 1
        if coinFlip():
            heads += 1
    return flips


def main():
    print(flipper1())
    print(flipper2())


main()
