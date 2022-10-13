import random
import colorgram


def colorgram_colors():
    colors = colorgram.extract("img.jpg", 20)
    rgb_colors = []

    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        rgb_colors.append((r, g, b))

    return rgb_colors


def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    color = (r, g, b)
    return color
