# lets Create Emp class
import sys


class Emp:
    # attrs [properties]
    # constructor
    def __init__(self, employee_id, employee_name, employee_gross_salary, employee_job):
        self.__employee_id = employee_id
        self.__employee_name = employee_name
        if employee_gross_salary > 0:
            self.__employee_gross_salary = employee_gross_salary
        else:
            print('Salary Cannot be -ve')
            sys.exit()
        self.__employee_job = employee_job

    # Extra Methods

    # Accessors : getters , Setters
    def get_employee_name(self):
        return self.__employee_name

    def set_employee_name(self, employee_name):
        self.__employee_name = employee_name

    def get_employee_gross_salary(self):
        return self.__employee_gross_salary

    def set_employee_gross_salary(self, employee_gross_salary):
        if employee_gross_salary > 0:
            self.__employee_gross_salary = employee_gross_salary
        else:
            print('Salary Cannot be -ve')
            sys.exit()


    def calc_monthly_net_salary(self):
        tax = 10
        return self.__employee_gross_salary - self.__employee_gross_salary * tax / 100

    def calc_annual_net_salary(self):
        return self.calc_monthly_net_salary() * 12
