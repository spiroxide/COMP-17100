# Erich Ostendarp
# 12/5/17
# Simple image editing program.


def save_ppm(original_path, new_path):
    """
    Generates a copy of the ppm at source named name.
    :param original_path: original ppm path
    :param new_path: copied ppm path
    :return: None
    """
    original = open(original_path)
    named = open(new_path, 'w')
    named.writelines(original.readlines())
    original.close()
    named.close()


def readPPM(filename):
    '''
    This functions reads a P3 PPM and returns a list of lists of lists
    containting pixel values. The lists are y, x, and c where c is color channel
    0 for red
    1 for green
    2 for blue
    Args: image name
    Return: 3D list of pixels in [y][x][c] format
    '''
    f = open(filename, "r")
    lines = f.readlines()

    type = lines[0]
    if lines[1][0] == "#":
        offset = 1
    else:
        offset = 0
    size = lines[1 + offset].split()

    width = int(size[0])
    height = int(size[1])
    print("width=", width, " height=", height)

    depth = int(lines[2 + offset])

    image = []
    row = []
    allValues = []
    for i in range(3 + offset, len(lines)):
        temp = lines[i].split()
        for j in range(len(temp)):
            allValues.append(int(temp[j]))
    pixel = []
    for x in range(len(allValues)):
        pixel.append(int(allValues[x]))
        if (len(pixel) == 3):
            row.append(pixel)
            pixel = []
            if (len(row) % width == 0):
                image.append(row)
                row = []
    f.close()

    return image


def writePPM(filename, image):
    '''
    This functions takes a ppm image stored in the format of a 3D list [y][x][c] where
    c is color channel
    0 for red
    1 for green
    2 for blue
    and writes a plain text P3 style PPM image under the name filename
    Args: image name, image data
    Return: none
    '''
    height = len(image)
    width = len(image[0])

    f = open(filename, "w")
    f.write("P3\n")
    f.write(str(width) + " " + str(height) + "\n")
    f.write("255\n")
    for y in range(len(image)):
        for x in range(len(image[y])):
            for c in range(len(image[y][x])):
                f.write(str(image[y][x][c]) + " ")
            f.write("\n")

    f.close()


def vertical_flip(path):
    """
    Generates a ppm of the ppm at path flipped vertically.
    :param path: path of original ppm
    :return: None
    """
    image = readPPM(path)
    flip = image[::-1]
    writePPM("vertical_flip.ppm", flip)


def horizontal_flip(path):
    """
    Generates a ppm of the ppm at path flipped horizontally.
    :param path: path of original ppm
    :return: None
    """
    image = readPPM(path)
    flip = []
    for line in image:
        flip.append(line[::-1])
    writePPM("horizontal_flip.ppm", flip)


# incomplete
def hopify_filter(pixel):
    """
    Generates a ppm of the ppm at path with a hopify filter applied.
    :param path: path of original ppm
    :return: None
    """
    return 0


# incomplete
def checkerboard_filter(pixel):
    """
    Generates a ppm of the ppm at path with a checkerboard filter applied.
    :param path: path of original ppm
    :return: None
    """
    return 0


# incomplete
def check_path():
    """
    Returns a valid path
    :return: valid path
    """
    return 0


# incomplete
def check_option():
    """
    Returns a valid option
    :return: valid option
    """
    return 0


# incomplete
def main():
    vertical_flip("face.ppm")


main()
