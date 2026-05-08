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


def get_customer():
    name = input("Your name: ")
    while name == "":
        print("Name is required.")
        name = input("Please type in your name: ")
    
    phone = input("Your phone number: ")
    while not phone.isdigit() or len(phone) != 10 or not phone.startswith("09"):
        print("Phone number must contain 10 digits and star with 09.")
        phone = input("Your phone number: ")

    address = input("Address for delivery: ")
    while address == "":
        print("Address for delivery is required.")
        address = input("Address for delivery: ")

    return {
        "name": name,
        "phone": phone,
        "address": address
    }


def show_goods(goods):
    print("Product list:")
    for code in goods:
        print(code, ":", goods[code]["name"], "-", goods[code]["price"], "ntd")
    print()
    print("x: remove item from cart")
    print("c: clear the cart")
    print("0: complete your order")
    

def get_goods(goods):
    choosen_good = input(
        "CHOOSE PRODUCT NUMBER: ").strip()

    if choosen_good == "0":
        return None
    if choosen_good.lower() == "c":
        return "clear"
    if choosen_good.lower() == "x":
        return "remove"
    try:
        choosen_good = int(choosen_good)
    except ValueError:
        print("Please enter a valid product number. Only an even digit 1 to 8.")
        return get_goods(goods)
    
    if choosen_good not in goods:
        print("Sorry, this product does not exist. Try again!")
        return get_goods(goods)
    return choosen_good


def get_quantity():
    quantity = input("Quantity: ").strip()

    try:
        quantity = int(quantity)
    except ValueError:
        print("Please enter a valid number.")
        return get_quantity()

    if quantity <= 0:
        print("Quantity must be a digit greater than zero.")
        return get_quantity()

    if quantity > 100:
        confirm = input(
            "That seems like a lot. Are you sure? (y = yes/n = no): ").strip().lower()
        if confirm != "y":
            return get_quantity()

    return quantity


def remove_from_card(cart, goods):
    if not cart:
        print("Cart is empty, nothing to remove.")
        return cart

    remove_code = input("Enter product code to remove: ").strip()

    try:
        remove_code = int(remove_code)
    except ValueError:
        print("Please enter a valid product code.")
        return cart

    for i in range(len(cart)):
        code = cart[i][0]

        if code == remove_code:
            removed_item = cart.pop(i)
            print(goods[removed_item[0]]["name"], "removed from cart")
            return cart
        
    print("This product isnot in the cart.")
    return cart


def clear_cart(cart):
    if not cart:
        print("Cart is already empty.")
        return cart

    return cart


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


customer = get_customer()


cart = []
while True:
    if cart:
        print()
    show_goods(goods)

    choosen_good = get_goods(goods)
    if choosen_good is None:
        break
    if choosen_good == "remove":
        cart = remove_from_card(cart, goods)
        continue
    if choosen_good == "clear":
        cart = clear_cart(cart)
        continue

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
        f"\nAdded: {goods[choosen_good]['name']} in quantity {quantity} = {tot} ntd")

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
    print("\nSubtotal:", subtotal, "ntd")

if not cart:
    print("\nCart is empty. No receipt generated.")
else:
    print_receipt(cart, goods)
