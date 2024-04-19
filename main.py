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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}




def print_report():
    return f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${profit}"


def check_resources(choice):
    if MENU[choice]["ingredients"]["water"] > resources["water"]:
        print("Sorry there is not enough water.")
        return True
    elif choice != "espresso" and MENU[choice]["ingredients"]["milk"] > resources["milk"]:
        print("Sorry there is not enough milk.")
        return True
    elif MENU[choice]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry there is not enough coffee.")
        return True
    return False


def process_coins(choice):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    if total < MENU[choice]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    else:
        change = total - MENU[choice]["cost"]
        rounded = format(change, ".2f")
        reduce_resources(choice)
        global profit
        profit += MENU[choice]["cost"]
        print(f"Here is ${rounded} in change.")
        print(f"Here is your {choice} ☕ Enjoy")


def reduce_resources(choice):
    resources["water"] -= MENU[choice]["ingredients"]["water"]
    resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
    if choice != "espresso":
        resources["milk"] -= MENU[choice]["ingredients"]["milk"]



def make_coffee():
    should_make_coffee = True
    while should_make_coffee:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "report":
            print(print_report())
        elif choice == "off":
            should_make_coffee = False
        elif choice == "espresso":
            print("espresso")
            if check_resources(choice):
                continue
            process_coins(choice)
        elif choice == "latte":
            print("latte")
            if check_resources(choice):
                continue
            process_coins(choice)
        elif choice == "cappuccino":
            print("cappuccino")
            if check_resources(choice):
                continue
            process_coins(choice)
        else:
            print("Wrong input! Try again")


make_coffee()
