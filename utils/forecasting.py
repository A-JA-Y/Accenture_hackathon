def forecast_demand(product_id, store_id, today, pricing_data, demand_data):
    elasticity_data = pricing_data[
        (pricing_data['Product ID'] == product_id) &
        (pricing_data['Store ID'] == store_id)
    ]['Elasticity Index'].values

    if elasticity_data.size == 0:
        # Handle missing elasticity data, e.g., use a default value or log a warning
        print(f"Warning: No elasticity data for product {product_id} at store {store_id}. Using default elasticity=0.")
        elasticity = 0
    else:
        elasticity = elasticity_data[0]

    # ... continue with your demand forecasting logic using elasticity ...
    # For example:
    forecast = 100  # placeholder logic
    return forecast