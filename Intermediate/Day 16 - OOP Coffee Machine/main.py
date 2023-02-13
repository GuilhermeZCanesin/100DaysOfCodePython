from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_on = True
machine_profit = 0
money_machine = MoneyMachine()
coffe_maker = CoffeeMaker()
menu = Menu()

while machine_on:
    options = menu.get_items()
    request = input(f"What would you like? ({options}): ")

    if request == "off":
        machine_on = False
    elif request == "report":
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(request)
        if coffe_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffe_maker.make_coffee(drink)
