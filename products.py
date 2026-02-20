from storage import Storage

class ProductManager:
    FILE = "products.json"

    def __init__(self):
        self.products = Storage.load(self.FILE)
        if not self.products:
            self.products = [
                {"product_id": "P1001", "name": "USB-C Cable", "price": 9.99, "stock": 30},
                {"product_id": "P1002", "name": "Wireless Mouse", "price": 19.99, "stock": 15},
                {"product_id": "P1003", "name": "Keyboard", "price": 29.99, "stock": 10}
            ]
            Storage.save(self.FILE, self.products)

    def list_products(self):
        return self.products

    def search_products(self, keyword):
        return [p for p in self.products if keyword.lower() in p["name"].lower()]

    def get_product(self, product_id):
        for p in self.products:
            if p["product_id"] == product_id:
                return p
        return None

    def validate_stock(self, product_id, qty):
        product = self.get_product(product_id)
        return product and product["stock"] >= qty

    def reduce_stock(self, product_id, qty):
        product = self.get_product(product_id)
        if product:
            product["stock"] -= qty
            Storage.save(self.FILE, self.products)