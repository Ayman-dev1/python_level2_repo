from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, person_id, person_name, person_gross_salary, person_job):
        self.__person_id = person_id
        self.__person_name = person_name
        self._person_gross_salary = person_gross_salary
        self.__person_job = person_job

    # Accessors
    def get_person_id(self):
        return self.__person_id

    def get_person_name(self):
        return self.__person_name

    def get_person_gross_salary(self):
        return self._person_gross_salary

    def get_person_job(self):
        return self.__person_job

    # method Overriding
    def print_person_details(self):
        print('Person id = ', self.__person_id)
        print('Person name = ', self.__person_name)

    # Creating Abstract function : function in abstract class, without body, must be implemented in all children
    @abstractmethod
    def calc_expenses(self):
        pass
