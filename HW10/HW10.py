# name: Erich Ostendarp
# date: 10/2/17

i = 1
while i <= 3:
    print(i)
    j = 1
    while j <= i:
        print('+')
        j += 1
    i += 1

print()

i = 1
while i <= 5:
    j = 1
    while j <= i:
        print('*', end='')
        j += 1
    print()
    i += 1
