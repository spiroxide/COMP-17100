print('exercise 1')
i = 1
while i <= 20:
    print(i)
    i += 1

print('exercise 2')
num = int(input("Enter a positive integer: \n"))
i = 1
while i <= num:
    print(i)
    i += 1

print('exercise 3')
num = int(input("Enter a positive integer: \n"))
i = num
while i >= 1:
    print(i)
    i -= 1

print('exercise 4')
num = int(input("Enter a positive integer: \n"))
i = 2
while i <= num:
    print(i)
    i += 2

print('exercise 5')
string = input("Enter a string or enter ”quit” to quit: \n")
while string != "quit":
    print(string)
    string = input("Enter a string or enter ”quit” to quit: \n")

print('exercise 6')
string = input("Enter a string or enter ”quit” to quit: \n")
while string != "quit" and string != "Quit" and string != "QUIT":
    print(string)
    string = input("Enter a string or enter ”quit” to quit: \n")

print('exercise 7')
num = int(input("Enter a positive number: \n"))
while num <= 1:
    num = int(input("Enter a positive number: \n"))

print('exercise 8')
num = int(input("Enter a positive integer: \n"))
total = 0
i = 0
while i <= num:
    total += i
    i += 1
print(total)
