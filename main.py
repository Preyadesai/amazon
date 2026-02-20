from users import UserManager
from products import ProductManager
from carts import CartManager
from orders import OrderManager

users = UserManager()
products = ProductManager()
cart = CartManager()
orders = OrderManager()

def welcome_menu():
    while True:
        print("\n=== WELCOME MENU ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            username = input("Username: ")
            password = input("Password: ")
            success, message = users.register(username, password)
            print(message)

        elif choice == "2":
            username = input("Username: ")
            password = input("Password: ")
            if users.login(username, password):
                print("Login successful.")
                store_menu(username)
            else:
                print("Invalid credentials.")

        elif choice == "3":
            break
        else:
            print("Invalid choice.")

def store_menu(username):
    while True:
        print("\n=== STORE MENU ===")
        print("1. Browse products")
        print("2. Search products")
        print("3. View cart")
        print("4. Checkout")
        print("5. Order history")
        print("6. Logout")

        choice = input("Choose: ")

        if choice == "1":
            for p in products.list_products():
                print(p)

        elif choice == "2":
            keyword = input("Search: ")
            results = products.search_products(keyword)
            for r in results:
                print(r)

        elif choice == "3":
            view_cart(username)

        elif choice == "4":
            checkout(username)

        elif choice == "5":
            user_orders = orders.get_user_orders(username)
            for o in user_orders:
                print(o)

        elif choice == "6":
            break
        else:
            print("Invalid choice.")

def view_cart(username):
    user_cart = cart.get_cart(username)
    total = 0
    for item in user_cart:
        product = products.get_product(item["product_id"])
        subtotal = product["price"] * item["qty"]
        total += subtotal
        print(f"{product['name']} x{item['qty']} - ${subtotal}")
    print("Total:", total)

def checkout(username):
    user_cart = cart.get_cart(username)
    if not user_cart:
        print("Cart is empty.")
        return

    total = 0
    order_items = []

    for item in user_cart:
        if not products.validate_stock(item["product_id"], item["qty"]):
            print("Stock issue detected.")
            return

    for item in user_cart:
        product = products.get_product(item["product_id"])
        products.reduce_stock(item["product_id"], item["qty"])
        subtotal = product["price"] * item["qty"]
        total += subtotal
        order_items.append({
            "product_id": item["product_id"],
            "qty": item["qty"],
            "unit_price": product["price"]
        })

    order = orders.create_order(username, order_items, total)
    cart.clear_cart(username)
    print("Order successful:", order["order_id"])

if __name__ == "__main__":
    welcome_menu()