# name: Erich Ostendarp
# date: 9/19/17
# purpose: To find the number of 1 gallon paint cans needed to paint the sides of a house with gables.

length = float(input("Enter the length of your house: "))
width = float(input("Enter the width of your house: "))
height = float(input("Enter the height of your house: "))
gable_height = float(input("Enter the gable height of your house: "))

wall_area = 2 * (length * height) + 2 * (height * width)

gable_area = width * gable_height

total_area = wall_area + gable_area

gallons_paint = total_area / 400

# rounds gallons of paint up to the nearest integer
total_cans = 0
if gallons_paint >= int(gallons_paint):
    total_cans = int(gallons_paint) + 1

print("\nThe total surface area of the sides is: " + str(total_area) +
      "\nThe total number of gallons of paint are: " + str(total_cans))
