'''
    A program that allows a set of pre-registered users to vote on their cusisine preference
    4/3/2017
    Author(s): Sharon Stansfield, Paul, Dickson, Toby Dragon, Erich Ostendarp
'''


def findVoter(registeredVoters, name):
    """
    Returns True if name is in registeredVoters and False otherwise
    :param registeredVoters: list of registered voters
    :param name: person you are checking is in registeredVoters
    :return: True if name is in registeredVoters and False otherwise
    """
    for i in range(len(registeredVoters)):
        if registeredVoters[i] == name:
            return True
    return False


def addToVoted(name, alreadyVotedList):
    """
    Adds name to alreadyVotedList
    :param name: person to add to alreadyVotedList
    :param alreadyVotedList: list of people who already voted
    :return: None
    """
    alreadyVotedList.append(name)


def processVote(voteCount, votedIndex):
    """
    Increments the vote of voteCount at votedIndex
    :param voteCount: list of votes on cuisines
    :param votedIndex: index of the cuisine that is incremented
    :return: None
    """
    voteCount[votedIndex] += 1


def findWinner(voteCount):
    """
    Returns the index of the cuisine with the highest number of votes
    :param voteCount: the list of votes on cuisines
    :return: the index of the cuisine with the highest number of votes
    """
    maxIndex = 0
    for i in range(1, len(voteCount)):
        if voteCount[maxIndex] < voteCount[i]:
            maxIndex = i
    return maxIndex


def main():
    # all registered voters are listed here, only they may vote
    registeredVoters = ["Allen", "Carlson", "Black", "Jones", "Smith", "Johnson", "Stevens",
                        "Hernandez", "Park", "Chen", "Matino", "Fellini", "Gates", "Williams"]
    # all cuisines are lists here, in the order they will be presented to voters
    cuisines = ["American", "Cajun", "Chinese", "French", "Greek",
                "Indian", "Italian", "Janpanese", "Mexican", "Morroccan", "Thai"]
    # there are 0 votes for each cuisine to start
    voteCount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # no one has already voted
    alreadyVotedList = []

    anotherVoter = "y"
    while anotherVoter == "y":
        name = input("Please enter your last name: ")

        registered = findVoter(registeredVoters, name)
        if registered:

            alreadyVoted = findVoter(alreadyVotedList, name)
            if not alreadyVoted:
                addToVoted(name, alreadyVotedList)

                print("Please vote for your favorite cuisine:")
                for index in range(len(cuisines)):
                    # print numbers starting at 1, not 0
                    print(index + 1, " - ", cuisines[index])

                vote = int(input("Enter the number corresponding to your choice: "))
                while (vote <= 0 or vote >= 12):
                    vote = int(input("Invalid Input.  Enter the number corresponding to your choice: "))

                votedIndex = vote - 1  # get the index by subtracting the 1 added during printout
                processVote(voteCount, votedIndex)
            else:
                print("Denied. You can't vote more than once.")
        else:
            print("Denied. You must be registered to vote.")

        anotherVoter = input("Is there another voter (y): ")

    # find the winner and print the winning cuisine
    winner = findWinner(voteCount)
    print("The winner is", cuisines[winner])


# run the program
main()