# Erich Ostendarp
# 10/16/17
# Tests a function that finds the larger of 2 numbers


def larger(a, b):
    """
    finds the larger of the 2 numbers
    :param a: a number
    :param b: another number
    :return: the larger number
    """
    if a > b:
        return a
    return b


def main():
    print("Is 1 or 1 larger: ", larger(1, 1))  # Tests when both numbers are the same
    print("Is -3 or 2 larger: ", larger(-3, 2))  # Tests when a number is negative
    print("Is -4 or -7 larger: ", larger(-4, -7))  # Tests when both numbers are negative
    print("Is 8.01 or 8 larger: ", larger(8.01, 8))  # Tests when a number is a float


main()
