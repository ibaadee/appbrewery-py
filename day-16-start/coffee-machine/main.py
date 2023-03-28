from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

is_on = True

while is_on :
    command = input(f'what do you like? ({menu.get_items()}):\n')
    
    if command == "off":
        is_on = False 
        break
    elif command == "report":
        coffee_maker.report()
        money_machine.report()
        continue
    
    order_menu = menu.find_drink(command)
    if coffee_maker.is_resource_sufficient(order_menu) and money_machine.make_payment(order_menu.cost):     
        coffee_maker.make_coffee(order_menu)
