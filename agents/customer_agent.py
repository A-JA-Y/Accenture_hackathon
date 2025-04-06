class CustomerBehaviorAgent:
    def __init__(self, demand_data):
        self.demand_data = demand_data

    def get_expected_demand(self, product_id, store_id, current_date):
        # Placeholder: could use ML model or rules
        df = self.demand_data[
            (self.demand_data['Product ID'] == product_id) &
            (self.demand_data['Store ID'] == store_id)
        ]
        return df['Sales'].mean()
