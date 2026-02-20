from storage import Storage

class CartManager:
    FILE = "carts.json"

    def __init__(self):
        self.carts = Storage.load(self.FILE)
        if not isinstance(self.carts, dict):
            self.carts = {}

    def get_cart(self, username):
        return self.carts.get(username, [])

    def add_to_cart(self, username, product_id, qty):
        if username not in self.carts:
            self.carts[username] = []

        for item in self.carts[username]:
            if item["product_id"] == product_id:
                item["qty"] += qty
                Storage.save(self.FILE, self.carts)
                return

        self.carts[username].append({
            "product_id": product_id,
            "qty": qty
        })
        Storage.save(self.FILE, self.carts)

    def remove_from_cart(self, username, product_id):
        if username in self.carts:
            self.carts[username] = [
                item for item in self.carts[username]
                if item["product_id"] != product_id
            ]
            Storage.save(self.FILE, self.carts)

    def clear_cart(self, username):
        self.carts[username] = []
        Storage.save(self.FILE, self.carts)