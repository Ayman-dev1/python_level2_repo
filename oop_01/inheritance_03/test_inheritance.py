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
