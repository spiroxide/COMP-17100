age = int(input("Enter your age: "))

if age >= 18:
    print("You can vote. ", end='')
    if age >= 21:
        print("You can drink.")
else:
    print("You cannot vote. You cannot drink.")
