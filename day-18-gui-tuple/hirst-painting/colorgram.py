"""
Exctract color from image using colorgram library
"""

import colorgram

colors = colorgram.extract('image.jpg', 10)
rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)