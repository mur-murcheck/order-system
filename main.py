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

    choosen_product = input(
        "CHOOSE THE FRUIT (type in 'done' to complete your purchase): ")

    if choosen_product == "done":
        break
    if choosen_product not in goods:
        print("The good is not in the list of goods. Try again!")

    quantity = int(input("Quantity: "))

    cart.append((choosen_product, quantity))
    tot = goods[choosen_product] * quantity
    print(tot)

print("\n\n ---RECIEPT")
total = 0
for good in cart:
    name = good[0]
    quantity = good[1]
    price = goods[name]
    amount = price * quantity
    print(f"{name} x {price} = {amount}")
    total += amount

print("\n ---TOTAL:", total)
