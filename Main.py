import pandas as pd 
from agents.store_agent import store_agent_process
from agents.warehouse_agent import WarehouseAgent
from agents.supplier_agent import SupplierAgent
from agents.customer_agent import CustomerBehaviorAgent
from agents.coordinator_agent import CoordinatorAgent

inventory_data = pd.read_csv("data/inventory_monitoring.csv")
demand_data = pd.read_csv("data/demand_forecasting.csv")
pricing_data = pd.read_csv("data/pricing_optimization.csv")


store_ids = inventory_data['Store ID'].unique()
store_agents = {f"store_{sid}": store_agent_process for sid in store_ids}


warehouse_agent = WarehouseAgent(inventory_data)
supplier_agent = SupplierAgent()
customer_agent = CustomerBehaviorAgent(demand_data)


coordinator = CoordinatorAgent(store_agents, warehouse_agent, supplier_agent, customer_agent)


for step in range(3):
    print(f"\n🌀 [Simulation Step {step + 1}]")
    coordinator.step(inventory_data, demand_data, pricing_data)
