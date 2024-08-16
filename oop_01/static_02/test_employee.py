# main program
from oop_01.static_02.employee import Employee

# create object emp_ahmed from Emp class
emp_ahmed = Employee(101, 'Ahmed Hesham', 7000, 'Programmer', 0)

print('-----------------------------')
# create object emp_marwa from Emp class
emp_marwa = Employee(102, 'Marwa Omar', 5000, 'Marketer', 0)

print('Ahmed wallet = ', emp_ahmed.get_emp_wallet())        # 0
print('Company bonus = ', Employee.get_company_bonus())     # 100_000

print('--- Ahmed receive 5000 egp ----')
emp_ahmed.receive_bonus(5000)

print('Ahmed wallet = ', emp_ahmed.get_emp_wallet())        # 5000
print('Company bonus = ', Employee.get_company_bonus())     # 95_000

print('--- Marwa receive 10000 egp ----')
emp_marwa.receive_bonus(10_000)
print('Marwa Wallet = ', emp_marwa.get_emp_wallet())        # 10000
print('Company bonus = ', Employee.get_company_bonus())     # 85_000

emp_usama = Employee(103, 'Usama', 9000, 'Sales', 0)
print('Number of Employees objects Created = ', Employee.get_employee_counter())