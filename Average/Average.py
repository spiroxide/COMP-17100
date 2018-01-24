total = 0
count = 0
x = input("Enter number to average or enter \"done\":\n")
minimum = float(x)
maximum = float(x)
while x != "done":
    total += float(x)
    count += 1

    if float(x) < minimum:
        minimum = float(x)
    elif float(x) > maximum:
        maximum = float(x)

    x = input("Enter number to average or enter \"done\":\n")

print("sum: " + str(total / count))
print("max: " + str(maximum) + " min: " + str(minimum))
