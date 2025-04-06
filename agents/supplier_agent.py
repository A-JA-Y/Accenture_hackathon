class SupplierAgent:
    def __init__(self):
        self.order_history = []

    def generate_order(self, product_id, quantity):
        print(f"[Supplier] Generating production order for Product {product_id}, Quantity: {quantity}")
        self.order_history.append({
            "product_id": product_id,
            "quantity": quantity,
            "status": "In Production"
        })
