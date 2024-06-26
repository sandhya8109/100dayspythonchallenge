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


def is_resource_enough(order_ingredients):
    """Returns True when order can be made and False if ingredient are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"sorry there is not enough {item}")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted"""
    print("print insert coins.")
    total = int(input("how many quarters:")) * 0.25
    total += int(input("how many dimes:")) * 0.1
    total += int(input("how many nickles:")) * 0.05
    total += int(input("how many pennies:")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """return True payment is accepted , or false if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorry money is not enough. money refunded")
        return False


def make_coffee(drink_name, oder_ingredients):
    """Deduct the required ingredient from the resources."""
    for item in oder_ingredients:
        resources[item] -= oder_ingredients[item]
    print(f"Here is your {drink_name}☕")


is_on = True
while is_on:
    user = input("What would you like?(espresso/latte/cappuccino):\n")
    if user == "off":
        is_on = False
    elif user == "report":
        print(f"water {resources['water']}ml")
        print(f"milk:{resources['milk']}ml")
        print(f"money:${profit} ")
        print(f"coffee: {resources['coffee']}g")
    else:
        drink = MENU[user]
        if is_resource_enough(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(user, drink["ingredients"])
