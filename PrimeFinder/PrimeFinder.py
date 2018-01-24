from math import *
from time import *


def is_prime(num):
    if num % 2 == 0:
        return False

    for i in range(3, ceil(sqrt(num)), 2):
        if num % i == 0:
            return False
    return True


def prime_finder(num):
    initial_time = time()
    num_prime = 0
    i = 2
    while num_prime < num:
        if is_prime(i):
            print(i)
            num_prime += 1
        i += 1
    print(time() - initial_time)


def main():
    prime_finder(1000)


main()
