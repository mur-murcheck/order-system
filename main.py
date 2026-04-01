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

cart = []
while True:
    print("Product list:")
    for good in goods:
        print(good, "-", goods[good])

    choosen_product = input("Choose the product: ")
    if choosen_product == "done":
        break

    quantity = int(input("Quantity: "))

    cart.append((choosen_product, quantity))
    tot = goods[choosen_product] * quantity
    print(tot)
print(cart)

# total = goods[choosen_product] * quantity
# print("Total:", total)
