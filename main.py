Small_Pizza = 100
Medium_pizza = 200
Large_pizza = 300

Peproni_for_small = 20
Peproni_for_medium_and_large_size = 40

cheese = 10

size = input("Which size do you want to order : ").lower()
peproni_s = input("Do you  want to add peproni : ").lower()
extra_cheese = input("Do you  want to add cheese : ").lower()

bill = 0

# determining what size user wants
if size == "s":
    bill += Small_Pizza
elif size == "m":
    bill += Medium_pizza
else:
    bill += Large_pizza

# if user wants to add peproni
if peproni_s == "y":
    if size == "s":
        bill += Peproni_for_small
    else:
        bill += Peproni_for_medium_and_large_size

# if user wants mix extra cheese
if extra_cheese == "y":
    bill += cheese

print(f"Here is your order with bill ${bill}")
