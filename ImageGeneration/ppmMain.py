from readwritePPM import *


def grey_scale():
    file = readPPM("face.ppm")

    image = []
    for x in range(len(file)):
        row = []
        for y in range(len(file[x])):
            pixel = []
            average = int((file[x][y][0] + file[x][y][1] + file[x][y][2]) / 3)
            for rgb in range(len(file[x][y])):
                pixel.append(average)
            row.append(pixel)
        image.append(row)

    writePPM("grey_scale.ppm", image)


def invert():
    file = readPPM("face.ppm")

    image = []
    for x in range(len(file)):
        row = []
        for y in range(len(file[x])):
            pixel = []
            for rgb in range(len(file[x][y])):
                pixel.append(255 - file[x][y][rgb])
            row.append(pixel)
        image.append(row)

    writePPM("inverted.ppm", image)


def flip_horizontaly():
    file = readPPM("face.ppm")
    flip = []
    for x in range(len(file)):
        row = []
        for y in range(len(file[x])):
            pixel = []
            for rgb in range(len(file[x][y][rgb])):

    writePPM("flipped.ppm", )


def main():
    grey_scale()
    invert()
    flip_horizontaly()


main()
