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


def show_goods(goods):
    print("Product list:")
    for good in goods:
        print(good, "-", goods[good])


def get_goods(goods):
    choosen_good = input(
        "CHOOSE THE FRUIT (type in 'done' to complete your purchase): ")

    if choosen_good == "done":
        return None
    if choosen_good not in goods:
        print("Sorry, we are out of this good. Try again!")
        return get_goods(goods)
    return choosen_good


def get_quantity():
    return int(input("Quantity: "))


def print_receipt(cart, goods):
    print("\n\n ---RECEIPT")
    total = 0
    for good in cart:
        name = good[0]
        quantity = good[1]
        price = goods[name]
        amount = price * quantity
        print(f"{name:<8}  ({quantity} x {price} ntd) = {amount}")
        total += amount

    print("\n ---TOTAL:", total)


cart = []
while True:
    show_goods(goods)

    choosen_good = get_goods(goods)
    if choosen_good is None:
        break

    quantity = get_quantity()

    cart.append((choosen_good, quantity))

    tot = goods[choosen_good] * quantity
    print(f"Added: {choosen_good} in quantity {quantity} = {tot} ntd")

    subtotal = 0
    for good in cart:
        name = good[0]
        quantity = good[1]
        subtotal += goods[name] * quantity
    print("Subtotal:", subtotal)
    print("Current cart:", cart)  # print(tot)

print_receipt(cart, goods)
