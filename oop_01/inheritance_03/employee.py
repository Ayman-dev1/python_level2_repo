from oop_01.inheritance_03.person import Person


class Employee(Person):
    def __init__(self, person_id, person_name, person_gross_salary, person_job, over_time_hours, over_time_rate):
        # call the parent constructor from the child constructor using super() keyword
        super().__init__(person_id, person_name, person_gross_salary, person_job)
        self.__over_time_hours = over_time_hours
        self.__over_time_rate = over_time_rate

    # accessors
    def get_over_time_hours(self):
        return self.__over_time_hours

    def get_over_time_rate(self):
        return self.__over_time_rate

    # Extra Methods
    def calc_monthly_net_salary(self):
        tax = 10
        return (self._person_gross_salary - self._person_gross_salary * tax / 100
                + self.__over_time_hours * self.__over_time_rate)

    def calc_annual_net_salary(self):
        return self.calc_monthly_net_salary() * 12

    # Method Overriding
    def print_person_details(self):
        # I need to call function from the parent class
        super().print_person_details()
        print('Monthly net salary =', self.calc_monthly_net_salary())
        print('Annual net salary = ', self.calc_annual_net_salary())

    def calc_expenses(self):
        print('This is Expenses function in Employee class')
