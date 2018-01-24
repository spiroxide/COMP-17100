from math import *
# name: Erich Ostendarp
# date: 10/16/17
# purpose: To find the number of 1 gallon paint cans needed to paint the sides of a house with gables.


def cans_of_paint(length, width, height, gable_height):
    """
    finds the number of 1 gallon cans of paint needed to paint a house
    :param length: the length of the house
    :param width: the width of the house
    :param height: the height of the house
    :param gable_height: the height of the gables
    :return: the number of 1 gallon cans of paint needed to paint the house
    """
    wall_area = 2 * (length * height) + 2 * (height * width)
    gable_area = width * gable_height
    total_area = wall_area + gable_area
    gallons_paint = total_area / 400
    return ceil(gallons_paint)


def main():
    length = float(input("Enter the length of your house: "))
    width = float(input("Enter the width of your house: "))
    height = float(input("Enter the height of your house: "))
    gable_height = float(input("Enter the gable height of your house: "))

    print(cans_of_paint(length, width, height, gable_height))
