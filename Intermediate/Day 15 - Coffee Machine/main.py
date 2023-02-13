MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
machine_on = True
machine_profit = 0


def get_coins():
    print("------------------------------------")
    print("Please insert coins...")
    print("------------------------------------")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    amount = quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01
    print("------------------------------------")
    print(f"Total amount: ${amount}")
    print("------------------------------------")
    return amount


def get_drink(requested_drink, money):
    drink = MENU[requested_drink]
    change = money
    resources.update({
        "water": resources["water"] - drink['ingredients']['water'],
        "milk": resources["milk"] - drink['ingredients']['milk'],
        "coffee": resources["coffee"] - drink['ingredients']['coffee'],
    })
    change -= drink['cost']
    global machine_profit
    machine_profit += drink['cost']
    return change


def check_availability(requested_drink):
    drink = MENU[requested_drink]['ingredients']
    for item in drink:
        if drink[item] > resources[item]:
            print(f"Too bad not enough {item} in the machine to produce your {requested_drink}, sorry!")
            return False

    return True


def check_cash(requested_drink, coins_deposited):
    drink = MENU[requested_drink]
    if coins_deposited < drink['cost']:
        print(f"Not enough coins were inserted! You are ${drink['cost'] - coins_deposited} short... "
              f"Here is your ${coins_deposited} back.")
        return False
    return True


while machine_on:
    request = input("What would you like? (espresso/latte/capuccino): ")

    if request == "off":
        machine_on = False
    elif request == "report":
        print("------------------------------------")
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${machine_profit}")
        print("------------------------------------")
    elif request == "espresso" or "latte" or "cappuccino":
        available = check_availability(request)
        if available:
            coins_inserted = get_coins()
            has_money = check_cash(request, coins_inserted)
            if has_money:
                change_from_machine = get_drink(request, coins_inserted)
                if change_from_machine > 0:
                    print(f"Here is ${change_from_machine} in change.")
                print(f"And here is your {request}... Enjoy!")
    else:
        print(f"Sorry there is no drink with the name '{request}'...")
