class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    # methods
    def calc_area(self):
        return (self.__length + self.__width) * 2

    def calc_perimeter(self):
        return self.__length * self.__width
