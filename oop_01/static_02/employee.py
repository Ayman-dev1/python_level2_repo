# Lets create Emp class
import sys

class Employee:
    # static attributes = class attributes
    __company_bonus = 100_000
    __employees_counter = 0

    # instance attributes [ properties ]
    # constructor
    # self keyword refer to members of the class : attributes or methods ( represent the current object [ instance ] نسخة
    def __init__(self, employee_id, employee_name, employee_gross_salary, employee_job, emp_wallet):
        Employee.__employees_counter = Employee.__employees_counter + 1
        self.__employee_id = employee_id
        self.__employee_name = employee_name
        if employee_gross_salary > 0:
            self.__employee_gross_salary = employee_gross_salary
        else:
            print('Salary cannot be -ve')
            sys.exit()
        self.__employee_job = employee_job
        self.__emp_wallet = emp_wallet

    # Accessors : Getters, Setters
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
            print('Salary cannot be -ve')
            sys.exit()

    def get_emp_wallet(self):
        return self.__emp_wallet
    @staticmethod
    def get_company_bonus():
        return Employee.__company_bonus
    @staticmethod
    def get_employee_counter():
        return Employee.__employees_counter

    # Extra Methods
    def calc_monthly_net_salary(self):
        tax = 10        # local variable
        return self.__employee_gross_salary - self.__employee_gross_salary * tax / 100

    def calc_annual_net_salary(self):
        return self.calc_monthly_net_salary() * 12

    def receive_bonus(self, amount):
        self.__emp_wallet = self.__emp_wallet + amount
        Employee.__company_bonus = Employee.__company_bonus - amount
