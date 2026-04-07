from datetime import datetime
goods = {
    1: {"name": "apple", "price": 20},
    2: {"name": "banana", "price": 45},
    3: {"name": "guava", "price": 50},
    4: {"name": "dragon fruit", "price": 75},
    5: {"name": "orange", "price": 30},
    6: {"name": "grape", "price": 350},
    7: {"name": "bala", "price": 40},
    8: {"name": "kiwi", "price": 75}
}

store = {
    "name": "Leka Store",
    "location": "Taichung, Taiwan"
}

customer = {
    "name": input("Your name: "),
    "phone": input("Your phone number: "),
    "address": input("Address for delivery: ")
}


def show_goods(goods):
    print("Product list:")
    for code in goods:
        print(code, ":", goods[code]["name"], "-", goods[code]["price"], "ntd")


def get_goods(goods):
    choosen_good = input(
        "CHOOSE PRODUCT NUMBER (type in '0' to complete your purchase): ")

    if choosen_good == "0":
        return None
    choosen_good = int(choosen_good)

    if choosen_good not in goods:
        print("Sorry, this product does not exist. Try again!")
        return get_goods(goods)
    return choosen_good


def get_quantity():
    return int(input("Quantity: "))


def print_receipt(cart, goods):
    print("\n\n ---RECEIPT---")
    print()
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M")
    print("Date:", formatted_time)
    print("Store:", store["name"])
    print("Location:", store["location"])
    print()
    print("Customer:", customer["name"])
    print("Phone:", customer["phone"])
    print("Address:", customer["address"])
    print("\n---------------------")
    total = 0
    for good in cart:
        code = good[0]
        quantity = good[1]
        name = goods[code]["name"]
        price = goods[code]["price"]
        amount = price * quantity
        print(f"{name:<13} ({quantity} x {price} ntd) = {amount} ntd")
        total += amount
    print("\n ---TOTAL:", total, "ntd")


cart = []
while True:
    if cart:
        print()
    show_goods(goods)

    choosen_good = get_goods(goods)
    if choosen_good is None:
        break

    quantity = get_quantity()

    found = False
    for i in range(len(cart)):
        code = cart[i][0]
        old_quantity = cart[i][1]
        if code == choosen_good:
            cart[i] = (code, old_quantity + quantity)
            found = True
            break
    if not found:
        cart.append((choosen_good, quantity))

    tot = goods[choosen_good]["price"] * quantity
    print(
        f"\nAdded: {goods[choosen_good]["name"]} in quantity {quantity} = {tot} ntd")

    subtotal = 0
    print("Current cart:")
    for good in cart:
        code = good[0]
        quantity = good[1]
        name = goods[code]["name"]
        price = goods[code]["price"]
        amount = price * quantity

        print(name, quantity, "x", price, "ntd =", amount, "ntd")  # print(tot)
        subtotal += amount
    print("\nSubtotal:", subtotal)

print_receipt(cart, goods)
