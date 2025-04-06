def calculate_optimal_stock(product_id, store_id, forecast_demand, inventory_data):
    current_stock = inventory_data[
        (inventory_data['Product ID'] == product_id) &
        (inventory_data['Store ID'] == store_id)
    ]['Stock Levels'].values[0]

    lead_time = inventory_data[
        (inventory_data['Product ID'] == product_id) &
        (inventory_data['Store ID'] == store_id)
    ]['Supplier Lead Time (days)'].values[0]

    stockout_freq = inventory_data[
        (inventory_data['Product ID'] == product_id) &
        (inventory_data['Store ID'] == store_id)
    ]['Stockout Frequency'].values[0]

    safety_stock = calculate_safety_stock(forecast_demand, lead_time, stockout_freq)
    reorder_point = (forecast_demand * lead_time) + safety_stock
    eoq = calculate_eoq(forecast_demand, ordering_cost=10, holding_cost=2)

    return {'current_stock': current_stock, 'reorder_point': reorder_point, 'eoq': eoq}

def calculate_safety_stock(forecast, lead_time, freq): return forecast * lead_time * (freq / 100)
def calculate_eoq(demand, ordering_cost, holding_cost): return ((2 * demand * ordering_cost) / holding_cost) ** 0.5
