# main program
from oop_01.basics_01.emp import Emp

# create object emp_ahmed from Emp class
emp_ahmed = Emp(101, 'Ahmed Hesham', 9000, "tester")
# print('name = ', emp_ahmed.employee_name)
print('name = ', emp_ahmed.get_employee_name())
emp_ahmed.set_employee_gross_salary(-7000)
print("Ahmed Monthly net salary = ", emp_ahmed.calc_monthly_net_salary())
print('Ahmed Annual net salary = ', emp_ahmed.calc_annual_net_salary())
print('----------------------------------')
#create object emp_marwa from Emp class
emp_marwa = Emp(102, 'Marwa Adel', 30000, 'Markter')
# print('name = ', emp_marwa.employee_name)
print('Name =', emp_marwa.get_employee_name())
print('Marwa gross salary = ', emp_marwa.get_employee_gross_salary())
print("marwa Monthly net salary = ", emp_marwa.calc_monthly_net_salary())
print('marwa Annual net salary = ', emp_marwa.calc_annual_net_salary())

# create object emp_usama from Emp class
emp_usama = Emp(103, 'Usama Zayed', 9000, 'Salesman')

# create object emp_noura from Emp class
emp_noura = Emp(104, 'Noura Ahmed', 8000, 'Secretary')

print("----------- List of objects -------------")

emps_list = [emp_ahmed, emp_marwa, emp_usama, emp_noura]
emps_list.append(Emp(105, 'Ibrahim Salah', 15000, 'P.M'))
print(len(emps_list))
# print(emps_list)        # no benefit
print('Gross salary of Marwa = ', emp_marwa.get_employee_gross_salary(), emps_list[1].get_employee_gross_salary())


print('-- Loop over emps List and print all names, net salary -----')

total_gross_salary = 0
for item in emps_list:
    print('Emp name = ', item.get_employee_name(), ', net salary before raise = ', item.calc_monthly_net_salary())
    # raise gross salary by 10% for all employees
    current_salary = item.get_employee_gross_salary()
    item.set_employee_gross_salary(current_salary + current_salary * 10 / 100)
    print('Emp name = ', item.get_employee_name(), ', net salary after raise = ', item.calc_monthly_net_salary())
    total_gross_salary = total_gross_salary + item.get_employee_gross_salary()
    print('------')

print('Total gross salary after raise = ', total_gross_salary)
