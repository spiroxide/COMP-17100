# Erich Ostendarp
# 10/14/17
# Custom add, division and sales price functions.


def add(num1, num2):
    """
    adds num1 and num2
    :param num1: a number to add
    :param num2: another number to add
    :return: the sum of num1 and num2
    """
    return num1 + num2


def safeDiv(num1, num2):
    """
    divides num1 and num2
    :param num1: the dividend
    :param num2: the divisor
    :return: the quotient of num1 and num2
    """
    if num2 == 0:
        return 0
    return num1 / num2


def salePrice(normPrice, percentOff):
    """
    finds the actual price of an item given its normal price and its percent off
    :param normPrice: normal price of the item
    :param percentOff: the discount on the item
    :return: the actual price of the item
    """
    if normPrice < 0 or percentOff < 0:
        return -1
    return normPrice - (normPrice * percentOff / 100)


def main():
    print("3 + 6 = ", add(3, 6))  # Tests if add works with integers
    print("-12 + 7 = ", add(-12, 7))  # Tests if add works with 1 negative number
    print("-12 + -7 = ", add(-12, -7))  # Tests if add works with 2 negative numbers
    print("1.234 + 5.678 = ", add(1.234, 5.678))  # Tests if add works with floating point numbers
    print()

    print("14 / 7 = ", safeDiv(14, 7))  # Tests if safeDiv works with integers
    print("-3 / 4 = ", safeDiv(-3, 4))  # Tests if safeDiv works with 1 negative number
    print("-3 / -4 = ", safeDiv(-3, -4))  # Tests if safeDiv works with 2 negative numbers
    print("1.234 / 5.678 = ", safeDiv(1.234, 5.678))  # Tests if safeDiv works with floating point numbers
    print("11 / 0 = ", safeDiv(11, 0))  # Tests if safeDiv handles a divide by 0
    print()

    print("A $200 item with a 10% discount = $", salePrice(200, 10))  # Tests if salePrice works with integers
    print("A $0 item with a 5% discount = $", salePrice(0, 5))  # Tests if salePrice works with a 0 normal price
    print("A $60 item with a 0% discount = $", salePrice(60, 0))  # Tests if salePrice works with a 0 percent off
    print("A $-100 item with a 5% discount = ", salePrice(-100, 5))  # Tests if salePrice handles a negative normal price
    print("A $60 item with a -15% discount = ", salePrice(60, -15))  # Tests if salePrice handles a negative percent off
    print("A $1.234 item with a 5.678% discount = $", salePrice(1.234, 5.678))  # Tests if salePrice works with floating point numbers


main()
