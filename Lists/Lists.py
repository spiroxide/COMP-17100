from math import log10


def multi_table(length):
    arr = [[i * j for i in range(1, length + 1)] for j in range(1, length + 1)]
    for i in arr:
        for j in i:
            print(j, end=' ' * (int(log10(length ** 2)) - int(log10(j)) + 1))
        print()


def main():
    multi_table(50)


main()
