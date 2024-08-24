class Person:
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

    def print_person_details(self):
        print('Person id = ', self.__person_id)
        print('Person name = ', self.__person_name)
