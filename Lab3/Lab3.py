# name: Erich Ostendarp
# date: 9/26/17
# purpose: Take a customer's order allowing them to pick an alcoholic beverage if older than 21 and prints the order

age = int(input("Enter your age: \n"))

entree = "salad"

answer = int(input("Enter 1 for fish and vegetables, 2 for steak and potatoes or 3 for burger and fries: \n"))
if answer == 1:
    entree = "fish and vegetables"
elif answer == 2:
    entree = "steak and potatoes"
else:
    entree = "burger and fries"

drink = "water"

if entree == "fish and vegetables":
    drink = "iced tea"
    if age >= 21:
        if int(input("Enter 1 for iced tea or 2 for white wine: \n")) == 2:
            drink = "white wine"
elif entree == "steak and potatoes":
    drink = "lemonade"
    if age >= 21:
        if int(input("Enter 1 for lemonade or 2 for red wine: \n")) == 2:
            drink = "red wine"
else:
    drink = "cola"
    if age >= 21:
        if int(input("Enter 1 for cola or 2 for beer: \n")) == 2:
            drink = "beer"

print("Your order is " + entree + " with " + drink)
