# simple shopping list
item = input("Item bought: ")
quantity = int(input("Number of items bought: "))
price = float(input("Item price: "))
print()
total_price = quantity * price

print(f"You bought {quantity} {item}/s with the total cost being Ksh {total_price}")