menu = {
    "Pizza": 450,
    "Pasta": 500,
    "Coffee": 350,
    "Tea": 100,
    "Cold Drink": 70,
    "Water": 50
}

# Greet
print("Welcome to My Python Restaurant")
print("Menu:")
for item, price in menu.items():
    print(f"{item}: {price}")

order_total = 0

while True:
    item = input("Enter the name of the item you want to order: ")
    if item in menu:
        order_total += menu[item]
        print(f"Your item {item} has been added to your order.")
    else:
        print(f"Ordered item {item} is not available yet!")
    
    another_item = input("Do you want to add another item? (Yes/No): ").strip().lower()
    if another_item != "yes":
        break

print(f"The total amount to pay is {order_total}.")
