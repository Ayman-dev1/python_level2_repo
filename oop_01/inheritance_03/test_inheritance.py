# main program
from oop_01.inheritance_03.employee import Employee
from oop_01.inheritance_03.manager import Manager

print('----- Employee object ------')
# Create object ? Employee or Person ?  We always create object from the child
emp_ahmed = Employee(101, 'Ahmed Omar', 9000, 'Programmer', 10, 20)
print('Monthly net salary = ', emp_ahmed.calc_monthly_net_salary())
print('Annual net salary = ', emp_ahmed.calc_annual_net_salary())

print('----- Manager object ------')
mgr_khaled = Manager(401, 'Khaled Aly', 15000, 'Project Manager', 10)
print('Monthly net salary = ', mgr_khaled.calc_monthly_net_salary())  # 13500
print('Annual net salary = ', mgr_khaled.calc_annual_net_salary())  # 162000
company_profit = 1_000_000.00
print('Annual net salary with profit = ', mgr_khaled.calc_annual_net_salary_profit(company_profit))  # 262000

print('-------Check for Method Overriding ------')
emp_ahmed.print_person_details()

print('-------- Check for Polymorphism --------')


def print_data_for_all(person):
    if isinstance(person, Employee):
        print('This is an employee object')
        print('person id = ', person.get_person_id())
        print('monthly net salary = ', person.calc_monthly_net_salary())
        print('--------')
    else:
        print('This is a manager object')
        print('person id = ', person.get_person_id())
        print('monthly net salary = ', person.calc_monthly_net_salary())
        print('--------')


# test Main program - call the function
print_data_for_all(emp_ahmed)
print_data_for_all(mgr_khaled)


print('------ Check For Abstraction -------')
emp_ahmed.calc_expenses()
mgr_khaled.calc_expenses()