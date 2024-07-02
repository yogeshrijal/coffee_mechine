from manual import menu
from manual import resources

def cost(drink):

    cost_needed = menu[drink]["cost"]
    print(f"Total cost in dollars: {cost_needed}")
    quarters = float(input("How many quarters: "))
    dimes = float(input("How many dimes: "))
    nickels = float(input("How many nickels: "))
    pennies = float(input("How many pennies: "))
    total_inserted = float(quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01)
    if total_inserted < cost_needed:
        print("Not enough money")
        return False
    else:
        total_money_collected=0
        change = total_inserted - cost_needed
        total_money_collected+=cost_needed
        print(f"Your change is ${change:.2f}")
        print(f"total money collected = {total_money_collected}")
        return True

def total_resources():
    return resources

def check_resources(drink):
    ingredients_needed = menu[drink]["ingredients"]
    for item in ingredients_needed:
        if ingredients_needed[item] > resources[item]:
            print(f"We can't make your order, not enough {item}.")
            return False
    return True

def update_resources(drink):
    ingredients_needed = menu[drink]["ingredients"]
    for item in ingredients_needed:
        resources[item] -= ingredients_needed[item]
    return resources

from art import logo
print(logo)
print("Welcome to the coffee machine :)")
while True:
    coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
    milk_amount = resources['milk']
    water_amount = resources['water']
    coffee_amount = resources['coffee']
    if coffee == 'report':
        print(f" milk: {milk_amount}ml\n"
              f" water: {water_amount}ml\n"
              f" coffee: {coffee_amount}g")

    if coffee in menu:
        if check_resources(coffee):
            if cost(coffee):
                updated_resources = update_resources(coffee)
                print(f"Here is your {coffee}. Enjoy!")

            milk_amount = resources['milk']
            water_amount = resources['water']
            coffee_amount = resources['coffee']

        else:
            print("Insufficient resources to make coffee.")
    else:
        print("Invalid selection. Please choose from (espresso/latte/cappuccino).")
