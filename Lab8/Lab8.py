# Erich Ostendarp
# 11/27/17
# Scrapes name and netpass information from a website and prints it.

import urllib.request


def scrape(url, names, netpass):
    """
    This function identifies names and corresponding netpass IDs and adds them to
    lists
    Args: a url,an empty list to add names to, and empty list to add netpassIDs to
    Returns: none
    """
    data = urllib.request.urlopen(url)
    lines = data.readlines()
    for line in lines:
        line = line.decode("utf-8")
        if "s.it" in line:
            start_name = line.find("\">") + 2
            end_name = line.find("</")
            names.append(line[start_name:end_name])

            start_id = line.find("u/") + 2
            end_id = line.find("/\"")
            netpass.append(line[start_id:end_id])


def printLogins(name, net):
    """
    Print all of the name and netpass information
    Args: a list of names, a list of netpass IDs
    Return: none
    """
    for i in range(len(name)):
        print(name[i] + ": " + net[i])


def main():
    """
    Run the webscraping function and print results
    Args: none
    Return: none
    """
    net = []
    names = []
    scrape("http://www.ithaca.edu/directories/eportfolios.php", names, net)
    printLogins(names, net)


main()
