#Defining the menu of hotel 
menu = {
    'Pizza': 200,
    'Burger': 150,
    'Pasta': 180,
    'Salad': 100,
    'Coffee': 50,
    'Juice': 80,
    'Pastry': 120,
}

#Greet
print("Welcome to Vini's restaurant!")
print("Here is our menu:")
print("Pizza: Rs.200 \nBurger: Rs.150 \nPasta: Rs.180 \nSalad: Rs.100 \nCoffee: Rs.50 \nJuice: Rs.80 \nPastry: Rs.120")

order_total = 0                         #This will store the total of order like eg. 150+80 = 230

item_1 = input("Please enter the first item you would like to order: ")
if item_1 in menu:
    order_total += menu[item_1]         # 0+150 = 150
    print(f"{item_1} has been added to your order.")

else:
    print(f"Sorry, {item_1} is not on the menu.")

another_item = input("Would you like to order another item? (yes/no): ")
if another_item.lower() == 'yes':
    item_2 = input("Please enter the second item you would like to order: ")
    if item_2 in menu:
        order_total += menu[item_2]     # 150+80 = 230
        print(f"{item_2} has been added to your order.")
    else:
        print(f"Sorry, {item_2} is not on the menu.")

print(f"Your total order amount is: Rs.{order_total}")

