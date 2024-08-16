import math


class Circle:
    def __init__(self, radius):
        self.__radius = radius

    # methods
    def calc_area(self):
        return math.pi * math.pow(self.__radius, 2)

    def calc_circumference(self):
        return 2 * math.pi * self.__radius
