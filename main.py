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
    choosen_product = input(
        "CHOOSE THE FRUIT (type in 'done' to complete your purchase): ")

    if choosen_product == "done":
        return None
    if choosen_product not in goods:
        print("Sorry, we are out of this good. Try again!")
        return get_goods(goods)


def get_quantity():
    return int(input("Quantity: "))


def print_reciept(cart, goods):
    print("\n\n ---RECIEPT")
    total = 0
    for good in cart:
        name = good[0]
        quantity = good[1]
        price = goods[name]
        amount = price * quantity
        print(f"{name:<8}  ({quantity} x {price} ntd = {amount}")
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
    print(tot)

print_reciept(cart, goods)
