import random

def simulate_demand_spike(demand, probability=0.1):
    if random.random() < probability:
        print("⚡ Demand Spike!")
        return demand * random.uniform(1.5, 2.5)
    return demand

def simulate_supplier_delay(probability=0.05):
    return random.random() < probability
