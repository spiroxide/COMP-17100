#
#
#


def pig_latin_word(word):
    vowel_index = -1
    for i in range(len(word) - 1, -1, -1):
        if word[i] in "aeiouyAEIOUY":
            vowel_index = i
    if vowel_index == 0:
        return word + "way"
    return word[vowel_index:] + word[:vowel_index] + "ay"


def pig_latin_translator(string):
    words = string.split()
    pig_latin = ""
    for i in words:
        pig_latin += pig_latin_word(i) + ' '
    return pig_latin


def main():
    print(pig_latin_translator("Hello World"))


main()
