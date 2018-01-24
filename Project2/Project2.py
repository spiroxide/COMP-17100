# Erich Ostendarp
# 11/8/17
# A game of hangman


def check_character(prompt):
    """
    Checks that a single letter is entered.
    :param prompt: prompt asking for input
    :return: a single letter
    """
    character = input(prompt).lower()
    if len(character) != 1:
        character = check_character("You must enter a single letter: ")
    elif character not in "abcdefghijklmnopqrstuvwxyz":
            character = check_character("You must enter a letter: ")
    return character


def check_word(prompt):
    """
    Checks that a single word is entered.
    :param prompt: prompt asking for input
    :return: a single word
    """
    word = input(prompt).lower()
    for character in word:
        if character not in "abcdefghijklmnopqrstuvwxyz":
            word = check_word("You must enter a single word: ")
    return word


def to_string(arr):
    """
    returns a string of characters from arr
    :param arr: a list of characters
    :return: a string of characters from arr
    """
    word = ""
    for i in arr:
        word += i
    return word


def hangman(word):
    """
    A game of hangman.
    :param word: word to guess
    :return: None
    """
    man = ["head", "body", "left arm", "right arm", "left leg", "right leg\nYou lose"]  # keeps track of current body part
    man_index = 0
    hidden_word = ["_" for i in range(len(word))]  # keeps track of guessed and hidden letters
    print("Welcome to the game of Hangman. Here is your word:\n" + to_string(hidden_word))

    while man_index < len(man) and to_string(hidden_word) != word:
        character = check_character("Guess a letter: ")
        if character in word:
            for i in range(len(word)):
                if character == word[i]:
                    hidden_word[i] = character
            print(to_string(hidden_word))
            if to_string(hidden_word) == word:
                print("You win!")
        else:
            print("draw body part: " + man[man_index])
            man_index += 1


def main():
    word = check_word("Enter a word: ")
    hangman(word)


main()
