# name: Erich Ostendarp
# date: 10/4/17

num = int(input("Enter an integer: "))

i = 1
while i <= num:

    # prints spaces before stars
    j = num - i
    while j >= 1:
        print(' ', end='')
        j -= 1

    # prints starts
    k = 1
    while k <= (i * 2) - 1:
        print('*', end='')
        k += 1

    print()
    i += 1
