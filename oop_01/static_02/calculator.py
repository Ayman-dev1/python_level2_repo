class Calculator:
    # attrs inside constructor
    def __init__(self, model, color, length, width):
        self.__model = model
        self.__color = color
        self.__length = length
        self.__width = width

    # accessors
    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    # extra methods : These methods donot depend on instance attributes
    @staticmethod  # decorator
    def add_numbers(a, b):
        return a + b

    @staticmethod
    def subtract_number(a, b):
        return a - b
