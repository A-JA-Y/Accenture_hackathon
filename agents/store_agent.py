from utils.communication import send_message
from utils.forecasting import forecast_demand
from utils.inventory import calculate_optimal_stock
from datetime import date

def store_agent_process(store_id, inventory_data, demand_data, pricing_data):
    today = date.today()
    store_products = inventory_data[inventory_data['Store ID'] == store_id]

    for _, product in store_products.iterrows():
        product_id = product['Product ID']
        current_stock = product['Stock Levels']
        reorder_point = product.get('Reorder Point', 50)  # Default value

        if current_stock < reorder_point:
            forecast = forecast_demand(product_id, store_id, today, pricing_data, demand_data)
            stock_info = calculate_optimal_stock(product_id, store_id, forecast, inventory_data)
            quantity = stock_info['eoq']
            send_message(f"store_{store_id}", "warehouse", "RESUPPLY_REQUEST",
                         {"product_id": product_id, "quantity": int(quantity)})
