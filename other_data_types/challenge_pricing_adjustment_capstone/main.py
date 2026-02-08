grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15)
}

eggs_info = grocery_inventory["Eggs"]
milk_info = grocery_inventory["Milk"]

if eggs_info[1] > 5:
    grocery_inventory["Eggs"] = (
        eggs_info[0],
        eggs_info[1] - 1,
        eggs_info[2]
    )
    print("Eggs are too expensive, reducing the price by $1.")
    
grocery_inventory.update({"Tomatoes": ("Produce", 1.20, 30)})
print("Inventory after adding Tomatoes:", grocery_inventory)

if milk_info[2] < 10:
    grocery_inventory["Milk"] = (
        milk_info[0],
        milk_info[1],
       milk_info[2] + 20
    )
    print("Milk needs to be restocked. Increasing stock by 20 units.")

print("Updated inventory:", grocery_inventory)