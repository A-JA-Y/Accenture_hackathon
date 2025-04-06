from utils.communication import send_message
from utils.inventory import calculate_optimal_stock

class WarehouseAgent:
    def __init__(self, inventory_data):
        self.inventory_data = inventory_data

    def process_resupply_request(self, message):
        product_id = message.content["product_id"]
        quantity = message.content["quantity"]
        store_id = message.sender.split("_")[1]

        print(f"[Warehouse] Received RESUPPLY_REQUEST for Product {product_id} (Qty: {quantity}) from Store {store_id}")

        # Fulfill from warehouse stock (simulate)
        # In a real scenario, we would check available stock and trigger order if needed
        send_message("warehouse", f"store_{store_id}", "RESUPPLY_APPROVED",
                     {"product_id": product_id, "approved_quantity": quantity})
