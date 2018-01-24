#
#
#


def to_acronym(string):
    arr = string.split()
    acronym = ""
    for word in arr:
        if word[0].isupper():
            acronym += word[0]
    return acronym


def main():
    print(to_acronym("dingus"))


main()