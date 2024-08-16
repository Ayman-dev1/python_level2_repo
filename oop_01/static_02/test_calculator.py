# main program
from oop_01.static_02.calculator import Calculator

sony_calculator = Calculator('Sony', 'grey', 10, 15)
# total = sony_calculator.add_numbers(5, 6)   # 11

samsung_calculator = Calculator('Samsung', 'white', 20, 7)
# total = samsung_calculator.add_numbers(5, 6)  # 11

total = Calculator.add_numbers(5, 6)   # 11
print(total)