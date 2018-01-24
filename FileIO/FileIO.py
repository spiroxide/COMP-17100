import urllib.request


def readFile(filename):
    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    return lines


def main():
    html = urllib.request.urlopen("https://xkcd.com/")
    lines = html.readlines()
    found = False
    while not found:
        for line in lines:
            line = line.decode("utf-8")
            if "Permanent" in line:
                print(line[30:52])
                found = True


main()
