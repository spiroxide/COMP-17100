def deep_copy(list_in):
    """
    Returns a copy of the input list
    :param list_in: the list to be copied
    :return: a copy of the input list
    """
    return [i for i in list_in]


def main():
    list1 = [1, 1, 2, 3, 5, 8, 13]
    list2 = list1[:]
    list2[len(list2) - 1] = -1
    print(list1)
    print(list2)


main()
