class Employee:
    def __init__(self, name, position, salary):
        self.__name = name
        self.__position = position
        self.__salary = salary

    # Accessors : getters , Setters
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def calc_monthly_net_salary(self):
        tax = 10
        return self.__salary - self.__salary * tax / 100
