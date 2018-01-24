from math import *
from random import *

print(int(random() * 6 + 1))

a = float(input("Enter a: "))
b = float(input("Enter b: "))

print(sqrt(pow(a, 2) + pow(b, 2)))

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

print((-b + sqrt(pow(b, 2) - (4 * a * c))) / (2 * a))
print((-b - sqrt(pow(b, 2) - (4 * a * c))) / (2 * a))
