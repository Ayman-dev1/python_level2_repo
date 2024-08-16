from oop_01.inheritance_03.person import Person

class Manager(Person):
    def __init__(self, person_id, person_name, person_gross_salary, person_job, profit_percentage):
        super().__init__(person_id, person_name, person_gross_salary, person_job)
        self.__profit_percentage = profit_percentage

    # accessors
    def get_profit_percentage(self):
        return self.__profit_percentage

    # extra methods
    def calc_monthly_net_salary(self):
        tax = 10
        return self._person_gross_salary - self._person_gross_salary * tax / 100

    def calc_annual_net_salary(self):
        return self.calc_monthly_net_salary() * 12

    def calc_annual_net_salary_profit(self, company_profit):
        return self.calc_annual_net_salary() + company_profit * self.__profit_percentage / 100