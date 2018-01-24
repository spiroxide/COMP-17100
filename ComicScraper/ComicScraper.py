# Erich Ostendarp
# 11/27/17
#

import urllib.request


def scrape():
    data = urllib.request.urlopen("http://smbc-comics.com/")
    lines = data.readlines()
    for line in lines:
        line = line.decode("utf-8")
        if "ta p" in line:
            start = line.find("t=\"") + 3
            end = line.find("\" /")
            print(line[start:end])
        elif "c='" in line:
            start = line.find("//") + 2
            end = line.find("'>")
            print("http://www." + line[start:end])


def main():
    scrape()


main()
