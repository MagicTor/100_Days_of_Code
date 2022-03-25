MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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


def update_resources(drink):
    global resources
    for i in MENU[drink]['ingredients']:
        resources[i] -= MENU[drink]['ingredients'][i]


def calculate_money():
    print("Please insert coins.")
    quarters = int(input("How many quarters: ")) * 0.25
    dimes = int(input("How many dimes: ")) * 0.10
    nickles = int(input("How many nickles: ")) * 0.05
    pennies = int(input("How many pennies: ")) * 0.01
    return quarters + dimes + nickles + pennies


def enough_resources(drink):
    for i in MENU[drink]['ingredients']:
        if resources[i] < MENU[drink]['ingredients'][i]:
            print(f"Sorry there is not enough {i}.")
            return False
    return True


profit = 0.0
is_true = True
while is_true:
    drink_selection = input("What would you like? (espresso/latte/cappuccino): ")
    if drink_selection == 'off':
        is_true = False
    elif drink_selection == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif enough_resources(drink_selection):
        price = MENU[drink_selection]['cost']
        funds = calculate_money()
        if funds >= price:
            print(f"Here is ${round(funds-price,2)} in change.")
            print("Here is your espresso ☕️. Enjoy!")
            update_resources(drink_selection)
            profit += MENU[drink_selection]['cost']
        else:
            print("Sorry that's not enough money. Money refunded.")
