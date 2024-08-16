# main Program
from oop_01.level2_HW.Q3.make_class_employee import Employee

ayman_emp = Employee("ayman", "project owner", 10000)

adel_emp = Employee("adel", "team leader", 8000)

emps_list = [ayman_emp, adel_emp]

total_gross_salary = 0
for item in emps_list:
    print('Emp name = ', item.get_name(), ', net salary before raise = ', item.calc_monthly_net_salary())
    # raise gross salary by 10% for all employees
    current_salary = item.get_salary()
    item.set_salary(current_salary + current_salary * 10 / 100)
    print('Emp name = ', item.get_name(), ', net salary after raise = ', item.calc_monthly_net_salary())
    total_gross_salary = total_gross_salary + item.get_salary()
    print('------')
