from storage import Storage
from datetime import datetime
import uuid

class OrderManager:
    FILE = "orders.json"

    def __init__(self):
        self.orders = Storage.load(self.FILE)

    def generate_order_id(self):
        return "O" + uuid.uuid4().hex[:6].upper()

    def create_order(self, username, items, total):
        order = {
            "order_id": self.generate_order_id(),
            "username": username,
            "items": items,
            "total": total,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.orders.append(order)
        Storage.save(self.FILE, self.orders)
        self.export_receipt(order)
        return order

    def get_user_orders(self, username):
        return [o for o in self.orders if o["username"] == username]

    def export_receipt(self, order):
        filename = f"receipt_{order['order_id']}.txt"
        with open(filename, "w") as f:
            f.write(f"Order ID: {order['order_id']}\n")
            f.write(f"User: {order['username']}\n")
            f.write(f"Date: {order['timestamp']}\n\n")
            for item in order["items"]:
                f.write(f"{item['product_id']} x{item['qty']} - ${item['unit_price']}\n")
            f.write(f"\nTotal: ${order['total']}\n")