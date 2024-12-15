from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

favorite_color = Color.GREEN
print("Favorite Color:", favorite_color)
