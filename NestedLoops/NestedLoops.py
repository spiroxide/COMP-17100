repeat = True

while repeat:

    start_index = int(input("Enter an integer: "))
    end_index = int(input("Enter another integer: "))

    i = start_index
    if start_index <= end_index:
        while i <= end_index:
            print(i)
            i += 1
    else:
        while i >= end_index:
            print(i)
            i -= 1

    user_action = input("Do you want to do this again (y/n): ")
    if user_action != "y":
        repeat = False


num = int(input("Enter an integer: "))
j = 1
while j <= num:
    i = 0
    while i <= num:
        print(j, end='')
        i += 1
    print()
    j += 1
