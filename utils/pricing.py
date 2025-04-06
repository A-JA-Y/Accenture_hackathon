excess_threshold = 100
shortage_threshold = 20

def optimize_price(product_id, store_id, inventory_data, pricing_data, demand_data):
    current_price = pricing_data[
        (pricing_data['Product ID'] == product_id) &
        (pricing_data['Store ID'] == store_id)
    ]['Price'].values[0]

    elasticity = pricing_data[
        (pricing_data['Product ID'] == product_id) &
        (pricing_data['Store ID'] == store_id)
    ]['Elasticity Index'].values[0]

    competitor_price = pricing_data[
        (pricing_data['Product ID'] == product_id) &
        (pricing_data['Store ID'] == store_id)
    ]['Competitor Prices'].values[0]

    current_stock = inventory_data[
        (inventory_data['Product ID'] == product_id) &
        (inventory_data['Store ID'] == store_id)
    ]['Stock Levels'].values[0]

    if current_stock > excess_threshold:
        return calculate_clearance_price(current_price, elasticity)
    elif current_stock < shortage_threshold:
        return calculate_premium_price(current_price, elasticity)
    else:
        return calculate_competitive_price(current_price, competitor_price, elasticity)

# Sample implementations
def calculate_clearance_price(price, elasticity): return price * (1 - 0.1 * elasticity)
def calculate_premium_price(price, elasticity): return price * (1 + 0.05 * elasticity)
def calculate_competitive_price(price, comp_price, elasticity): return (price + comp_price) / 2
