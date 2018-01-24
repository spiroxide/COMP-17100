from Functions import *


def main():
    fahrenheit = float(input("Enter a fahrenheit temperature: "))
    print(fahrenheit_to_celsius(fahrenheit))
    celsius = float(input("Enter a celsius temperature: "))
    print(celsius_to_fahrenheit(celsius))


main()
