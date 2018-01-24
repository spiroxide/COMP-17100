# Erich Ostendarp
# 12/1/17
#


def map_range(f_val, f_start, f_end, t_start, t_end):
    """

    :param f_val:
    :param f_start:
    :param f_end:
    :param t_start:
    :param t_end:
    :return:
    """
    return (t_end - t_start) / (f_end - f_start) * (f_val - f_start) + t_start


def generate_ppm():
    color = open("color.ppm", 'r')
    greyScale = open("greyScale.ppm", 'w')
    color.readline()
    width = int(color.readline())
    height = int(color.readline())
    greyScale.write("P3\n" + str(width) + '\n' + str(height) + "\n255\n")
    color.readline()
    for i in range(width * height):
        rgb = color.readline().split(' ')
        r = int(rgb[0])
        g = int(rgb[1])
        b = int(rgb[2])
        average = int((r + g + b) / 3)
        greyScale.write(str(average) + ' ' + str(average) + ' ' + str(average) + "\n")


def main():
    generate_ppm()


main()
