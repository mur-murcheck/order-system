goods = {
    "apple": 20,
    "banana": 45,
    "guava": 50,
    "dragon fruct": 75,
    "orange": 30,
    "grape": 350,
    "bala": 40,
    "kiwi": 75
}

print("Product list:")
for good in goods:
    print(good, "-", goods[good])

chosen_product = input("Choose the product: ")
quantity = int(input("Quantity: "))
total = goods[chosen_product] * quantity
print("Total:", total)
